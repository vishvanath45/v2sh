# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import SuperUser, Experience

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutus(request):
	return render(request, 'aboutus.html')

def reportissue(request):
	return render(request, 'issue_report.html')

def authenticate(request):
	return render(request, 'authenticate.html')

def contactform(request):
	return render(request, 'contactform.html')

def superuserprofile(request):

	user = SuperUser.objects.all()[0]
	exp = Experience.objects.get(object_name = user)
	return render(request, 'superuserprofile.html',{'user':user,'exp':exp})
