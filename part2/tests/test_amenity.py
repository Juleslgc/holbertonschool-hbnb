#!/usr/bin/python3


from app.models.amenity import Amenity

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi", description="This is a description")
    assert amenity.name == "Wi-Fi"
    assert amenity.description == "This is a description"
    print("Amenity creation test passed!")

test_amenity_creation()