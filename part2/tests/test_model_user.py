#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from app.models.user import User
import pytest


def test_user_creation():
    """
    This is a test for validate user creation.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    assert user.places == []
    print("User creation test passed!")


def test_user_creation_invalid_first_name():
    """
    This is a test for create a valid user (first name is mandatory).
    """
    with pytest.raises(ValueError):
        User(first_name="", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_first_name passed")

    with pytest.raises(TypeError):
        User(first_name=1, last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_first_name passed")

    with pytest.raises(ValueError):
        User(first_name="kjfuehjenfjfhebnedljrnendkhjrnzkfbrnhjdhenekkchebnrljfnrndejbbfdbrkdedndnjhdhssjkdhdbhnzsjsjnfjrnrncndbk", last_name= "Doe", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_first_name passed")

    

def test_user_creation_invalid_last_name():
    """
    This is a test for create a valid user (last_name is required).
    """
    with pytest.raises(ValueError):
        User(first_name="John", last_name="", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_last_name passed")

    with pytest.raises(TypeError):
        User(first_name="John", last_name= 2, email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_first_name passed")

    with pytest.raises(ValueError):
        User(first_name="John", last_name= "kjfuehjenfjfhebnedljrnendkhjrnzkfbrnhjdhenekkchebnrljfnrndejbbfdbrkdedndnjhdhssjkdhdbhnzsjsjnfjrnrncndbk", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_first_name passed")


def test_user_creation_invalid_email():
    """
    This is a test for created user by validate email (not empty email).
    """
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="", password="passwordoftheworld")
    print("test user_creation_invalid_email passed")
    with pytest.raises(TypeError):
        User(first_name="John", last_name="Doe", email=1345, password="passwordoftheworld")


def test_user_invalid_input_mail():
    """
    This is a test for standard email format.
    """
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="vililili.com", password="passwordoftheworld")
    print("test_user_invalid_input_mail passed")
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="vililili@com", password="passwordoftheworld")
    print("test_user_invalid_input_mail passed")
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="vilililicom", password="passwordoftheworld")
    print("test_user_invalid_input_mail passed")

    