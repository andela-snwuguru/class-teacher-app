from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect, Http404
from classes.forms import ClassesForm
from classes.models import Classes

class ClassesView(View):
    def get(self, request, *args, **kwargs):
        classes = Classes.objects.all()
        form = ClassesForm(request.POST or None)
        return render(request, 'classes.html', {'form': form, 'classes': classes})

    def post(self, request, *args, **kwargs):
        form = ClassesForm(request.POST or None)
        if form.is_valid():
            class_data = form.save(commit=False)
            class_data.user = request.user
            class_data.save()
            messages.success(request, 'New class successfully added')
        else:
            messages.success(request, 'Invalid data entry')
        return HttpResponseRedirect('/classes/')
