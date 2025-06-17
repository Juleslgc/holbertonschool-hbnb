#!/usr/bin/python3


from models.base_model import BaseModel
from models.user import User
from models.place import Place

class Review(BaseModel):
    def __init__(self, place_id, user_id, text, rating):
        super().__init__()
        self.__place = place_id
        self.__user_id = user_id
        self.text = text
        self.rating = rating

        if not isinstance(text, str):
            raise TypeError("Reviews contain is mandatory")
        
        if not isinstance(rating, int):
            raise TypeError("Rating must be a integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating between 1 and 5")


        if not isinstance(user_id, User):
            raise TypeError("User is a user instance")

        if not isinstance(place_id, Place):
            raise TypeError("Place is a place instance")

    @property
    def place_id(self):
         return self.__place

    @place_id.setter
    def place_id(self, new_place):
         if not isinstance(new_place, Place):
            raise TypeError("Place is a place instance")
         self.__place = new_place

    @property
    def user_id(self):
         return self.__user_id

    @user_id.setter
    def user_id(self, new_user_id):
        if not isinstance(new_user_id, User):
            raise TypeError("User is a user instance")
        self.__user_id = new_user_id
