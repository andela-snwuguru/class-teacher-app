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
from .models import ClassRoom
from students.models import Student

class ClassRoomList(ListView):
    template_name = 'classroom/list.html'
    model = ClassRoom

class ClassRoomDetail(DetailView):
    template_name = 'classroom/detail.html'
    model = ClassRoom

    def get_context_data(self, **kwargs):
        context = super(ClassRoomDetail, self).get_context_data(**kwargs)
        context['object_list'] = Student.objects.filter(room=context['object'])
        return context

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