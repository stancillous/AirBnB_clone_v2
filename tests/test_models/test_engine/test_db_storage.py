import unittest
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os

class TestDBStorageMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set the database connection variables as environment variables
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        # Set up a DBStorage instance for testing
        
        cls.db_storage = DBStorage()
        cls.db_storage.reload()
        cls.session = cls.db_storage._DBStorage__session

        
    @classmethod
    def tearDownClass(cls):
        # Close the session and drop all tables when done
        cls.session.close()
        cls.db_storage._DBStorage__engine.dispose()

    # def test_state(self):
    #     # Test creating, saving, and reloading a State object
    #     state = State(name="California")
    #     state.save()
    #     self.assertTrue(state.id in self.db_storage.all(State))

    # def test_city(self):
    #     # Test creating, saving, and reloading a City object
    #     state = State(name="California")
    #     state.save()
    #     city = City(name="San Francisco", state_id=state.id)
    #     city.save()
    #     self.assertTrue(city.id in self.db_storage.all(City))

    # def test_user(self):
    #     # Test creating, saving, and reloading a User object
    #     user = User(email="john@snow.com", password="johnpwd")
    #     user.save()
    #     self.assertTrue(user.id in self.db_storage.all(User))

    # def test_place(self):
    #     # Test creating, saving, and reloading a Place object
    #     state = State(name="California")
    #     state.save()
    #     user = User(email="john@snow.com", password="johnpwd")
    #     user.save()
    #     city = City(name="San Francisco", state_id=state.id)
    #     city.save()
    #     place = Place(user_id=user.id, city_id=city.id, name="House 1")
    #     place.save()
    #     self.assertTrue(place.id in self.db_storage.all(Place))

    # def test_review(self):
    #     # Test creating, saving, and reloading a Review object
    #     state = State(name="California")
    #     state.save()
    #     user = User(email="john@snow.com", password="johnpwd")
    #     user.save()
    #     city = City(name="San Francisco", state_id=state.id)
    #     city.save()
    #     place = Place(user_id=user.id, city_id=city.id, name="House 1")
    #     place.save()
    #     review = Review(user_id=user.id, place_id=place.id, text="Great place!")
    #     review.save()
    #     self.assertTrue(review.id in self.db_storage.all(Review))

    # def test_amenity(self):
    #     # Test creating, saving, and reloading an Amenity object
    #     amenity = Amenity(name="Wifi")
    #     amenity.save()
    #     self.assertTrue(amenity.id in self.db_storage.all(Amenity))

if __name__ == '__main__':
    unittest.main()
