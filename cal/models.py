from django.db import models

class Event(models.Model):
    name =  models.CharField('titel', max_length=50)
    loc  =  models.CharField('sted', max_length=50)
    address = models.CharField('adresse', blank=True, null=True, max_length=100)
    link =  models.URLField(blank=True, null=True)
    #desc= models.TextField(blank=True, null=True)
    date =  models.DateTimeField('dato og tid')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'
        verbose_name = 'arrangement'
        verbose_name_plural = 'arrangementer'

