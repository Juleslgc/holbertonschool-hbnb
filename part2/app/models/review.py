#!/usr/bin/python3


from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, place_id, user_id, text, rating):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.rating = rating

        if not isinstance(text, str):
            raise TypeError("Reviews contain is mandatory")
        
        if not isinstance(rating, int):
            raise TypeError("Rating must be a integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating between 1 and 5")


        if not isinstance(user_id, str):
            raise TypeError("User is a user instance")

        if not isinstance(place_id, str):
            raise TypeError("Place is a place instance")
        
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id
        }