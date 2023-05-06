#!/usr/bin/env python3

from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a compressed archive of the web_static directory"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_file))
    if result.failed:
        return None
    return archive_file
