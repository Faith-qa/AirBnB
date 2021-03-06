#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import uuid
import datetime
import random


class Test_BaseModel(unittest.TestCase):
    """
    test cases for basemodel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        check if instance id is cteated and initialized

        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_if_type_id_str(self):
        """
        check if id type is string
        """
        b = BaseModel()
        self.assertTrue(type(b.id), str)

    def test_if_id_is_unique(self):
        """
        check if id is unique
        """
        
        b1 = BaseModel()
        b2 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
    
    def BaseModel_instance_has_created_at(self):
        """
        test if instance created_at us created and initialized
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "created_at"))

    def test_if_created_at_is_datetime(self):
        """
        test if created_at is an instance of datetime
        """
        b = BaseModel()
        self.assertTrue(type(b.created_at), datetime)

    def test_str__(self):
        """
        test str output
        """
        b = BaseModel()
        self.assertEqual(b.__str__(), "[{}] ({}) {}".format(type(b).__name__, b.id,  b.__dict__))


        
