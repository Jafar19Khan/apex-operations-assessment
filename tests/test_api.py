from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest

from app.main import create_app


def client():
    return create_app({'TESTING': True}).test_client()


def database_connection(cursor):
    """Return a connection mock that behaves like psycopg2's context manager."""
    connection = MagicMock()
    connection.__enter__.return_value = connection
    connection.cursor.return_value.__enter__.return_value = cursor
    return connection


def test_root():
    response = client().get('/')
    assert response.status_code == 200
    assert response.json['service'] == 'apex-operations-api'


def test_health():
    response = client().get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_ready_database_down(monkeypatch):
    monkeypatch.setattr(
        'app.main.psycopg2.connect',
        MagicMock(side_effect=Exception('offline')),
    )
    response = client().get('/ready')
    assert response.status_code == 503
    assert response.json == {'status': 'not_ready', 'database': 'unavailable'}


def test_ready_database_connected(monkeypatch):
    cursor = MagicMock()
    connection = database_connection(cursor)
    monkeypatch.setattr('app.main.psycopg2.connect', MagicMock(return_value=connection))

    response = client().get('/ready')

    assert response.status_code == 200
    assert response.json == {'status': 'ready', 'database': 'connected'}
    connection.cursor.assert_called_once_with()
    cursor.execute.assert_called_once_with('SELECT 1')


def test_create_item(monkeypatch):
    created_at = datetime(2026, 10, 31, tzinfo=timezone.utc)
    cursor = MagicMock()
    cursor.fetchone.return_value = {'id': 1, 'name': 'sample', 'created_at': created_at}
    connection = database_connection(cursor)
    monkeypatch.setattr('app.main.psycopg2.connect', MagicMock(return_value=connection))

    response = client().post('/items', json={'name': ' sample '})

    assert response.status_code == 201
    assert response.json['item']['id'] == 1
    assert response.json['item']['name'] == 'sample'
    assert response.json['item']['created_at'] == created_at.isoformat()
    assert cursor.execute.call_args.args[1] == ('sample',)


def test_list_items(monkeypatch):
    created_at = datetime(2026, 10, 31, tzinfo=timezone.utc)
    cursor = MagicMock()
    cursor.fetchall.return_value = [
        {'id': 1, 'name': 'sample', 'created_at': created_at}
    ]
    connection = database_connection(cursor)
    monkeypatch.setattr('app.main.psycopg2.connect', MagicMock(return_value=connection))

    response = client().get('/items')

    assert response.status_code == 200
    assert response.json['items'][0]['name'] == 'sample'
    assert response.json['items'][0]['created_at'] == created_at.isoformat()


def test_missing_name_rejected():
    assert client().post('/items', json={}).status_code == 400


def test_non_string_name_rejected():
    assert client().post('/items', json={'name': 42}).status_code == 400


def test_blank_name_rejected():
    assert client().post('/items', json={'name': '  '}).status_code == 400


def test_long_name_rejected():
    assert client().post('/items', json={'name': 'x' * 121}).status_code == 400


def test_metrics_endpoint():
    response = client().get('/metrics')
    assert response.status_code == 200
    assert b'apex_api_requests_total' in response.data


@pytest.mark.intentional_failure
def test_intentional_failure_demo():
    """This test is expected to fail when run alone for the CI gate demo."""
    assert 'expected failure' == 'passing test'
