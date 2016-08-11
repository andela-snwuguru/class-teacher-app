from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView,
    )
from django.http import HttpResponseRedirect, Http404
from classroom.forms import ClassesForm
from classroom.models import ClassRoom

class ClassRoomList(ListView):
    template_name = 'classroom/list.html'
    model = ClassRoom

class ClassRoomDetail(DetailView):
    template_name = 'classroom/detail.html'
    model = ClassRoom

class ClassRoomCreate(CreateView):
    template_name = 'classroom/form.html'
    model = ClassRoom
    fields = [
            'name',
            'capacity',
        ]

class ClassRoomUpdate(UpdateView):
    template_name = 'classroom/form.html'
    model = ClassRoom
    fields = [
            'name',
            'capacity',
        ]

class ClassRoomDelete(DeleteView):
    template_name = 'classroom/delete.html'
    model = ClassRoom
    success_url = '/classes/'