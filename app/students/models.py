from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from classroom.models import ClassRoom
from subject.models import Subject

class Student(models.Model):
    room = models.ForeignKey(ClassRoom, default=0)
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk':self.id})

    class Meta:
        ordering = ['-created_date']



class StudentSubject(models.Model):
  student = models.ForeignKey(Student)
  subject = models.ForeignKey(Subject)
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.student.first_name

  class Meta:
    ordering = ['-created_date']