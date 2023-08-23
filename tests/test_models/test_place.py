#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    # def test_city_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.city_id), str)

    # def test_user_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.user_id), str)

    # def test_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)

    # def test_description(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.description), str)

    # def test_number_rooms(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.number_rooms), int)

    # def test_number_bathrooms(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.number_bathrooms), int)

    # def test_max_guest(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.max_guest), int)

    # def test_price_by_night(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.price_by_night), int)

    # def test_latitude(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.latitude), float)

    # def test_longitude(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

import unittest
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_inheritance(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))

    def test_relationship(self):
        self.assertTrue(hasattr(self.place, 'reviews'))
        # self.assertTrue(hasattr(self.place, 'amenities'))

    # def test_amenities(self):
    #     amenity = Amenity()
    #     self.place.amenities.append(amenity)
    #     self.assertIn(amenity, self.place.amenities)

    # def test_reviews(self):
    #     review = Review()
    #     self.place.reviews.append(review)
    #     self.assertIn(review, self.place.reviews)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_save(self):
        self.assertEqual('save' in dir(self.place), True)

    def test_delete(self):
        self.assertEqual('delete' in dir(self.place), True)

if __name__ == '__main__':
    unittest.main()
