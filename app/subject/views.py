from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import Subject
from .forms import SubjectForm


class SubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        form = SubjectForm(request.POST or None)
        return render(request, 'subject/list.html', {'object_list': subjects, 'form': form})

    def post(self, request):
        form = SubjectForm(request.POST or None)
        if(form.is_valid()):
          form.save()
          return HttpResponseRedirect('/subjects/')

        subjects = Subject.objects.all()
        return render(request, 'subject/list.html', {'object_list': subjects, 'form': form})


class SubjectDeleteView(View):
    def get(self, request, **kwargs):
        subject = Subject.objects.filter(pk=kwargs.get('pk'))
        if subject:
            subject.delete()
        return HttpResponseRedirect('/subjects/')
