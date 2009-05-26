from django.db import models
from datetime import datetime

class FutureEventManager(models.Manager):
    def get_query_set(self):
        return super(FutureEventManager, self).get_query_set().filter(date__gte=datetime.now())

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
        
    objects = models.Manager()
    future = FutureEventManager()


