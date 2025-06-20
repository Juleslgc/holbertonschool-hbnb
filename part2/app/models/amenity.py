#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is a amenity class inheritance Base model.
    """
    def __init__(self, name):
        super().__init__()
        if not isinstance(name, str) or name == "":
            raise TypeError("Name must be a string and not empty")
        if len(name) > 50:
            raise ValueError("Name must be at most 50 characters ")
        self.name = name


    def to_dict(self):
        """
        This a method for return  a dictionary representation
        of the amenity instance.
        """
        return {
            'id': self.id,
            'name': self.name
        }