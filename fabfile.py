import os
from fabric.api import local
from fabric.contrib.project import rsync_project
from fabric.api import run, env
#
# env.hosts = ['47.90.18.219',]
# env.hosts = ['203.156.198.183', '67.207.85.65',]
env.hosts = ['67.207.85.65',]
env.user = "jiaxin"


def test_store():
    local("./manage.py test store")

def test():
    test_store()

def deploy_static():
    local("./manage.py compilemessages")
    local("./manage.py collectstatic --noinput --settings='haumea.settings.deploy'")
    local("./manage.py compress --settings='haumea.settings.deploy'")
    rsync_project(
        remote_dir='/data/static/haumea/',
        local_dir='/tmp/static/',
        delete=True
    )

def deploy_python():
    local('find . -name "*.pyc" -exec rm {} \;')
    rsync_project(
        remote_dir='/data/www/magellanic/',
        local_dir='{dir}/'.format(dir=os.getcwd()),
        # exclude=('.git',  '.idea/', 'magellanic/whoosh_index/'),
        exclude=('.git', 'db.sqlite3', '.idea/', ),
        delete=True,
    )

def clear():
    local('rm -rf /tmp/static/')

def deploy():
    test()
    deploy_static()
    deploy_python()
    clear()