#!/usr/bin/python3
"""
Deploy module using fabric
"""

from pathlib import Path
from fabric.api import env, run, put

env.hosts = ["54.160.93.22", "18.234.169.109"]


def do_deploy(archive_path):
    """
    Deploy static content to multiple webservers

    Arguments:
        archive_path: Path to archive

    Returns:
        Bool
    """
    archive_path = Path(archive_path)

    if not archive_path.exists():
        return False

    # Upload archive to remote hosts
    if put(str(archive_path), "/tmp/").failed:
        return False

    # Create directory to extract archive
    if run(
        "mkdir -p /data/web_static/releases/{}".format(archive_path.stem)
    ).failed:
        return False

    # Extract archive
    if run(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_path.name, archive_path.stem
        )
    ).failed:
        return False

    # Remove archive
    if run("rm -rf /tmp/{}".format(archive_path.name)).failed:
        return False

    if run(
        "mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}".format(
            archive_path.stem, archive_path.stem
        )
    ).failed:
        return False
    if run(
        "rm -rf /data/web_static/releases/{}/web_static".format(
            archive_path.stem
        )
    ).failed:
        return False

    # Remove old symbolic link
    if run(
        "rm -rf /data/web_static/current".format(archive_path.stem)
    ).failed:
        return False

    # Create new symbolic link
    if run(
        "ln -s /data/web_static/releases/{} /data/web_static/current".format(
            archive_path.stem
        )
    ).failed:
        return False
    return True
