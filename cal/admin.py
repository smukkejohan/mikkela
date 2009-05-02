from django.contrib import admin
from mikkel.cal.models import Event

class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'loc', 'address', 'link')
    list_display = ('name', 'loc', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'loc')

admin.site.register(Event, EventAdmin)
