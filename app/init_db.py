import os
import time
import psycopg2

for attempt in range(30):
    try:
        with psycopg2.connect(os.environ['DATABASE_URL'], connect_timeout=3) as conn:
            with conn.cursor() as cur:
                cur.execute('CREATE TABLE IF NOT EXISTS items (id BIGSERIAL PRIMARY KEY, name VARCHAR(120) NOT NULL, created_at TIMESTAMPTZ NOT NULL DEFAULT NOW())')
        print('Database schema ready.')
        break
    except psycopg2.OperationalError:
        if attempt == 29:
            raise
        time.sleep(2)
