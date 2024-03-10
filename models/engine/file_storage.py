#!/usr/bin/python3
"""
File storage class the serializes instances to JSON FIlE
and deserializes JSON FILE to instances
"""

import json
from .classes_ import classes


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

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
                allDicts = json.load(fp)

            self.__objects = {}

            for id, dict in allDicts.items():
                cls_name = classes[dict['__class__'].lower()]
                cls = cls_name(**dict)
                self.__objects[id] = cls
        except FileNotFoundError:
            pass

    def delete_by_id(self, id):
        """
        deletes an instance by the id
        """
        del self.__objects[id]
        self.save()
