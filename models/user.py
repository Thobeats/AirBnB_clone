#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A user class that defines all clients of
    the Airbnb project
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
