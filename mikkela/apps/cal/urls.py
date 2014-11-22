from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'cal.views.index', name='cal_index'),
)
