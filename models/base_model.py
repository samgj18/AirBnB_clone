#!/usr/bin/python3
import uuid
from datetime import datetime, date


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime
        self.updated_at = datetime

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime
