from django.contrib import admin
from testimonials.models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    fields = ('quote', 'name', 'place', 'date', 'event')
    list_display = ('quote', 'name', 'place', 'date', 'event')
    list_filter = ('date',)
    search_fields = ('quote', 'name', 'place', 'event')

admin.site.register(Testimonial, TestimonialAdmin)
