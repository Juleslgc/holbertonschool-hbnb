#!/usr/bin/python3


from models.base_model import BaseModel
from models.user import User
from models.place import Place

class Review(BaseModel):
    def __init__(self, place, user, comment, rating):
        super().__init__()
        self.place = place
        self.user = user
        self.comment = comment
        self.rating = rating

        if not isinstance(comment, str):
            raise TypeError("Reviews contain is mandatory")
        
        if not isinstance(rating, int):
            raise TypeError("Rating must be a integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating between 1 and 5")


        if not isinstance(user, User):
            raise TypeError("User is a user instance")

        if not isinstance(place, Place):
            raise TypeError("Place is a place instance")
