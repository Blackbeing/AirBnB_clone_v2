#!/usr/bin/python3
"""
Fabric module to compress folder to tgz archive for deployment
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Compress folder to tgz archive
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(now)

    # Make version directory
    local("mkdir -p versions")
    result = local(
        "tar -cvzf versions/{} -C web_static .".format(archive_name),
    )
    if result.failed:
        return None
    return "versions/{}".format(archive_name)
