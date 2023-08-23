#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    # def test_name3(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)

import unittest
from models.state import State
from models.city import City


class TestState(unittest.TestCase):

    def test_state_attributes(self):
        # Test the initialization of State attributes
        state = State()
        # self.assertEqual(state.name, "")
        self.assertEqual(state.cities, [])

    def test_state_name(self):
        # Test setting and getting the name attribute
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    # def test_add_city(self):
    #     """Test adding a city to the state's cities list"""
    #     state_data = {
    #         "name": "California"
    #     }
    #     city_data = {
    #         "name": "San Francisco"
    #     }
    #     state = State(**state_data)
    #     city = City(**city_data)
    #     state.cities.append(city)
    #     self.assertIn(city, state.cities)  # Check if the city is added


    # def test_remove_city(self):
    #     """Test removing a city from the state's cities list"""
    #     state_data = {
    #         "name": "California"
    #     }
    #     city_data = {
    #         "name": "San Francisco"
    #     }
    #     state = State(**state_data)
    #     city = City(**city_data)
    #     state.cities.append(city)
    #     self.assertIn(city, state.cities)  # Check if the city is in the list
    #     state.cities.remove(city)
    #     self.assertNotIn(city, state.cities)  # Check if the city is removed


    def test_to_dict_method(self):
        # Test the to_dict method of the State class
        state_data = {
            "id": "123",
            "name": "California",
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-01T00:00:00",
        }
        state = State(**state_data)
        state_dict = state.to_dict()
        self.assertEqual(state_dict["id"], "123")
        self.assertEqual(state_dict["name"], "California")
        self.assertEqual(state_dict["created_at"], "2023-01-01T00:00:00")
        self.assertEqual(state_dict["updated_at"], "2023-01-01T00:00:00")

if __name__ == '__main__':
    unittest.main()

