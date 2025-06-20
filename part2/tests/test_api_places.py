import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1"
PLACES_URL = f"{BASE_URL}/places"
USERS_URL = f"{BASE_URL}/users"

@pytest.fixture(scope="module")
def test_user():
    """Create a user to be able to create a place."""
    data = {
        "first_name": "Owner",
        "last_name": "Test",
        "email": "owner@test.com",
        "password": "ownerpass"
    }
    res = requests.post(USERS_URL, json=data)
    if res.status_code == 409:
        users = requests.get(USERS_URL).json()
        user = next((u for u in users if u["email"] == data["email"]), None)
        return user["id"]
    return res.json()["id"]

@pytest.fixture
def test_place_data(test_user):
    """Returns valid data to create a place."""
    return {
        "title": "Beautiful Cabin",
        "description": "A cozy wooden cabin in the mountains.",
        "price": 120.0,
        "latitude": 45.123,
        "longitude": -72.456,
        "owner_id": test_user
    }

@pytest.fixture
def created_place(test_place_data):
    """Create a place to test."""
    res = requests.post(PLACES_URL, json=test_place_data)
    assert res.status_code == 201
    return res.json()["id"]

def test_create_place_success(test_place_data):
    res = requests.post(PLACES_URL, json=test_place_data)
    assert res.status_code == 201
    body = res.json()
    assert "id" in body
    assert body["title"] == test_place_data["title"]

def test_create_place_invalid_owner():
    data = {
        "title": "Fake Place",
        "description": "Owner doesn't exist",
        "price": 100.0,
        "latitude": 0.0,
        "longitude": 0.0,
        "owner_id": "invalid-id",
        "amenities": []
    }
    res = requests.post(PLACES_URL, json=data)
    assert res.status_code == 404
    assert res.json()["error"] == "User not found"

def test_get_all_places():
    res = requests.get(PLACES_URL)
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_place_by_id_success(created_place):
    res = requests.get(f"{PLACES_URL}/{created_place}")
    assert res.status_code == 200
    data = res.json()
    assert "title" in data
    assert "price" in data

def test_get_place_not_found():
    res = requests.get(f"{PLACES_URL}/nonexistent-id")
    assert res.status_code == 404
    assert res.json()["error"] == "Place not found"

def test_update_place_success(created_place, test_user):
    data = {
        "title": "Updated Title",
        "description": "Updated desc",
        "price": 150.0,
        "latitude": 40.0,
        "longitude": -70.0,
        "owner_id": test_user,
        "amenities": []
    }
    res = requests.put(f"{PLACES_URL}/{created_place}", json=data)
    assert res.status_code == 200
    assert res.json()["message"] == "Place updated successfully"

def test_update_place_not_found(test_place_data):
    res = requests.put(f"{PLACES_URL}/nonexistent-id", json=test_place_data)
    assert res.status_code == 404
    assert res.json()["error"] == "Place not found"

