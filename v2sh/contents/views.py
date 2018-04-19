# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from superuser.models import SuperUser, Experience

from django.contrib.auth.decorators import login_required

from django.urls import reverse
# Create your views here.


# @login_required()
def home(request):
    return render(request, 'contents/home.html')

# @login_required()
def aboutus(request):
    return render(request, 'contents/aboutus.html')

# @login_required()
def reportissue(request):
    return render(request, 'contents/issue_report.html')

# @login_required()
def feedbackform(request):
	if(request.method=="POST"):
		note=request.POST['note']
		rating=request.POST['rating']
		ask=request.POST.getlist('ask')
		# print(note)
		# print(rating)
		# print(ask)	
	return render(request, 'contents/feedbackform.html')

# @login_required()
def ourmission(request):
    return render(request, 'contents/ourmission.html')

# @login_required()

def bycompany(request,alpha):
    alpha1=alpha.upper()
    names=[]
    number_of_people=[]
    job_count_pairs = []
    for i in range(Experience.objects.count()):
        if(Experience.objects.all()[i].company_name[0]==alpha or Experience.objects.all()[i].company_name[0]==alpha1):
            names.append(Experience.objects.all()[i].company_name)
    for i in names:
        cnt=0
        for j in range(Experience.objects.count()):
            if(str(i)== str(Experience.objects.all()[j].company_name)):
                cnt+=1
        number_of_people.append(cnt)
    for i in range(len(names)):
        job_count_pairs.append((names[i], number_of_people[i]))

    return render(request,'search_results/bycompany.html',{'names':job_count_pairs,'alpha':alpha1})



def byyear(request,beta):
    year_passed = int(beta)
    user_names = []
    for i in range(Experience.objects.count()):
        ending_year = int(Experience.objects.all()[i].ending_date.split(' ')[2])
        joining_year = int(Experience.objects.all()[i].joining_date.split(' ')[2])
        if ( (ending_year >= year_passed ) and (joining_year <= year_passed )):
            user_names.append(Experience.objects.all()[i].object_name.name)
    return render(request, 'search_results/byyear.html',{'name':user_names, 'beta':year_passed})


def company(request , name):
    experiences = []
    for i in range(Experience.objects.count()):
        if (Experience.objects.all()[i].company_name == name):
            experiences.append(Experience.objects.all()[i])
    return render(request , 'contents/company_profile.html' , {'experiences' : experiences , 'name':name})