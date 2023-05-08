#!/usr/bin/python3
"""
Distributes an archive to your web servers, using the function do_deploy
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """ Deploys the web static """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_file = archive_path.split("/")[-1]
        folder_name = ("/data/web_static/releases/" + archive_file.split(".")[0])
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, folder_name))
        run("rm /tmp/{}".format(archive_file))
        run("mv {}/web_static/* {}".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_name))
        print("New version deployed!")
        return True
    except:
        return False

