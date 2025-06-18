from app.persistence.repository import InMemoryRepository
from models.user import User




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

    # Placeholder method for creating a user
    def create_user(self, user_data):
        """
        Create a new user and add to the user repository.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        """
        Get place by ID.
        """
        # Logic will be implemented in later tasks
        pass

    def get_user(self, user_id):
        """
        Get user by ID.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Get user by email address.
        """
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """
        Get all users from repository.
        """
        return self.user_repo.get_all()


    def update(self, user_id, data):
        """
        Update a users information.
        """
        user = self.user_repo.get(user_id)
        if not user:
            return None
        return self.user_repo.update(user_id, data)

    def to_dict(self, id, first_name, last_name, email):
        """
        Return a dictionary representation of a user.
        """
        return {
            'id': id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
            }, 200

facade = HBnBFacade()
