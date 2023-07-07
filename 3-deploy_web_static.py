#!/usr/bin/python3
"""
Pack and deploy static content using fabric
"""

from fabric.api import env, put, run, local
from pathlib import Path
from datetime import datetime

env.hosts = ["54.85.182.135", "100.25.165.99"]


def do_pack():
    """
    Compress folder to tgz archive
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(now)

    # Make version directory
    local("mkdir -p versions")
    result = local(
        "tar -cvzf versions/{} {}".format(archive_name, "web_static"),
    )
    if result.failed:
        return None
    return "versions/{}".format(archive_name)


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


def deploy():
    """
    Wrapper for do_pack and do deploy
    """
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
