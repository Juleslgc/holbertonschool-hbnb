from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.amenity_repository import AmenityRepository
from app.services.repositories.review_repository import ReviewRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app import db

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.amenity_repo = AmenityRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()

    # USER
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_users(self):
        return [user.to_dict() for user in self.user_repo.get_all()]

    def get_user(self, user_id, as_dict=True):
        user = self.user_repo.get(user_id)
        if as_dict:
            return user.to_dict() if user else None
        return user

    def get_user_by_email(self, email, as_dict=False):
        user = self.user_repo.get_by_attribute('email', email)
        if as_dict:
            return user.to_dict() if user else None
        return user
    
    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)

    # AMENITY
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity.to_dict()

    def get_amenity(self, amenity_id, as_dict=True):
        amenity = self.amenity_repo.get(amenity_id)
        if as_dict:
            return amenity.to_dict() if amenity else None
        return amenity

    def get_all_amenities(self):
        return [amenity.to_dict() for amenity in self.amenity_repo.get_all()]

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)

    # PLACE
    def create_place(self, place_data):
        user = self.user_repo.get_by_attribute('id', place_data['owner_id'])
        if not user:
            raise KeyError('Invalid input data')
        del place_data['owner_id']
        amenities = place_data.pop('amenities', [])
        amenities_objs = []
        for a in amenities:
            amenity = self.amenity_repo.get(a['id'] if isinstance(a, dict) else a)
            if not amenity:
                raise KeyError('Invalid input data')
            amenities_objs.append(amenity)
        place_data['owner'] = user
        amenities = place_data.pop('amenities', None)
        place = Place(**place_data)
        if amenities:
            for a in amenities:
                amenity = self.get_amenity(a['id'])
                if not amenity:
                    raise KeyError('Invalid input data')
                place.amenities.append(amenity)
        self.place_repo.add(place)
        user.add_place(place)
        db.session.commit()
        return place
    
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return [place.to_dict() for place in self.place_repo.get_all()]

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)

    def add_amenities_to_place(self, place_id, amenities_data):
        place = self.place_repo.get(place_id)
        if not place:
            raise KeyError("Place not found")
        for amenity_dict in amenities_data:
            amenity = self.amenity_repo.get(amenity_dict['id'])
            if not amenity:
                raise KeyError(f"Amenity {amenity_dict['id']} not found")
            if amenity not in place.amenities:
                place.add_amenity(amenity)
        return place.to_dict()
    
    def get_review_by_user_and_place(self, user_id, place_id, as_dict=True):
        for review in self.review_repo.get_all():
            if review.user.id == user_id and review.place.id == place_id:
                return review.to_dict() if as_dict else review
        return None

    # REVIEWS
    def create_review(self, review_data):
        user = self.user_repo.get(review_data['user_id'])
        if not user:
            raise KeyError('Invalid input data')
        del review_data['user_id']
        review_data['user'] = user

        place = self.place_repo.get(review_data['place_id'])
        if not place:
            raise KeyError('Invalid input data')
        del review_data['place_id']
        review_data['place'] = place

        review = Review(**review_data)
        review.user = user
        review.place = place
        self.review_repo.add(review)
        user.add_review(review)
        place.add_review(review)
        return review.to_dict()

    def get_review(self, review_id, as_dict=True):
        review = self.review_repo.get(review_id)
        if as_dict:
            return review.to_dict() if review else None
        return review

    def get_all_reviews(self):
        return [review.to_dict() for review in self.review_repo.get_all()]

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise KeyError('Place not found')
        return [review.to_dict() for review in place.reviews]

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise KeyError("Review not found")
        db.session.delete(review)
        db.session.commit()
