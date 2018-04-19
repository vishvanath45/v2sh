# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from .models import SuperUser, Experience
# Create your views here.
from django.http import HttpResponse

def contactform(request):
	if(request.method == 'POST'):

		su_id = SuperUser.objects.count()+1
		name = request.POST['name']
		branch = request.POST['branch']
		yog = request.POST['yog']
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
		# print su_id, name, branch, yog, contact_no, email_id
		# print I_comp_name, I_role, I_F_month , I_F_year,I_T_month,I_T_year
		# print J_comp_name, J_role, J_F_month , J_F_year,J_T_month,J_T_year


		note = request.POST['note']

		# print note

		User = SuperUser.objects.create(su_id = su_id, name = name, email = email_id, ph_no = contact_no, branch = branch,yog = yog,note =note )

		for i in range(len(I_comp_name)):

			if(I_comp_name[i]!=''):
				exp = Experience.objects.create(company_name = I_comp_name[i], joining_date = str(I_F_month[i])+" "+ str(I_F_year[i]), ending_date = str(I_T_month[i])+" "+ str(I_T_year[i]), role = I_role[i], internship_or_job = True, object_name = User)


		for i in range(len(J_comp_name)):

			if(J_comp_name[i]!=''):
				exp = Experience.objects.create(company_name = J_comp_name[i], joining_date = str(J_F_month[i])+" "+ str(J_F_year[i]), ending_date = str(J_T_month[i])+" "+str(J_T_year[i]), role = J_role[i], internship_or_job = False, object_name = User)
				 


		return HttpResponse("Thanks for filling the form")
		# try:
		# 	pkp = request.POST.getlist('Cname')
		# 	print (pkp)
		# except :
		# 	pkp = 1
		

	return render(request, 'superuser/contactform.html')
# @login_required()




def superuserprofile(request,su_id):

#  I am currently taking user with su_id = 54, this value will be passed to this function, right now for testing I have taken 54, and populated fake exp in DB.
	
	
	for i in range(SuperUser.objects.count()):
		if (SuperUser.objects.all()[i].su_id == int(su_id)):
			user = SuperUser.objects.all()[i]
			


	# I am considering at max 5 internship and 5 Job exp, we can make more, easily scalable.

	class intershipexp(object):
		comp_name = str()
		joining_date = str()
		ending_date = str()
		role = str()
		present = False

	ie_index = -1

	ie = []
	# for i in range(5):
	# 	ie.append(intershipexp())



	class jobexp(object):
		comp_name = str()
		joining_date = str()
		ending_date = str()
		role = str()
		present = False

	je_index = -1
	je = []
	# for i in range(5):
	# 	je.append(jobexp())


	'''
	@vishvanath45 -- 
	exp = Experience.objects.get(object_name = user)
	earlier we used to use get() to find entries with object user,
	but get() only expects single object to be returned, but suppose 
	Experience might have different rows for same user.
	so multiple objects need to be returned.

	So we will use filter instead, 
	See discussion here - https://stackoverflow.com/questions/7983946/django-multipleobjectsreturned
	'''


	# no_of_obj_returned = Experience.objects.filter(object_name = user).count()

	for i in Experience.objects.all():

		if (i.object_name ==user and i.internship_or_job == True):
			ie.append(intershipexp())
			ie_index+=1
			ie[ie_index].comp_name = i.company_name;
			ie[ie_index].joining_date = i.joining_date;
			ie[ie_index].ending_date = i.ending_date;
			ie[ie_index].role = i.role
			ie[ie_index].present = True
			# ie_index += 1
		elif(i.object_name ==user and i.internship_or_job == False):

			je.append(jobexp())
			je_index += 1
			je[je_index].comp_name = i.company_name;
			je[je_index].joining_date = i.joining_date;
			je[je_index].ending_date = i.ending_date;
			je[je_index].role = i.role
			je[je_index].present = True


	
	return render(request, 'superuser/superuserprofile.html',{'user':user,'ie':ie,'je':je})

def error(request):
    return render(request , 'error.html')

