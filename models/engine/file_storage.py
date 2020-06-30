#!/usr/bin/python3
"""
This module contains code related to file storage
for the airbnb clone project. A json data format
for serialization and deserialization of data.
"""
import json
import models
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = dict()

    def all(self) -> object:
        """
        Returns the dictionary __objects
        :return: The dictionary __objects
        """
        return self.__objects

    def new(self, obj: object) -> None:
        """
        Sets in __objects the obj with key <obj class name>.id
        :param obj: object to be settled
        """
        if obj:
            self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self) -> None:
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='UTF-8') as a_file:
            json.dump(dictionary, a_file)

    def reload(self) -> None:
        """
        Deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesnt exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding='UTF-8') as a_file:
                objects = json.load(a_file)
            for key, value in objects.items():
                self.__objects[key] = models.classes[value["__class__"]](
                    **value)
        except FileNotFoundError:
            pass
