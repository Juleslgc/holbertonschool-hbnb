#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from app.models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent a review by user for place.
    """
    def __init__(self, place_id, user_id, text, rating):
        """
        Initialize a new review instance.
        """
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.rating = rating

        if not isinstance(text, str) or not text:
            raise ValueError("Review text must be a not-empty string")
        
        if not isinstance(rating, int):
            raise TypeError("Rating must be a number")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")


        if not isinstance(user_id, str) or not user_id:
            raise ValueError("User ID must be a not-empty string")

        if not isinstance(place_id, str) or not place_id:
            raise ValueError("Place ID must be a non-empty string")
        
    def to_dict(self):
        """
        Return a dictionary representation of the review.
        """
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id
        }