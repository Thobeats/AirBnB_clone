#!/usr/bin/python3
"""
base_model.py
user.py
engine/
    __init__.py
    file_storage.py
"""

from .engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

storage = FileStorage()
storage.reload()
