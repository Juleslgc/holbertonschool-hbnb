#!/usr/bin/python3


import pytest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review

def test_place_creation():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)

    # Adding a review
    review = Review(text="Great stay!", rating=5, place=place, user=owner)
    place.add_review(review)

    assert place.title == "Cozy Apartment"
    assert place.price == 104.56
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"
    print("Place creation and relationship test passed!")

def test_title_creation_invalid():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    with pytest.raises(ValueError):
        Place(title="", description="A nice place to stay", price=104.56, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    print("Title is Empty")

def test_price_positive_number_invalid():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    with pytest.raises(ValueError):
        Place(title="Title", description="A nice place to stay", price=0.0, latitude=37.7749, longitude=-122.4194, owner_id=owner.id)
    print("Price must be a positive number")
    
def test_latitude_number_invalid():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    with pytest.raises(ValueError):
        Place(title="Title", description="A nice place to stay", price=145.45, latitude= -91.0, longitude=-122.4194, owner_id=owner.id)
    print("Latitude must be between -90.0 and 90.0")

def test_longitude_number_invalid():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="passwordofworld")
    with pytest.raises(ValueError):
        Place(title="Title", description="A nice place to stay", price=145.45, latitude=37.7749, longitude= 200.0, owner_id=owner.id)
    print("Longitude must be between -180.0 and 180.0")

def test_invalid_owner_id():
    with pytest.raises(ValueError):
       Place(title="Title", description="Description", price=100.0, latitude=30.0, longitude=30.0, owner_id="no_uuid")
    print("Invalid UUID format test passed")