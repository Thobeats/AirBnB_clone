#!/usr/bin/python3
"""
Write a class City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A city class
    """
    state_id = ""
    name = ""
