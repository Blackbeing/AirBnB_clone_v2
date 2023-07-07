#!/usr/bin/python3
"""
This module clean up old files from local and servers
"""

from fabric.api import local, run, env

env.hosts = ["54.85.182.135", "100.25.165.99"]


def do_clean(number=0):
    """
    clean old files locally and remotely

    Arguments:
        number: number of most recent archives to keep
    """
    number = number if number > 1 else 1
    number += 1
    local("ls -t *.py | tail -n +{}".format(number))
    run(
        "ls -dt /data/web_static/releases/web_static* | \
                tail -n +{} | \
                xargs -r rm -r --".format(
            number
        )
    )
