from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^kalender/', include('mikkel.cal.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Serve static media through django if we are on a development server
if settings.DEVELOPMENT_MODE:
    urlpatterns += patterns('django.views',
        url(r'%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    )
