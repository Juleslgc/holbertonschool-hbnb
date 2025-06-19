#!/usr/bin/python3


from app.models.amenity import Amenity

def test_amenity_creation():
    """
    Required for crate Amenity
    """
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")

test_amenity_creation()