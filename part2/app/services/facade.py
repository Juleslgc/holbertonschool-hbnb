from app.persistence.repository import InMemoryRepository
from app.models.user import User


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all_users()
    
    def update(self, user_id, data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        return self.user_repo.update(user_id, data)
 
    def to_dict(self, id, first_name, last_name, email):
        return {
            'id': id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
            }, 200

facade = HBnBFacade()
