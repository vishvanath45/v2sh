# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from v2sh.environment import db, experience, superuser, user,session

def contactform(request):
	if(request.method == 'POST'):

		su_id = superuser.count()+1
		name = request.POST['name']
		branch = request.POST['branch']
		yog = int(request.POST['yog'])
		contact_no = request.POST['contact_no']
		email_id = request.POST['email_id']
		
		I_comp_name = request.POST.getlist('I_comp_name')
		I_role = request.POST.getlist('I_role')
		#  internship from = I_F
		#  internship to = I_T
		I_F_month = request.POST.getlist('I_F_month')
		I_F_year = request.POST.getlist('I_F_year')
		I_T_month = request.POST.getlist('I_T_month')
		I_T_year = request.POST.getlist('I_T_year')

		J_comp_name = request.POST.getlist('J_comp_name')
		J_role = request.POST.getlist('J_role')

		J_F_month = request.POST.getlist('J_F_month')
		J_F_year = request.POST.getlist('J_F_year')
		J_T_month = request.POST.getlist('J_T_month')
		J_T_year = request.POST.getlist('J_T_year')

		# For debugging purpose
		# print (name, branch, yog, contact_no, email_id)
		# print (I_comp_name, I_role, I_F_month , I_F_year,I_T_month,I_T_year)
		# print (J_comp_name, J_role, J_F_month , J_F_year,J_T_month,J_T_year)


		note = request.POST['note']

		obj_id = superuser.insert({'su_id' : su_id, 'name' : name, 'email' : email_id, \
			'ph_no' : contact_no, 'branch' : branch, 'yog' : yog, 'note' : note})

		for i in range(len(I_comp_name)):

			if(I_comp_name[i]!=''):
				exp = experience.insert({'company_name' : I_comp_name[i], \
					'joining_date' : str(I_F_month[i])+" "+ str(I_F_year[i]), \
					'ending_date' : str(I_T_month[i])+" "+ str(I_T_year[i]), \
					'role' : I_role[i], 'internship_or_job' : True, 'object_name' : obj_id})


		for i in range(len(J_comp_name)):

			if(J_comp_name[i]!=''):
				exp = experience.insert({'company_name' : J_comp_name[i], \
					'joining_date' : str(J_F_month[i])+" "+ str(J_F_year[i]), \
					'ending_date' : str(J_T_month[i])+" "+str(J_T_year[i]), \
					'role' : J_role[i], 'internship_or_job' : False, 'object_name' : obj_id})
				 


		return render(request, 'superuser/thankyou_form.html')

	return render(request, 'superuser/contactform.html')

#@login_required()
def superuserprofile(request,su_id):

#  I am currently taking user with su_id = 54, this value will be passed to this function, right now for testing I have taken 54, and populated fake exp in DB.
	user = superuser.find_one({'su_id':su_id})

	obj_id = user['_id']

	class intershipexp(object):
		comp_name = str()
		joining_date = str()
		ending_date = str()
		role = str()
		present = False

	ie = []
	ie_index = -1

	class jobexp(object):
		comp_name = str()
		joining_date = str()
		ending_date = str()
		role = str()
		present = False

	je = []
	je_index = -1

	for i in experience.find({'object_name':obj_id}):

		if (i['internship_or_job'] == True):
			ie.append(intershipexp())
			ie_index+=1
			ie[ie_index].comp_name = i['company_name']
			ie[ie_index].joining_date = i['joining_date']
			ie[ie_index].ending_date = i['ending_date']
			ie[ie_index].role = i['role']
			ie[ie_index].present = True
		else:
			je.append(jobexp())
			je_index += 1
			je[je_index].comp_name = i['company_name']
			je[je_index].joining_date = i['joining_date']
			je[je_index].ending_date = i['ending_date']
			je[je_index].role = i['role']
			je[je_index].present = True

	return render(request, 'superuser/superuserprofile.html',{'user':user,'ie':ie,'je':je})

def error(request):
    return render(request , 'error.html')

