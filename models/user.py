#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
# from models.place import Place
# from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    # email = ''
    # password = ''
    # first_name = ''
    # last_name = ''

    """New attrs"""
    __tablename__ = "users"
    email = Column(String(length=128), nullable=False)
    password = Column(String(length=128), nullable=False)
    first_name = Column(String(length=128), nullable=False)
    last_name = Column(String(length=128), nullable=False)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
