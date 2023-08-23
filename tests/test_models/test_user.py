#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    # def test_first_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.first_name), str)

    # def test_last_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.last_name), str)

    # def test_email(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.email), str)

    # def test_password(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.password), str)

import unittest
from models.user import User
from models import storage

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a clean storage instance before each test"""
        storage.reload()

    def test_user_attributes(self):
        """Test if User class has the expected attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_instance(self):
        """Test if user is an instance of User class"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_save_method(self):
        """Test if save method updates the updated_at attribute"""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    # def test_user_to_dict_method(self):
    #     """Test if to_dict method returns a dictionary"""
    #     user = User(email="test@example.com", password="test_password")
    #     user_dict = user.to_dict()
    #     self.assertIsInstance(user_dict, dict)

    # def test_user_to_dict_keys(self):
    #     """Test if the keys exist in the to_dict return value"""
    #     user = User(email="test@example.com", password="test_password")
    #     user_dict = user.to_dict()
    #     self.assertIn('id', user_dict)
    #     self.assertIn('created_at', user_dict)
    #     self.assertIn('updated_at', user_dict)
    #     self.assertIn('email', user_dict)
    #     self.assertIn('password', user_dict)
    #     self.assertIn('first_name', user_dict)
    #     self.assertIn('last_name', user_dict)
    #     self.assertIn('__class__', user_dict)

    # def test_user_create_instance_from_dict(self):
    #     """Test if an instance can be created from a dictionary"""
    #     user_data = {
    #         'id': 'test_id',
    #         'created_at': '2022-01-01T00:00:00',  # Set the created_at attribute
    #         'updated_at': '2022-01-01T00:00:00',
    #         'email': 'test@example.com',
    #         'password': 'test_password',
    #         'first_name': 'John',
    #         'last_name': 'Doe',
    #         '__class__': 'User'
    #     }
    #     user = User(**user_data)
    #     self.assertEqual(user.id, 'test_id')
    #     self.assertEqual(user.email, 'test@example.com')
    #     self.assertIsNotNone(user.created_at)  # Ensure created_at is not None


    def test_user_delete_method(self):
        """Test if delete method removes the object from storage"""
        user = User()
        user.save()
        user_id = user.id
        user.delete()
        self.assertIsNone(storage.all(User).get(user_id))

if __name__ == '__main__':
    unittest.main()
