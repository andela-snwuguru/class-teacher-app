from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {})