from .basemodel import BaseModel
from .place import Place
from .user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        self.__text = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer")
        super().is_between('Rating', value, 1, 6)
        self.__rating = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise TypeError("Place must be a Place instance")
        self.__place = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("User must be a User instance")
        self.__user = value

    def to_dict(self, detail=False):
        """
        Retourne un dict pour l'API.
        - Si detail=True, inclut tous les détails du user et du lieu.
        - Sinon, ne met que les IDs (plus simple pour les endpoints).
        """
        base = {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
        }
        if detail:
            base['place'] = self.place.to_dict() if self.place else None
            base['user'] = self.user.to_dict() if self.user else None
        else:
            base['place_id'] = self.place.id if self.place else None
            base['user_id'] = self.user.id if self.user else None
        return base
