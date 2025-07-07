#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place



class Review(BaseModel):
    """
    Represent a review by user for place.
    """
<<<<<<< HEAD
    def __init__(self, place, user, text, rating):
=======
    def __init__(self, place_id, user_id, text, rating):
>>>>>>> main
        """
        Initialize a new review instance.
        """
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

<<<<<<< HEAD

    @property
    def place(self):
        """
        Get the place associated with the review. 
        """
        return self.__place


    @place.setter
    def place(self, value):
        """
        Set the place associated with the review.
        """
        if not isinstance(value, Place):
            raise TypeError("place must be an instance of Place")
        self.__place = value


    @property
    def user(self):
        """
        Get the user origin write the review.
        """
        return self.__user


    @user.setter
    def user(self, value):
        """
        Set the user origin write the review.
        """
        if not isinstance(value, User):
            raise TypeError("user must be an instance of User")
        self.__user = value


=======
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
        
>>>>>>> main
    def to_dict(self):
        """
        Return a dictionary representation of the review.
        """
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
        """
        Return a string representation of the review.
        """
        return f"[Review] {self.id} - Rating: {self.rating}, Text: {self.text[:30]}..."
