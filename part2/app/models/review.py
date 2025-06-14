#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, place, user, comment, rating):
        super().__init__()
        self.place = place
        self.user = user
        self.comment = comment
        self.rating = rating