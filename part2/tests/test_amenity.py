#!/usr/bin/python3
"""
This is a module for interpreting python3
"""
<<<<<<<< HEAD:part2/tests/test_amenity.py

========
>>>>>>>> main:part2/tests/test_model_amenity.py

from app.models.amenity import Amenity

def test_amenity_creation():
    """
<<<<<<<< HEAD:part2/tests/test_amenity.py
    This is a test for create amenity with name and description.
    """
    amenity = Amenity(name="Wi-Fi", description="This is a description")
========
    Required for crate Amenity
    """
    amenity = Amenity(name="Wi-Fi")
>>>>>>>> main:part2/tests/test_model_amenity.py
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")

test_amenity_creation()