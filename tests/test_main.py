from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_exit(mocker):
    mock_exit = mocker.patch('os._exit')
    response = client.get("/exit")
    mock_exit.assert_called_once_with(0)

def test_error(mocker):
    mock_exit = mocker.patch('os._exit')
    response = client.get("/error")
    mock_exit.assert_called_once_with(1)