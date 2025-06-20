from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review




class HBnBFacade:
    """
    Facade class for simplified interface for managing users,
    places, reviews and amenities.
    """
    def __init__(self):
        """
        Initialize the facade with in-memory repositories for users,
        places, reviews and amenities.
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    # User
    # Placeholder method for creating a user
    def create_user(self, user_data):
        """
        Create a new user and add to the user repository.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user


    def get_user(self, user_id):
        """
        Get user.
        """
        return self.user_repo.get(user_id)


    def get_user_by_email(self, email):
        """
        Get user by Email adress.
        """
        return self.user_repo.get_by_attribute('email', email)


    def get_user_by_id(self, id):
        """
        Get user by ID.
        """
        return self.user_repo.get_by_attribute('id', id)


    def get_all_users(self):
        """
        Get all users from repository.
        """
        users = self.user_repo.get_all()
        return [user.to_dict() for user in users]
    

    def update(self, user_id, data):
        """
        Update a users information.
        """
        user = self.user_repo.update(user_id, data)
        return self.user_repo.get(user_id)


    # Amenity
    def create_amenity(self, amenity_data):
        """
        Creates and adds a new amenity from data.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity


    def get_amenity(self, amenity_id):
        """
        Returns an amenity by its ID.
        """
        return self.amenity_repo.get(amenity_id)


    def get_all_amenities(self):
        """
        Returns all amenities as dictionaries.
        """
        amenities = self.amenity_repo.get_all()
        return [amenity.to_dict() for amenity in amenities]
    

    def get_amenity_by_id(self, id):
        """
        Returns an amenity by its ID using attribute search.
        """
        return self.amenity_repo.get_by_attribute('id', id)


    def update_amenity(self, amenity_id, amenity_data):
        """
        Updates an amenity and returns the updated amenity.
        """
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)
    

    # Place
    def create_place(self, place_data):
        """
        Creates and adds a new place from data
        """
        place = Place(**place_data)
        self.place_repo.add(place)
        return place


    def get_place(self, place_id):
        """
        Returns a place by its ID.
        """
        return self.place_repo.get(place_id)


    def get_all_places(self):
        """
        Returns all places as dictionaries.
        """
        places = self.place_repo.get_all()
        return [place.to_dict() for place in places]


    def get_user_by_id(self, id):
        """
        Returns a user by ID from the place repository.
        """
        return self.place_repo.get_by_attribute('id', id)


    def update_place(self, place_id, place_data):
        """
        Updates a place and returns the updated place.
        """
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)
    

    # Review
    def create_review(self, review_data):
        """
        Creates and adds a new review from data.
        """
        review = Review(**review_data)
        self.review_repo.add(review)
        return review


    def get_review(self, review_id):
        """
        Returns a review by its ID.
        """
        return self.review_repo.get(review_id)


    def get_all_reviews(self):
        """
        Returns all reviews as dictionaries.
        """
        reviews = self.review_repo.get_all()
        return [review.to_dict() for review in reviews]


    def get_reviews_by_place(self, place_id):
        """
        Returns all reviews for a specific place.
        """
        place = self.place_repo.get(place_id)
        if place:
            return place.reviews


    def update_review(self, review_id, review_data):
        """
        Updates a review and returns the updated review.
        """
        place = self.review_repo.update(review_id, review_data)
        return self.review_repo.get(review_id)


    def delete_review(self, review_id):
        """
        Deletes a review by its ID.
        """
        return self.review_repo.delete(review_id)
     
facade = HBnBFacade()