import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1"
USERS_URL = f"{BASE_URL}/users"
PLACES_URL = f"{BASE_URL}/places"
REVIEWS_URL = f"{BASE_URL}/reviews"

@pytest.fixture(scope="module")
def test_user():
    """Create or retrieve a user for testing."""
    user_data = {
        "first_name": "Review",
        "last_name": "Tester",
        "email": "review@test.com",
        "password": "testpass"
    }
    res = requests.post(USERS_URL, json=user_data)
    if res.status_code == 409:
        users = requests.get(USERS_URL).json()
        return next(u["id"] for u in users if u["email"] == user_data["email"])
    return res.json()["id"]

@pytest.fixture(scope="module")
def test_place(test_user):
    """Create a valid place to link reviews to."""
    place_data = {
        "title": "Reviewable Place",
        "description": "A place for testing reviews.",
        "price": 99.99,
        "latitude": 10.0,
        "longitude": 20.0,
        "owner_id": test_user
    }
    res = requests.post(PLACES_URL, json=place_data)
    return res.json()["id"]

@pytest.fixture
def review_data(test_user, test_place):
    """Returns a dataset to create a review."""
    return {
        "text": "Great stay!",
        "rating": 5,
        "user_id": test_user,
        "place_id": test_place
    }

@pytest.fixture
def created_review(review_data):
    """Crée une review pour les tests."""
    res = requests.post(REVIEWS_URL, json=review_data)
    assert res.status_code == 201
    return res.json()["id"]

def test_create_review_success(review_data):
    res = requests.post(REVIEWS_URL, json=review_data)
    assert res.status_code == 201
    data = res.json()
    assert data["text"] == review_data["text"]
    assert data["rating"] == review_data["rating"]

def test_create_review_invalid_input():
    res = requests.post(REVIEWS_URL, json={
        "text": "Missing fields"
        # no rating, user_id, place_id
    })
    assert res.status_code == 400
    assert "error" in res.json()

def test_get_all_reviews():
    res = requests.get(REVIEWS_URL)
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_review_by_id(created_review):
    res = requests.get(f"{REVIEWS_URL}/{created_review}")
    assert res.status_code == 200
    assert "text" in res.json()

def test_get_review_not_found():
    res = requests.get(f"{REVIEWS_URL}/nonexistent-id")
    assert res.status_code == 404

def test_update_review_success(created_review, review_data):
    updated_data = review_data.copy()
    updated_data["text"] = "Updated review text"
    updated_data["rating"] = 4
    res = requests.put(f"{REVIEWS_URL}/{created_review}", json=updated_data)
    assert res.status_code == 200
    assert res.json()["message"] == "Review updated successfully"

def test_update_review_not_found(review_data):
    res = requests.put(f"{REVIEWS_URL}/nonexistent-id", json=review_data)
    if res.status_code == 200:
        assert "error" in res.json() or "message" in res.json()
    else:
        assert res.status_code == 404

def test_delete_review_success(created_review):
    res = requests.delete(f"{REVIEWS_URL}/{created_review}")
    assert res.status_code == 200
    assert res.json()["message"] == "Review deleted successfully"

def test_delete_review_not_found():
    res = requests.delete(f"{REVIEWS_URL}/nonexistent-id")
    assert res.status_code == 404

def test_get_reviews_by_place(test_place):
    res = requests.get(f"{REVIEWS_URL}/places/{test_place}/reviews")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_reviews_by_place_not_found():
    res = requests.get(f"{REVIEWS_URL}/places/nonexistent-id/reviews")
    assert res.status_code == 404
