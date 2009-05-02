from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'cal.views.index', name='cal_index'),
)
