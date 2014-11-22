from django.db import models

class Testimonial(models.Model):
    quote= models.TextField('citat')
    name =  models.CharField('Navn', max_length=50)
    place  =  models.CharField('Fra', max_length=50, blank=True, null=True)
    date =  models.DateField('dato', blank=True, null=True)
    event  =  models.CharField('begivenhed', max_length=50, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('date',)
        get_latest_by = 'date'
        
