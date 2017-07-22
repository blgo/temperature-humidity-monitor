# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item,item) for item in get_all_styles())

# Create your models here.
#Think of a Snippet as a part of a template. It's basically a piece
#of content with a given name that can be included and
#rendered with a template with templatetag ``include_snippet``.

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.TextField(default=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        #Note the ,: it causes the variable to be created as a 'list', which is required because a single value cannot be orderned.
        ordering = ('created',)
