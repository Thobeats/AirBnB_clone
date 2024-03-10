#!/usr/bin/python3
"""
class variable that holds all the class to be used
"""


from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity



classes = {
    "basemodel": BaseModel,
    "user": User,
    "amenity": Amenity,
    "state": State,
    "city": City,
    "place": Place,
    "review": Review
}
