import logging
import os
import psycopg2
from flask import Flask, jsonify, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
from psycopg2.extras import RealDictCursor

REQUESTS = Counter('apex_api_requests_total', 'Total API requests', ['method', 'endpoint', 'status'])


def create_app(config=None):
    app = Flask(__name__)
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'postgresql://apex:change-me@db:5432/apex')
    app.config['MAX_CONTENT_LENGTH'] = 16384
    if config:
        app.config.update(config)
    logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'), format='%(asctime)s %(levelname)s %(message)s')

    def connect():
        return psycopg2.connect(app.config['DATABASE_URL'], connect_timeout=3)

    @app.after_request
    def metrics(response):
        REQUESTS.labels(request.method, request.path, str(response.status_code)).inc()
        return response

    @app.get('/')
    def index():
        return jsonify(service='apex-operations-api', version='1.0.0')

    @app.get('/health')
    def health():
        return jsonify(status='healthy'), 200

    @app.get('/ready')
    def ready():
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT 1')
            return jsonify(status='ready', database='connected'), 200
        except Exception:
            app.logger.exception('readiness_check_failed')
            return jsonify(status='not_ready', database='unavailable'), 503

    @app.get('/items')
    def list_items():
        try:
            with connect() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute('SELECT id, name, created_at FROM items ORDER BY id')
                    rows = cur.fetchall()
            return jsonify(items=[dict(row, created_at=row['created_at'].isoformat()) for row in rows]), 200
        except Exception:
            app.logger.exception('list_items_failed')
            return jsonify(error='internal_server_error'), 500

    @app.post('/items')
    def create_item():
        data = request.get_json(silent=True)
        if not isinstance(data, dict) or not isinstance(data.get('name'), str):
            return jsonify(error='name_must_be_a_string'), 400
        name = data['name'].strip()
        if not name or len(name) > 120:
            return jsonify(error='name_must_be_between_1_and_120_characters'), 400
        try:
            with connect() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute('INSERT INTO items (name) VALUES (%s) RETURNING id, name, created_at', (name,))
                    row = cur.fetchone()
            return jsonify(item=dict(row, created_at=row['created_at'].isoformat())), 201
        except Exception:
            app.logger.exception('create_item_failed')
            return jsonify(error='internal_server_error'), 500

    @app.get('/metrics')
    def metric_endpoint():
        return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

    @app.errorhandler(413)
    def too_large(_error):
        return jsonify(error='request_too_large'), 413

    return app


app = create_app()
