from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_add_valid_numbers():
    response = client.post("/api/v1/add", json={"a": 5, "b": 10})
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}

def test_add_negative_and_decimal_numbers():
    response = client.post("/api/v1/add", json={"a": -2.5, "b": 7.5})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_add_invalid_non_numeric():
    response = client.post("/api/v1/add", json={"a": "abc", "b": 10})
    assert response.status_code == 422

def test_add_missing_field():
    response = client.post("/api/v1/add", json={"a": 5})
    assert response.status_code == 422
