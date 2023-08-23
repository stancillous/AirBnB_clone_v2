#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    # def test_name2(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        # Test creating an Amenity instance
        amenity = Amenity(name="WiFi")
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        # Test attributes of the Amenity class
        amenity = Amenity(name="TV")
        self.assertEqual(amenity.name, "TV")

    # def test_amenity_to_dict(self):
    #     # Test the to_dict method of the Amenity class
    #     amenity = Amenity(name="Pool")
    #     amenity_dict = amenity.to_dict()
    #     self.assertEqual(amenity_dict["name"], "Pool")
    #     self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_amenity_from_dict(self):
        # Test creating an Amenity instance from a dictionary
        amenity_dict = {"name": "Balcony", "__class__": "Amenity", "id": "12345"}
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.name, "Balcony")
        self.assertEqual(amenity.id, "12345")


if __name__ == '__main__':
    unittest.main()
