#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""


def do_pack():
    import os
    import tarfile
    from datetime import datetime

    now = datetime.now()
    # our tgz filename
    filename = (f"web_static_{now.year}{now.month}{now.day}\
                {now.hour}{now.minute}{now.second}.tgz")

    if not os.path.exists("web_static"):
        return None

    # create dir where the tgz file will be put
    if not os.path.exists:
        os.mkdir("versions")

    with tarfile.open(f"versions/{filename}", "w:gz") as tar:
        tar.add("web_static")

    tgz_path = f"versions/{filename}"
    if os.path.exists(tgz_path):
        return tgz_path
    else:
        return None
