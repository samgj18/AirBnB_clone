#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = str(datetime.now())

    def to_dict(self):
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        return dic
