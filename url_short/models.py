from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class FellaURLManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(FellaURLManager, self).all(*args, **kwargs).filter(active=True)

class FellaURL(models.Model):
    url = models.URLField(max_length=250)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = FellaURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(FellaURL, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url



