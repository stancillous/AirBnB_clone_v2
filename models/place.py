#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import MetaData, Table, Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


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

    # create an instance of SQLAl table called place_amenity
    # for creating rlshp Many to Many btwn Place and Amenity
    # metadata = MetaData()
    metadata = Base.metadata
    place_amenity = Table(
        "place_amenity", metadata,
        Column('place_id', String(60), ForeignKey('places.id')),
        Column('amenity_id', String(60, ForeignKey('amenities.id')))
    )

    amenity_ids = []

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
    reviews = relationship("Review", backref="user", cascade="all, delete")

    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False,)

    @property
    def reviews(self):
        """Returns list of review instances"""
        reviews_lst = []
        from models import storage
        # returns a dict with instances of Class City
        instances_dict = storage.all(Review)

        for key, value in instances_dict.items():
            if value.place_id == self.id:
                reviews_lst.append[value]
        return reviews_lst
    



    @property
    def amenities(self): # getter attr amenities
        """Returns list of review instances"""
        amenities_lst = []
        from models import storage
        # returns a dict with instances of Class City
        instances_dict = storage.all(Amenity)

        for am_instance in instances_dict.values():
            if am_instance.place_id == self.id:
                amenities_lst.append[am_instance]
        return amenities_lst
    
    @property.setter
    def amenities(self, obj=None):
        """appends Amenity.id to the att amenity_ids"""
        if isinstance(obj, Amenity):
            Place.amenity_ids.append(obj.id)

    
