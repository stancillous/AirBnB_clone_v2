#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

import os

from models.user import User
from models.base_model import BaseModel, Base
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.dbUser = os.environ.get("HBNB_MYSQL_USER")
        self.dbPwd = os.environ.get("HBNB_MYSQL_PWD")
        self.dbHost = os.environ.get("HBNB_MYSQL_HOST")
        self.dbName = os.environ.get("HBNB_MYSQL_DB")

        # print(f"\n\tDbStorage.__init__\n")

        db_url = (
            f"mysql+mysqldb://{self.dbUser}:{self.dbPwd}@"
            f"{self.dbHost}/{self.dbName}"
        )

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        # print(f"\n\tNew engine created\n")

        if os.environ.get("HBNB_ENV") == "test":
            # Create a MetaData object
            metadata = MetaData()
            # Reflect all existing tables in the database
            metadata.reflect(bind=self.__engine)

            # loop thru and drop each table
            for table_name, table_obj in metadata.tables.items():
                table_obj.drop(self.__engine)
            # print("All tables have been dropped")

    def all(self, cls=None):
        # self.__session = Session()

        # classes to loop thru if cls != None
        objs_list = [User, State, City, Amenity, Place, Review]
        objs_dict = {}

        if (cls is None):
            # query all objs
            for obj in objs_list:
                # query the objects from the database
                query = self.__session.query(obj).all()

                # the previous query will return a list
                for item in query:
                    itemClass = item.__class__.__name__
                    itemId = item.id
                    itemKey = str(itemClass)+'.'+str(itemId)

                    # update the dictionary (objs_dict)
                    objs_dict[itemKey] = item

            return objs_dict

        else:
            # query all objs depending on the arg 'cls'
            our_query = self.__session.query(cls).all()

            for item in our_query:
                itemClass = item.__class__.__name__
                itemId = item.id
                itemKey = str(itemClass)+'.'+str(itemId)

                # update the dictionary (objs_dict)
                objs_dict[itemKey] = item
            return objs_dict

    def new(self, obj):
        """add a new obj to current db session"""
        self.__session.add(obj)

    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload our db"""
        # print(f"\n\tDbStorage.reload\n")
        Base.metadata.create_all(self.__engine)
        # Create a session factory using sessionmaker
        Session = sessionmaker(bind=self.__engine, expire_on_commit=True)

        # Create a scoped session from the session factory
        self.__session = scoped_session(Session)

        # print(f"\n\tNew session created\n")
