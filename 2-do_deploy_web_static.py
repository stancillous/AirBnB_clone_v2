#!/usr/bin/python3
"""that distributes an archive to your web servers,"""

def do_deploy(archive_path):
    """that distributes an archive to your web servers,"""
    import os
    if not os.path.exists(archive_path):
        return False