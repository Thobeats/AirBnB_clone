#!/usr/bin/python3
"""File storage class the serializes instances to JSON FIlE
and deserializes JSON FILE to instances
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class the serializes instances and deserializes JSON FIle
    """

    def __init__(self):
        """
        initializes the FileStorage Class
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        stores a new obj in the objects dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes the objects into the file
        """
        dictionaryContainer = {}
        for key, values in self.__objects.items():
            dictionaryContainer[key] = values.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(dictionaryContainer, fp)

    def reload(self):
        """
        deserializes the file into objects
        """
        try:
            with open(self.__file_path, 'r') as fp:
                allDicts = json.loads(fp.read())

            self.__objects = {}
            for id, dict in allDicts.items():
                cls = BaseModel(**dict)
                self.__objects[id] = cls
        except FileNotFoundError:
            pass

    def delete_by_id(self, id):
        """
        deletes an instance by the id
        """
        del self.__objects[id]
        self.save()
