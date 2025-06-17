#!/usr/bin/python3


from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name, description=""):
        super().__init__()
        self.name = name
        self.description = description

        
        if not isinstance(name, str) or name == "":
            raise TypeError("Name must be a string and not empty")
        if len(name) > 50:
            raise ValueError("Name must be at most 50 characters ")

        if not isinstance(description, str):
            raise TypeError("Description must be a string")
