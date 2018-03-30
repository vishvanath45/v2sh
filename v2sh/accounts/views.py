# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login

from django.shortcuts import render,redirect

from .forms import RegisterForm

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
