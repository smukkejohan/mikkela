from django.contrib import admin
from cal.models import Event

class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'loc', 'address', 'link')
    list_display = ('name', 'loc', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'loc')

admin.site.register(Event, EventAdmin)

#This should be moved to a location outside the cal app
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
admin.site.unregister(Site)
admin.site.unregister(Group)
