#!/usr/bin/python3


from models.base_model import BaseModel
from models.user import User


class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, description=""):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if title == "" or len(title) > 100:
            raise ValueError("Title is required and must be at 100 most characters")

        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        
        if not isinstance(price, float):
            raise TypeError("Price must be a float number")
        if price < 0:
            raise ValueError("Price must be a positive number")
        
        if not isinstance(latitude, float):
            raise TypeError("Latitude must be a float")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")

        if not isinstance(longitude, float):
            raise TypeError("Longitude must be a float")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")


        if  not isinstance(owner, User):
            raise TypeError("Owner is an instance of User")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)