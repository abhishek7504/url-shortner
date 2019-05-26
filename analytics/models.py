from django.db import models

# Create your models here.
from url_short.models import FellaURL


class ClickEventManager(models.Manager):
    def create_event(self, kirrInstance):
        if isinstance(kirrInstance, FellaURL):
            obj, created = self.get_or_create(fella_url=kirrInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    fella_url    = models.OneToOneField(FellaURL, on_delete=models.CASCADE)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True) 
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)