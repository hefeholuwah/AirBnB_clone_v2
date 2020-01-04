#!/usr/bin/python3
""" create tgz from /web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack """
    archive_name = 'web_static_' +
    datetime.strftime(datetime.now(), "%Y%m%d%I%M%S") +
    '.tgz'

    local('mkdir -p versions')
    direc = 'versions/'
    archive = local('tar -cvzf {}{} web_static'.format(direc, archive_name))
    if archive.failed:
        return None
    if archive.succeeded:
        return direc + archive_name
