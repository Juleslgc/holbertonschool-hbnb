#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from app.models.base_model import BaseModel
from app.models.place import Place
import re



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
        self.__password = password
        self.is_admin = is_admin
        self.places = []

        if not isinstance(first_name, str):
            raise TypeError("First name must be a non-empty string and at most 50 characters")
        if len(first_name) > 50 or first_name == "":
            raise ValueError("First name is required must be characters")
        

        if not isinstance(last_name, str):
            raise TypeError("Last name must be a non-empty string and at most 50 characters")
        if len(last_name) > 50 or last_name == "":
            raise ValueError("Last name is required must be characters")

        
        if not isinstance(is_admin, bool):
            raise TypeError("Is_admin must be boolean type")
    
    @property
    def email(self):
        """
        Returns the user's email address.
        """
        return self.__email
    
    @email.setter
    def email(self, new_email):
        """
        Sets a new, validated email address for the user.
        """
        if not isinstance(new_email, str):
            raise TypeError("email must be strings")
        self.__email = self.verified_email(new_email)
    
    @property
    def password(self):
        """
        Returns the user's password.
        """
        return self.__password
    
    @password.setter
    def password(self, new_password):
        """
        Sets a new password for the user.
        """
        self.__password = new_password

    def __str__(self):
        """
        Return the  string representation of user.
        """
        return f"first_name: {self.first_name}\n last_name: {self.last_name}\n email: {self.email}"

    def add_place(self, place):
        """
        Add a place to the user
        """
        self.places.append(place)

    def delete_place(self, place):
        """
        Removes a place from the list.
        """
        self.places.remove(place)

    def to_dict(self):
        """
        Return a dictionary representation of the user.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
            }
    
    @staticmethod
    def verified_email(email):
        """
        Validate email format with allowed extensions.
        """
        extensions = ['com', 'fr', 'net', 'org']
        pattern = r'^[^@\s]+@[^@\s]+\.(%s)$' % '|'.join(extensions)
        
        if not re.match(pattern, email, re.IGNORECASE):
            raise ValueError("Email must be a valid email address")
        return email
