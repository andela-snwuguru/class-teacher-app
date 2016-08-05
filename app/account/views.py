from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/classes/')
            else:
                error_message = "The password is valid, but the account has been disabled!"
        else:
           error_message = "The username and password were incorrect.";
        return render(request, 'login.html', {'error_message':error_message})