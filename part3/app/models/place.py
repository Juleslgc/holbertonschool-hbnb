from .baseclass import BaseModel
from .user import User
from app import db
from sqlalchemy.orm import validates
from .amenity import Amenity

# Association table for many-to-many relationship
amenity_place = db.Table('amenity_place',
                         db.Column('amenity_id', db.String(40), db.ForeignKey('amenities.id'), primary_key=True),
                         db.Column('place_id', db.String(40), db.ForeignKey('places.id'), primary_key=True)
                        )

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(40), db.ForeignKey('users.id'), nullable=False)
    amenities = db.relationship('Amenity', secondary=amenity_place, lazy='subquery',
                                backref=db.backref('places', lazy=True))

    
    @validates('title')
    def validate_title(self, key, value):
        if not value or value.strip() == "":
            raise ValueError("Title cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        super().is_max_length('title', value, 100)
        return value
    
    @validates('description')
    def validate_description(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        return value
    
    @validates('price')
    def validate_price(self, key, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be positive.")
        if not value:
            raise ValueError("Price must not be empty")
        return value
    
    @validates('latitude')
    def validate_latitude(self, key, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")
        if not value:
            raise ValueError("Latitude must not be empty")
        super().is_between("latitude", value, -90, 90)
        return value
    
    @validates('longitude')
    def validate_longitude(self, key, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")
        if not value:
            raise ValueError("Longitude must not be empty")
        super().is_between("longitude", value, -180, 180)
        return value
    
    @validates('owner')
    def validate_owner(self, key, value):
        if not isinstance(value, User):
            raise TypeError("Owner must be a user instance")
        if not value:
            raise ValueError("Owner must not be empty")
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
    
    def delete_review(self, review):
        """Remove a review from the place."""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id
        }
    
    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict(),
            'amenities': [{'id': a.id, 'name': a.name} for a in self.amenities],
            'reviews': [review.to_dict() for review in self.reviews]
        }
