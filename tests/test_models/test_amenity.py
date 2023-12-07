#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """Test if Amenity class initializes attributes correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """Test the to_dict method of Amenity class."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
