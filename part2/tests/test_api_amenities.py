import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1"
AMENITIES_URL = f"{BASE_URL}/amenities"

@pytest.fixture
def amenity_data():
    return {
        "name": "WiFi"
    }

@pytest.fixture
def created_amenity(amenity_data):
    res = requests.post(AMENITIES_URL, json=amenity_data)
    assert res.status_code == 201
    return res.json()["id"]

def test_create_amenity_success(amenity_data):
    res = requests.post(AMENITIES_URL, json=amenity_data)
    assert res.status_code == 201
    assert "id" in res.json()
    assert res.json()["name"] == amenity_data["name"]

def test_create_amenity_invalid_input():
    res = requests.post(AMENITIES_URL, json={})  # missing required field
    assert res.status_code == 400
    assert "error" in res.json()

def test_get_all_amenities():
    res = requests.get(AMENITIES_URL)
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_amenity_by_id(created_amenity):
    res = requests.get(f"{AMENITIES_URL}/{created_amenity}")
    assert res.status_code == 200
    assert "name" in res.json()

def test_get_amenity_not_found():
    res = requests.get(f"{AMENITIES_URL}/nonexistent-id")
    assert res.status_code == 404 or res.status_code == 400  # dépend de ton exception

def test_update_amenity_success(created_amenity):
    updated_data = {
        "name": "Updated Amenity"
    }
    res = requests.put(f"{AMENITIES_URL}/{created_amenity}", json=updated_data)
    assert res.status_code == 200
    assert res.json()["message"] == "Amenity updated successfully"

def test_update_amenity_not_found():
    updated_data = {
        "name": "Test"
    }
    res = requests.put(f"{AMENITIES_URL}/nonexistent-id", json=updated_data)
    assert res.status_code == 404

