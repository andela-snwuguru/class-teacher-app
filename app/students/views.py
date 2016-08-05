from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect, Http404
from students.forms import StudentForm
from students.models import Student

class StudentView(View):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        form = StudentForm(request.POST or None)
        return render(request, 'students.html', {'form': form, 'students': students})

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST or None)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'New Student details successfully added')
        else:
            messages.success(request, 'Invalid data entry')
        return HttpResponseRedirect('/students/')
