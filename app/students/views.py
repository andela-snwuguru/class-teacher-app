from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView,
    )
from django.http import HttpResponseRedirect, Http404
from students.forms import StudentForm
from students.models import Student

class StudentList(ListView):
    template_name = 'student/list.html'
    model = Student

class StudentDetail(DetailView):
    template_name = 'student/detail.html'
    model = Student

class StudentCreate(CreateView):
    template_name = 'student/form.html'
    model = Student
    fields = [
            'first_name',
            'last_name',
            'room',
        ]

class StudentUpdate(UpdateView):
    template_name = 'student/form.html'
    model = Student
    fields = [
            'first_name',
            'last_name',
            'room',
        ]

class StudentDelete(DeleteView):
    template_name = 'student/delete.html'
    model = Student
    success_url = '/students/'