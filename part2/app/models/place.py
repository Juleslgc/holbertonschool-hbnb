import uuid
from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner_id, description=""):
        super().__init__()
        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.__owner_id = owner_id
        self.reviews = []
        self.amenities = []

        if not isinstance(self.title, str):
            raise TypeError("Title must be a string")
        if self.title == "" or len(self.title) > 100:
            raise ValueError("Title is required and must be at most 100 characters")
        if not isinstance(self.description, str):
            raise TypeError("Description must be a string")
        if not isinstance(self.price, float):
            raise TypeError("Price must be a float number")
        if self.price < 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(self.latitude, float):
            raise TypeError("Latitude must be a float")
        if self.latitude < -90.0 or self.latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        if not isinstance(self.longitude, float):
            raise TypeError("Longitude must be a float")
        if self.longitude < -180.0 or self.longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")

        if not isinstance(owner_id, str):
            raise TypeError("Owner ID must be a string UUID")
        try:
            uuid.UUID(owner_id)
        except ValueError:
            raise ValueError("Invalid UUID format for owner_id")

        self.__owner_id = owner_id

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, new_owner_id):
        try:
            uuid.UUID(new_owner_id)
        except ValueError:
            raise ValueError("Invalid UUID format for owner_id")
        self.__owner_id = new_owner_id
