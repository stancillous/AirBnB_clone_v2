#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    # def test_place_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.place_id), str)

    # def test_user_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.user_id), str)

    # def test_text(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.text), str)


import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a clean instance of Review for each test."""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test."""
        del self.review

    def test_instantiation(self):
        """Test if an instance of Review is properly instantiated."""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test the attributes of a Review instance."""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))

    def test_text_attribute(self):
        """Test the 'text' attribute of Review."""
        self.review.text = "A great place to stay!"
        self.assertEqual(self.review.text, "A great place to stay!")

    def test_place_id_attribute(self):
        """Test the 'place_id' attribute of Review."""
        self.review.place_id = "12345"
        self.assertEqual(self.review.place_id, "12345")

    def test_user_id_attribute(self):
        """Test the 'user_id' attribute of Review."""
        self.review.user_id = "67890"
        self.assertEqual(self.review.user_id, "67890")

if __name__ == '__main__':
    unittest.main()
