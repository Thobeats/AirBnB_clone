#!/usr/bin/python3
"""
class variable that holds all the class to be used
"""


from models.base_model import BaseModel
from models.user import User


classes = {
    "basemodel": BaseModel,
    "user": User
}
