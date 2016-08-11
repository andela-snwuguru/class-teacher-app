from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.views.generic import (
        CreateView,
        DetailView,
        DeleteView,
        ListView,
        UpdateView,
        View,
    )
from django.http import HttpResponseRedirect, Http404
from students.forms import StudentForm, StudentSubjectForm
from students.models import Student, StudentSubject

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

class StudentSubjectView(View):
    template_name = 'student/student_subject.html'

    def get(self, request, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        subjects = StudentSubject.objects.filter(student=student)
        form = StudentSubjectForm(request.POST or None)
        return render(request, self.template_name, {'form': form, 'subject_list': subjects, 'student': student})

    def post(self, request, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = StudentSubjectForm(request.POST or None)
        if(form.is_valid()):
            subject = form.save(commit=False)
            subject.student = student
            subject.save()
            return HttpResponseRedirect('/students/'+ str(student.id) + '/subject/')
        subjects = StudentSubject.objects.filter(student=student)
        return render(request, self.template_name, {'form': form, 'subject_list': subjects, 'student': student})


class StudentSubjectDeleteView(View):

    def get(self, request, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        student_subject = StudentSubject.objects.get(pk=kwargs.get('student_subject_id'))
        if student_subject:
            student_subject.delete()
        return HttpResponseRedirect('/students/'+ str(student.id) + '/subject/')
