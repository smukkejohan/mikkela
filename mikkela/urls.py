# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url, include

from cal.models import Event
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^kalender/', include('cal.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    #url(r'^$', 'direct_to_template',
    #    {'template': 'index.html',
    #        'extra_context':{
    #            'event_list': Event.future.all()[:4]
    #        }
    #    }),
    #url(r'^mikkel/$',       'direct_to_template', {'template': 'mikkel.html'}),
    #url(r'^virksomhed/$',   'direct_to_template', {'template': 'virksomhed.html'}),
    #url(r'^kirke/$',        'direct_to_template', {'template': 'kirke.html'}),
    #url(r'^bryllup/$',      'direct_to_template', {'template': 'bryllup.html'}),
    #url(r'^privat/$',       'direct_to_template', {'template': 'privat.html'}),
    #url(r'^musik/$',        'direct_to_template', {'template': 'musik.html'}),
)

# Serve static media through django if we are on a development server
if settings.DEVELOPMENT_MODE:
    urlpatterns += patterns('django.views',
        url(r'%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    )
