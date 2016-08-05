from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from django.db import models

class Classes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=140)
    capacity = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']

