from unittest.mock import MagicMock
import pytest
from app.main import create_app


def client():
    return create_app({'TESTING': True}).test_client()


def test_root():
    assert client().get('/').json['service'] == 'apex-operations-api'


def test_health():
    response = client().get('/health')
    assert response.status_code == 200 and response.json['status'] == 'healthy'


def test_ready_database_down(monkeypatch):
    monkeypatch.setattr('app.main.psycopg2.connect', MagicMock(side_effect=Exception('offline')))
    response = client().get('/ready')
    assert response.status_code == 503


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
    assert response.status_code == 200 and b'apex_api_requests_total' in response.data


@pytest.mark.intentional_failure
def test_intentional_failure_demo():
    """Run separately; this test is expected to fail to demonstrate a CI gate."""
    assert 'expected failure' == 'passing test'
