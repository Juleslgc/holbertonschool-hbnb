#!/usr/bin/python3


from app.models.base_model import BaseModel
from app.models.place import Place





class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
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
        return f"first_name: {self.first_name}\n last_name: {self.last_name}\n email: {self.email}"

    def add_place(self, place):
        """
        Add a place to the user
        """
        self.places.append(place)
