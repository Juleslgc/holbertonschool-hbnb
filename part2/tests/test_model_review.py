#!/usr/bin/python3
"""
This is a module for interpreting python3
"""

import pytest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review



def test_review_creation_valid():
    """
    This is a test for create a validate review.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    review = Review(place_id=place.id, user_id=user.id, text='text', rating=5)
    assert review.place_id == place.id
    assert review.user_id == user.id
    assert review.text == "text"
    assert review.rating == 5
    print("Review creation valid test passed")


def test_review_text_invalid():
    """
    This is a test for verify if review is empty or not (text required).
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    with pytest.raises(ValueError):
        Review(place_id=place.id, user_id=user.id, text='', rating=5)
    print("Review creation text invalid passed")


def test_rating_invalid():
    """
    This is a test for wrong rating (only rate between 1 and 5).
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    with pytest.raises(ValueError):
        Review(place_id=place.id, user_id=user.id, text='text', rating=6)
    with pytest.raises(ValueError):
        Review(place_id=place.id, user_id=user.id, text='text', rating=0)
    print("Review rating must be between 1 and 5")


def test_review_invalid_user():
    """
    This is a test for invalid review (user required).
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    with pytest.raises(ValueError):
        Review(place_id=place.id, user_id="", text='text', rating=5)
    print("Invalid User test passed")


def test_review_invalid_place():
    """
    This is a test for invalid place (place required).
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    with pytest.raises(ValueError):
        Review(place_id="", user_id=user.id, text='text', rating=5)
    print("Invalid Place test passed")
