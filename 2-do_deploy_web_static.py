#!/usr/bin/python3
"""fabric script"""
from fabric.api import *
import os
#   username, and host
env.user = os.environ.get('ubuntu')
env.hosts = ['34.73.113.30', '35.185.32.152']


def do_deploy(archive_path):
    """function that distributes an archive to a server"""
    if os.path.isfile('{}'.format(archive_path)) is False:
        return False
    tgz_file = archive_path.split('/')[-1]
    storage_location = '/tmp/'
    new_location = '/data/web_static/releases/'
    upload = put('{}'.format(archive_path), storage_location)
    if upload is False:
        return False
    uncompress = run('tar -xzvf {} -C {}'.format(storage_location +
                                                 tgz_file, new_location))
    if uncompress is False:
        return False
    delete_file = run('rm -f {}'.format(storage_location + tgz_file))
    if delete_file is False:
        return False
    sym_link_name = '/data/web_static/current'
    delete_sym = run('rm -f {}'.format(sym_link_name))
    if delete_sym is False:
        return False
    create_sym = run('ln -sT {} {}'.format(new_location +
                                           tgz_file.replace('.tgz', ''),
                                           sym_link_name))
    if create_sym is False:
        return False
    return True


def do_pack():
    """function to generate a tgz archive"""
    import datetime
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = 'versions/web_static_{}.tgz'.format(date)
    dir_path = 'web_static'
    local('mkdir -p versions')
    command = local('tar -cvzf {} {}'.format(filename, dir_path))
    archive_path = os.environ.get('PWD') + '/' + filename
    if command.succeeded:
        return archive_path
    return None
