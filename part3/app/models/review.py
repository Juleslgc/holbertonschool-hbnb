from .baseclass import BaseModel
from .place import Place
from .user import User
from app import db
from sqlalchemy.orm import validates

class Review(BaseModel):

	__tablename__ = 'reviews'

	text = db.Column(db.String(100), nullable=False)
	rating = db.Column(db.Integer, nullable=False)
	place_id = db.Column(db.String(40), db.ForeignKey('places.id'), nullable=False)
	place = db.relationship('Place', backref='reviews', lazy=True)
	user_id = db.Column(db.String(40), db.ForeignKey('users.id'), nullable=False)

	@validates('text')
	def validate_text(self, key, value):
		if not value or value.strip() == "":
			raise ValueError("Text cannot be empty")
		if not isinstance(value, str):
			raise TypeError("Text must be a string")
		return value
	
	@validates('rating')
	def validate_rating(self, key, value):
		if not isinstance(value, int):
			raise TypeError("Rating must be an integer")
		if not value:
			raise ValueError("Rating must not be empty")
		super().is_between('Rating', value, 1, 6)
		return value
	
	@validates('place')
	def validate_place(self, key, value):
		if not isinstance(value, Place):
			raise TypeError("Place must be a place instance")
		if not value:
			raise ValueError("Place must not be empty")
		return value
	
	@validates('user')
	def validate_user(self, key, value):
		if not isinstance(value, User):
			raise TypeError("User must be a user instance")
		if not value:
			raise ValueError("User must not be empty")
		return value

	def to_dict(self):
		return {
			'id': self.id,
			'text': self.text,
			'rating': self.rating,
			'place_id': self.place.id,
			'user_id': self.user.id
		}
