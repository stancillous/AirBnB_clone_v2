#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    # name = ""

    """New class attrs"""
    __tablename__ = 'states'
    name = Column(String(length=128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    """Getter attribute"""
    @property
    def cities(self):
        """Returns list of cities that match state id"""
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)

        return city_list
