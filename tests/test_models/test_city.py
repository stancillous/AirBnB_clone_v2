#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    # def test_state_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.state_id), str)

    # def test_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)

import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from models.place import Place

class TestCity(unittest.TestCase):
    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))

    def test_save_method(self):
        """Test save method of City"""
        city = City()
        prev_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(prev_updated_at, city.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of City"""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertIsInstance(city_dict['id'], str)

    def test_create_new_city(self):
        """Test creating a new City instance"""
        city = City(name="New York", state_id="NY")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "NY")

    # def test_city_relationship(self):
    #     """Test the relationship between City and Place"""
    #     city = City()
    #     place = Place(city_id=city.id)
    #     self.assertIn(place, city.places)

    # def test_city_deletion(self):
    #     """Test deleting a City instance"""
    #     city = City()
    #     storage.new(city)
    #     city_id = city.id
    #     storage.save()
    #     del_city = storage.get(City, city_id)
    #     self.assertEqual(del_city, city)
    #     storage.delete(city)
    #     storage.save()
    #     del_city = storage.get(City, city_id)
    #     self.assertIsNone(del_city)

if __name__ == '__main__':
    unittest.main()
