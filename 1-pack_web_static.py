#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""


def do_pack():
    """script that generates a .tgz archive"""
    import tarfile
    from fabric.api import local
    from datetime import datetime

    now = datetime.now()
    # our tgz filename
    filename = (f"web_static_{now.year}{now.month}{now.day}\
                {now.hour}{now.minute}{now.second}.tgz")

    try:
        local("mkdir versions")
        local(f"tar -czvf versions/web_static_{filename} web_static/")
    except Exception as e:
        return None

    tgz_path = f"versions/web_static_{filename}"
    return tgz_path
