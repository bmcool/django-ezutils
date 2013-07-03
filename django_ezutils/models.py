# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from unidecode import unidecode
from mezzanine.core.models import Slugged

class TimestampModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class UnicodeSluggedBase:
    def get_slug(self):
        return slugify(unidecode(self.title))

class UnicodeSlugged(UnicodeSluggedBase, Slugged):
    class Meta:
        abstract = True
    
    