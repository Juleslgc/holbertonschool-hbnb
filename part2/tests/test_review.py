#!/usr/bin/python3

import pytest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review


def test_review_creation_valid():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    review = Review(place=place, user=user, text='text', rating=5)

    assert review.place == place
    assert review.user == user
    assert review.text == "text"
    assert review.rating == 5
    print("Review creation valid test passed")


def test_review_text_invalid():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)

    with pytest.raises(ValueError):
        review = Review(place=place, user=user, text='', rating=5)
    print("Review creation text invalid passed")


def test_rating_invalid():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)

    with pytest.raises(ValueError):
        review = Review(place=place, user=user, text='text', rating=6)
    with pytest.raises(ValueError):
        review = Review(place=place, user=user, text='text', rating=0)
    print("Review rating must be between 1 and 5")


def test_review_invalid_user():
    with pytest.raises(TypeError):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
        place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)

        review = Review(place=place, user=None, text='text', rating=5)
    print("Invalid User test passed")


def test_review_invalid_place():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)

    with pytest.raises(TypeError):
        review = Review(place=None, user=user, text='text', rating=5)
    print("Invalid Place test passed")
