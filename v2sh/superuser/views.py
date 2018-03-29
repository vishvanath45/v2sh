# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import SuperUser, Experience

# Create your views here.
def contactform(request):
	return render(request, 'superuser/contactform.html')

def superuserprofile(request):

	user = SuperUser.objects.all()[0]
	exp = Experience.objects.get(object_name = user)
	return render(request, 'superuser/superuserprofile.html',{'user':user,'exp':exp})
