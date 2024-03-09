#!/usr/bin/python3
"""
base_model.py
user.py
engine/
    __init__.py
    file_storage.py
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
