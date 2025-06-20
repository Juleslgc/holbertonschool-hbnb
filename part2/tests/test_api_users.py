import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1/users"

test_user = {
    "first_name": "Alice",
    "last_name": "Wonder",
    "email": "alice@example.com",
    "password": "test123"
}

@pytest.fixture(scope="module")
def created_user():

    response = requests.post(BASE_URL, json=test_user)
    assert response.status_code in (201, 409)

    if response.status_code == 201:
        return response.json()["id"]
    else:

        users = requests.get(BASE_URL).json()
        user = next((u for u in users if u["email"] == test_user["email"]), None)
        return user["id"]


def test_create_user_success():
    data = {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob@example.com",
        "password": "secret"
    }
    response = requests.post(BASE_URL, json=data)
    assert response.status_code == 201
    json = response.json()
    assert "id" in json
    assert json["email"] == data["email"]

def test_create_user_conflict():
    valid_email = "bob@example.com"

    data_1 = {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": valid_email,
        "password": "secret"
    }

    response2 = requests.post(BASE_URL, json=data_1)
    assert response2.status_code == 409
    assert response2.json()["error"] == "Email already registered"

def test_get_all_users():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id_success(created_user):
    response = requests.get(f"{BASE_URL}/{created_user}")
    assert response.status_code == 200
    json = response.json()
    assert json["email"] == test_user["email"]

def test_get_user_by_id_not_found():
    response = requests.get(f"{BASE_URL}/nonexistent-id")
    assert response.status_code == 404
    assert "error" in response.json()

def test_update_user_success(created_user):
    data = {
        "first_name": "Alice",
        "email": "alice@example.com"
    }
    response = requests.put(f"{BASE_URL}/{created_user}", json=data)
    assert response.status_code == 200
    assert response.json()["first_name"] == "Alice"
    assert response.json()["email"] == "alice@example.com"

def test_update_user_invalid_email(created_user):
    data = {"email": "not-an-email"}
    response = requests.put(f"{BASE_URL}/{created_user}", json=data)
    assert response.status_code == 400

def test_update_user_conflict_email(created_user):

    data = {
        "first_name": "Temp",
        "last_name": "User",
        "email": "temp@example.com",
        "password": "1234"
    }
    res = requests.post(BASE_URL, json=data)
    other_user_id = res.json().get("id")


    conflict_data = {"email": "temp@example.com"}
    conflict_res = requests.put(f"{BASE_URL}/{created_user}", json=conflict_data)
    assert conflict_res.status_code == 409
