# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .forms import RegisterForm,LoginForm

from .models import user
# Create your views here.

def authenticate(request):
    return render(request, 'accounts/authenticate.html')

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        passwd = request.POST['password']
        User = user.objects.create(name = name , email = email , pwd = passwd)
        return render(request , 'contents/home.html' , {'User' : User})


    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    form  = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['password']
        try:
            User = user.objects.get(email = email ,pwd = passwd)
            return render(request, 'contents/home.html', {'User': User})
        except:
            return render(request, 'accounts/login.html', {'form': form})

    return render(request , 'accounts/login.html' , {'form' : form})