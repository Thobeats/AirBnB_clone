#!/usr/bin/python3
"""
The BaseModel that defines all common
methods and attributes for other classes
"""

import cmd
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The BaseModel Class serves as a parent class for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        initialises a new instance of the base class
        """
        if kwargs and len(kwargs) > 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs['id']
                if key == "name":
                    self.name = kwargs['name']
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "my_number":
                    self.my_number = kwargs['my_number']
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        override the default __str__ function and
        return the str representation of the class
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        """
        updates the value of updated_at
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        classDictionary = self.__dict__
        classDictionary['__class__'] = __class__.__name__
        created_at = classDictionary['created_at']
        updated_at = classDictionary['updated_at']
        str_created_at = created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        str_updated_at = updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        classDictionary['created_at'] = str_created_at
        classDictionary['updated_at'] = str_updated_at
        return classDictionary
