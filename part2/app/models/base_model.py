#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
