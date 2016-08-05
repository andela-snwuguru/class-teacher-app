from __future__ import unicode_literals
from django.db import models
from classes.models import Classes

class Student(models.Model):
    room = models.ForeignKey(Classes, default=0)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['-created_date']

