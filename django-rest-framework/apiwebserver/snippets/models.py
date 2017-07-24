# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Think of a Snippet as a part of a template. It's basically a piece
#of content with a given name that can be included and
#rendered with a template with templatetag ``include_snippet``.

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(blank=False, default='None')
    humidity = models.FloatField(blank=False, default='None')

    class Meta:
        #Note the ,: it causes the variable to be created as a 'list', which is required because a single value cannot be orderned.
        ordering = ('created',)
