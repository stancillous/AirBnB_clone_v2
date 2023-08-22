#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.review import Review
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    # city_id = ""
    # user_id = ""
    # name = ""
    # description = ""
    # number_rooms = 0
    # number_bathrooms = 0
    # max_guest = 0
    # price_by_night = 0
    # latitude = 0.0
    # longitude = 0.0
    # amenity_ids = []

    """New attrs"""
    __tablename__ = 'places'
    city_id = Column(String(length=60),
                     ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(length=60),
                     ForeignKey('users.id'), nullable=False, )
    name = Column(String(length=128), nullable=False)
    description = Column(String(length=1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("Review", backref="user", cascade="delete")

    @property
    def reviews(self):
        """Returns list of review instances"""
        reviews_lst = []
        from models.storage import storage
        # returns a dict with instances of Class City
        instances_dict = storage.all(Review)

        for key, value in instances_dict.items():
            if value.place_id == self.id:
                reviews_lst.append[value]
        return reviews_lst
