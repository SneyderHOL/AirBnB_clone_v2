from fabric.api import *
import os
#   username, and host
env.user = os.environ.get('USER')
env.hosts = ['localhost']


def do_pack():
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
