#!/usr/bin/python3
"""
The Test for the BaseModel
"""


import unittest
import pep8

from models.base_model import BaseModel


class TestBase(unittest.TestCase):

    def test__init__(self):
        """
        different tests for the id property
        test for id is None and id has a value
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_pepEight_code_style(self):
        """ test if the code follows pep8 codestyle """
        pepEightStyle = pep8.StyleGuide(quiet='true')
        result = pepEightStyle.check_files(['models/base_model.py'])
        error = "Found code style errors (and warnings)"
        self.assertEqual(result.total_errors, 0, error)
