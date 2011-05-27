import os
import sys
import site

site.addsitedir('/home/mikkelandersen/.virtualenvs/mikkelandersen/lib/python2.7/site-packages')
sys.path.append('/home/mikkelandersen/srv')
sys.path.append('/home/mikkelandersen/srv/mikkel')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mikkel.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
