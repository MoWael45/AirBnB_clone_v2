#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os
import models

class TestBaseModel(unittest.TestCase):

    def test_id_generation(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)

    def test_created_at(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsNotNone(bm.created_at)

    def test_updated_at(self):
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        sleep(0.01)  # Simulating time passing
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_str_representation(self):
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIn("BaseModel", bm_str)
        self.assertIn(bm.id, bm_str)

    def test_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="custom_id", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "custom_id")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_save_method(self):
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        sleep(0.01)  # Simulating time passing
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_additional_attributes(self):
        bm = BaseModel()
        bm.name = "Test Model"
        bm.my_number = 42
        bm_dict = bm.to_dict()
        self.assertIn("name", bm_dict)
        self.assertIn("my_number", bm_dict)
        self.assertEqual(bm_dict["name"], "Test Model")
        self.assertEqual(bm_dict["my_number"], 42)

if __name__ == "__main__":
    unittest.main()
