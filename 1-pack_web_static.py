#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""


import time
from fabric import task

@task
def do_pack(c):
    # Create the versions folder if it doesn't exist
    c.run('mkdir -p versions')

    # Generate the archive name based on the current time
    timestamp = time.strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'

    # Compress the web_static folder into the archive
    c.run(f'tar -czvf versions/{archive_name} web_static')

    # Check if the archive was created successfully
    archive_path = f'versions/{archive_name}'
    if c.run(f'test -e {archive_path}').ok:
        return archive_path
    else:
        return None
