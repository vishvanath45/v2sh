# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'contents/home.html')

def aboutus(request):
	return render(request, 'contents/aboutus.html')

def reportissue(request):
	return render(request, 'contents/issue_report.html')
