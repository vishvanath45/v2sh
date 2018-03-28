# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutus(request):
	return render(request, 'aboutus.html')

def reportissue(request):
	return render(request, 'issue_report.html')

def authenticate(request):
	return render(request, 'authenticate.html')

def superuserprofile(request):
	return render(request, 'superuserprofile.html')