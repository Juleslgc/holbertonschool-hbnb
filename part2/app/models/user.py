#!/usr/bin/python3


from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

        if not isinstance(first_name, str):
            raise TypeError("First name is required")
        if len(first_name) > 50 or first_name == "":
            raise ValueError("First name is required must be characters")
        

        if not isinstance(last_name, str):
            raise TypeError("Last name is required")
        if len(last_name) > 50 or last_name == "":
            raise ValueError("Last name is required must be characters")

        if  not isinstance(password, str):
            raise TypeError("Password required")
        if password == "":
            raise ValueError("Password is not empty")

        if not isinstance(is_admin, bool):
            raise TypeError("Is_admin must be boolean type")
    

    def __str__(self):
        return f"first_name: {self.first_name}\n last_name: {self.last_name}\n email: {self.email}"
