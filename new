#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """script that generates a .tgz archive from the
    contents of the web_static folder"""
    filedate = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"web_static_{filedate}.tgz"

    try:
        local("mkdir -p versions")
        local(f"python -m tarfile -vc versions/{filename} web_static/")
        return "versions/{filename}".format(filename)
    except Exception as e:
        return None
