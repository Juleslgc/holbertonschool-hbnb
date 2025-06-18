#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from app.models.base_model import BaseModel
from app.models.place import Place



class User(BaseModel):
    """
    Represents a user with information and connect places.
    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initialize a new instance user.
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []


        if not isinstance(first_name, str):
            raise TypeError("First name is required")
        if len(first_name) > 50 or first_name == "":
            raise ValueError("First name is required must be characters")


        if not isinstance(last_name, str):
            raise TypeError("Last name is required")
        if len(last_name) > 50 or last_name == "":
            raise ValueError("Last name is required must be characters")

        if not isinstance(email, str):
            raise TypeError("email must be strings")
        if email == "" or "@" not in email or "." not in email:
            raise ValueError("email must be not empty and contain '@' and '.' ")

        if not isinstance(is_admin, bool):
            raise TypeError("Is_admin must be boolean type")
    

    def __str__(self):
        """
        Return the  string representation of user.
        """
        return f"first_name: {self.first_name}\n last_name: {self.last_name}\n email: {self.email}"


    def add_place(self, place):
        """
        Add a place to the user.
        """
        if not isinstance(place, Place):
            raise TypeError("place must be an instance of Place")
        self.places.append(place)


    def to_dict(self):
        """
        Return a dictionary representation of the user.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            }
