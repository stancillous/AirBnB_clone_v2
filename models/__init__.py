#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os


if (os.environ.get("HBNB_TYPE_STORAGE") == "db"):
    from models.engine.db_storage import DBStorage
    # print(f"\n\tBefore starting dbstorage\n")
    storage = DBStorage()
    # print(f"\n\tAfter starting dbstorage\n")
    storage.reload()

else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()

