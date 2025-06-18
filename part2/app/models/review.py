#!/usr/bin/python3

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, place, user, text, rating):
        super().__init__()

        if not isinstance(place, Place):
            raise TypeError("place must be an instance of Place")
        if not isinstance(user, User):
            raise TypeError("user must be an instance of User")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be a non-empty string")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("rating must be an integer between 1 and 5")

        self.__place = place
        self.__user = user
        self.text = text
        self.rating = rating

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise TypeError("place must be an instance of Place")
        self.__place = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("user must be an instance of User")
        self.__user = value

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.__user.id,
            'place_id': self.__place.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __str__(self):
        return f"[Review] {self.id} - Rating: {self.rating}, Text: {self.text[:30]}..."
