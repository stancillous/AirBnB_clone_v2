#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    # name = ""
    """new attrs"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    # place_amenities = 
    
