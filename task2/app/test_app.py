from unittest.mock import MagicMock

import pytest

import app as flask_app


@pytest.fixture
def client():
    flask_app.app.config["TESTING"] = True
    with flask_app.app.test_client() as client:
        yield client


def test_welcome_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Welcome to my Coderco Docker Project!"


def test_count_route_increments_and_returns_value(client, monkeypatch):
    mock_redis = MagicMock()
    mock_redis.incr.return_value = 1

    monkeypatch.setattr(flask_app, "client", mock_redis)

    response = client.get("/count")
    assert response.status_code == 200
    assert response.data.decode() == "You are Visitor number: 1"
    mock_redis.incr.assert_called_once_with("visitor_count")
