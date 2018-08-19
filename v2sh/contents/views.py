# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from superuser.models import SuperUser, Experience

from django.contrib.auth.decorators import login_required

from django.urls import reverse

from django.contrib.auth import get_user_model

from v2sh.environment import db, experience, superuser, user

# Create your views here.
User = get_user_model()

# @login_required()
def home(request):
    return render(request, 'contents/home.html')

# @login_required()
def aboutus(request):
    return render(request, 'contents/aboutus.html')

# @login_required()
def reportissue(request):
    if(request.method=="POST"):
        mail=request.POST['mail']
        issue=request.POST['issue']
        details=request.POST['details']
        device=request.POST.getlist('device')
        # print(mail)
        # print(issue)
        # print(device)
        # print(details)
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

#@login_required()
def bycompany(request,alpha):

    alpha1=alpha.upper()
    names=[]    
    number_of_people=[]
    job_count_pairs = []
    myname = {}

    # for i in range(Experience.objects.count()):
    #     if(Experience.objects.all()[i].company_name[0]==alpha or Experience.objects.all()[i].company_name[0]==alpha1):
    #         comp_name = Experience.objects.all()[i].company_name
    #         if comp_name in myname:
    #             continue
    #         names.append(comp_name)
    #         myname[comp_name]=1

    for i in experience.find({'company_name':{'$regex':str('^'+alpha),'$options' : 'i'}}):
        comp_name = i['company_name']
        if comp_name in myname:
            continue
        names.append(comp_name)
        myname[comp_name] = 1

    for i in names:
        cnt = experience.find({'company_name':i}).count()
        number_of_people.append(cnt)
    # for i in names:
    #     cnt=0
    #     for j in range(Experience.objects.count()):
    #         if(str(i)== str(Experience.objects.all()[j].company_name)):
    #             cnt+=1
    #     number_of_people.append(cnt)
    for i in range(len(names)):
        job_count_pairs.append((names[i], number_of_people[i]))

    return render(request,'search_results/bycompany.html',{'names':job_count_pairs,'alpha':alpha1})

#@login_required()
# def byyear(request,beta):
#     year_passed = int(beta)
#     map_user_names = {}
#     user_names = []
#     for i in range(Experience.objects.count()):
#         ending_year = int(Experience.objects.all()[i].ending_date.split(' ')[2])
#         joining_year = int(Experience.objects.all()[i].joining_date.split(' ')[2])
#         if ( (ending_year >= year_passed ) and (joining_year <= year_passed )):
#             person_name = Experience.objects.all()[i].object_name
#             if person_name in map_user_names:
#                 continue
#             user_names.append(person_name)
#             map_user_names[person_name] = 1
#     return render(request, 'search_results/byyear.html',{'name':user_names, 'beta':year_passed})
def byyear(request,beta):
    year_passed = int(beta)
    print(year_passed)
    print("\n----\n")
    map_user_names = {}
    user_names = []
    for i in experience.find({}):
        ending_year = int(i['ending_date'].split(' ')[-1])
        joining_year = int(i['joining_date'].split(' ')[-1])
        print(ending_year, joining_year, year_passed)
        if ( (ending_year >= year_passed ) and (joining_year <= year_passed )):
            person = superuser.find_one({'_id':i['object_name']})
            person_name = person['name']
            if person_name in map_user_names:
                continue
            user_names.append(person_name)
            map_user_names[person_name] = 1
    print(user_names)
    return render(request, 'search_results/byyear.html',{'name':user_names, 'beta':year_passed})


# To do work for @rishi07

#@login_required()
def company(request , name):
    # print(name)
    experiences = []
    for i in experience.find({'company_name':name}):
        experiences.append(i)
    return render(request , 'contents/company_profile.html' , {'experiences' : experiences , 'name':name})

#@login_required
def byname(request , gamma):
    gamma1 = gamma.upper()
    names = []
    User = SuperUser.objects.all()
    for i in range(SuperUser.objects.count()):
        if SuperUser.objects.all()[i].name[0] == gamma or SuperUser.objects.all()[i].name[0] == gamma1:
            names.append(SuperUser.objects.all()[i])

    return render(request , 'search_results/byname.html' , {'names' : names , 'alpha' : gamma})