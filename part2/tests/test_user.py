#!/usr/bin/python3


from app.models.user import User
import pytest

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    assert user.places == []
    print("User creation test passed!")

def test_user_creation_invalid_first_name():
    with pytest.raises(ValueError):
        User(first_name="", last_name="Doe", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_first_name passed")

def test_user_creation_invalid_last_name():
    with pytest.raises(ValueError):
        User(first_name="John", last_name="", email="john.doe@example.com", password="passwordoftheworld")
    print("test_user_creation_invalid_last_name passed")

def test_user_creation_invalid_email():
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="", password="passwordoftheworld")
    print("test user_creation_invalid_email passed")

def test_user_invalid_input_mail():
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="vililili.com", password="passwordoftheworld")
    print("test_user_invalid_input_mail passed")
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="vililili@com", password="passwordoftheworld")
    print("test_user_invalid_input_mail passed")
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="vilililicom", password="passwordoftheworld")
    print("test_user_invalid_input_mail passed")
