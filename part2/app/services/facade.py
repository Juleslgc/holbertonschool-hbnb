from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    """
<<<<<<< HEAD
    Central facade for managing users, places,
    amenities and reviews.
    """
    def __init__(self):
        """
        Initialize the facade with in-memory repositories for all models.
=======
    Facade class for simplified interface for managing users,
    places, reviews and amenities.
    """
    def __init__(self):
        """
        Initialize the facade with in-memory repositories for users,
        places, reviews and amenities.
>>>>>>> main
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


<<<<<<< HEAD
    def create_user(self, user_data):
        """
        Create a new user.
=======
    # User
    # Placeholder method for creating a user
    def create_user(self, user_data):
        """
        Create a new user and add to the user repository.
>>>>>>> main
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user


    def get_user(self, user_id):
        """
<<<<<<< HEAD
        Get a user by ID.
        """
        return self.user_repo.get(user_id)
    

    def get_user_by_email(self, email):
        """
        Get a user by email address.
        """
        return self.user_repo.get_by_attribute('email', email)
    

    def get_user_by_id(self, id):
        """
        Get a user by ID.
=======
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
>>>>>>> main
        """
        return self.user_repo.get_by_attribute('id', id)


    def get_all_users(self):
        """
<<<<<<< HEAD
        Get a list of all user
=======
        Get all users from repository.
>>>>>>> main
        """
        users = self.user_repo.get_all()
        return [user.to_dict() for user in users]


    def update(self, user_id, data):
        """
<<<<<<< HEAD
        Update a user information.
        """
        self.user_repo.update(user_id, data)
        return self.user_repo.get(user_id)


    def create_amenity(self, amenity_data):
        """
        Create a new Amenity.
=======
        Update a users information.
        """
        user = self.user_repo.update(user_id, data)
        return self.user_repo.get(user_id)


    # Amenity
    def create_amenity(self, amenity_data):
        """
        Creates and adds a new amenity from data.
>>>>>>> main
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity


    def get_amenity(self, amenity_id):
        """
<<<<<<< HEAD
        Get amenity by  ID.
=======
        Returns an amenity by its ID.
>>>>>>> main
        """
        return self.amenity_repo.get(amenity_id)


    def get_all_amenities(self):
        """
<<<<<<< HEAD
        Get a list of all amenities.
=======
        Returns all amenities as dictionaries.
>>>>>>> main
        """
        amenities = self.amenity_repo.get_all()
        return [amenity.to_dict() for amenity in amenities]
    

    def get_amenity_by_id(self, id):
        """
<<<<<<< HEAD
        Get amenity by ID.
=======
        Returns an amenity by its ID using attribute search.
>>>>>>> main
        """
        return self.amenity_repo.get_by_attribute('id', id)


    def update_amenity(self, amenity_id, amenity_data):
        """
<<<<<<< HEAD
        Update amenity information.
=======
        Updates an amenity and returns the updated amenity.
>>>>>>> main
        """
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)
    

<<<<<<< HEAD
    def create_place(self, place_data):
        """
        Create a new place.
=======
    # Place
    def create_place(self, place_data):
        """
        Creates and adds a new place from data
>>>>>>> main
        """
        place = Place(**place_data)
        self.place_repo.add(place)
        return place


    def get_place(self, place_id):
        """
<<<<<<< HEAD
        Get place by ID.
=======
        Returns a place by its ID.
>>>>>>> main
        """
        return self.place_repo.get(place_id)


    def get_all_places(self):
        """
<<<<<<< HEAD
        Get a list of all places.
        """
        places = self.place_repo.get_all()
        return [place.to_dict() for place in places]
    
=======
        Returns all places as dictionaries.
        """
        places = self.place_repo.get_all()
        return [place.to_dict() for place in places]


    def get_user_by_id(self, id):
        """
        Returns a user by ID from the place repository.
        """
        return self.place_repo.get_by_attribute('id', id)
>>>>>>> main


    def update_place(self, place_id, place_data):
        """
<<<<<<< HEAD
        Update a place information.
        """
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)


    def create_review(self, review_data):
        """
        Create a new review.
=======
        Updates a place and returns the updated place.
        """
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)
    

    # Review
    def create_review(self, review_data):
        """
        Creates and adds a new review from data.
>>>>>>> main
        """
        review = Review(**review_data)
        self.review_repo.add(review)
        return review


    def get_review(self, review_id):
        """
<<<<<<< HEAD
        Get a review by ID.
=======
        Returns a review by its ID.
>>>>>>> main
        """
        return self.review_repo.get(review_id)


    def get_all_reviews(self):
        """
<<<<<<< HEAD
        Get a list of all reviews.
=======
        Returns all reviews as dictionaries.
>>>>>>> main
        """
        reviews = self.review_repo.get_all()
        return [review.to_dict() for review in reviews]


    def get_reviews_by_place(self, place_id):
        """
<<<<<<< HEAD
        Get all reviews for a specific place.
=======
        Returns all reviews for a specific place.
>>>>>>> main
        """
        place = self.place_repo.get(place_id)
        if place:
            return place.reviews


    def update_review(self, review_id, review_data):
        """
<<<<<<< HEAD
        Update a reviews information.
        """
        self.review_repo.update(review_id, review_data)
=======
        Updates a review and returns the updated review.
        """
        place = self.review_repo.update(review_id, review_data)
>>>>>>> main
        return self.review_repo.get(review_id)


    def delete_review(self, review_id):
        """
<<<<<<< HEAD
        Delete a review by its ID.
=======
        Deletes a review by its ID.
>>>>>>> main
        """
        return self.review_repo.delete(review_id)


facade = HBnBFacade()
