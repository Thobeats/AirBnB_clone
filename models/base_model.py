#!/usr/bin/python3
"""
The BaseModel that defines all common
methods and attributes for other classes
"""

import cmd
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    The BaseModel Class serves as a parent class for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        initialises a new instance of the base class
        """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dict_rep = {}
        time_format = datetime.isoformat
        for key in self.__dict__:
            value = self.__dict__[key]
            if key == "created_at" or key == "updated_at":
                dict_rep[key] = str(time_format(value))
            else:
                dict_rep[key] = value
        dict_rep["__class__"] = type(self).__name__
        return dict_rep

