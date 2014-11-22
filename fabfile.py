from fabric.api import env, run, prefix, cd, sudo, local, get

env.user = 'mikkelandersen'
env.hosts = ['tango.johan.cc']
env.directory = '/home/mikkelandersen/srv/mikkela'
env.activate = 'source /home/mikkelandersen/.virtualenvs/mikkelandersen/bin/activate'

def deploy():
    local('git push')
    with cd(env.directory):
        with prefix(env.activate):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic')
            run('python manage.py cleanup')
            run('touch mikkela/wsgi.py') # this triggers a gracefull reload



def dump_prod_data():
	with cd(env.directory):
		with prefix(env.activate):
			run('python manage.py dumpdata articles files taggit  --indent 4 --natural > datadump.json')

			get('datadump.json', 'datadump.json')
