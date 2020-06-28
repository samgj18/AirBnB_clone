#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
	def __init__(self, *args, **kwargs):
		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at':
					self.created_at = datetime.strptime(
						value, "%Y-%m-%dT%H:%M:%S.%f")
				if key == 'updated_at':
					self.updated_at = datetime.strptime(
						value, "%Y-%m-%dT%H:%M:%S.%f")
				if key != '__class__':
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now().isoformat()
			self.updated_at = datetime.now().isoformat()

	def __str__(self):
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		self.updated_at = str(datetime.now().isoformat())

	def to_dict(self):
		dic = self.__dict__
		dic["__class__"] = self.__class__.__name__
		return dic
