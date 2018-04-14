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
		name = request.POST['name']
		branch = request.POST['branch']
		yog = request.POST['yog']
		contact_no = request.POST['contact_no']
		email_id = request.POST['email_id']
		
		I_comp_name = request.POST.getlist('I_comp_name')
		I_role = request.POST.getlist('I_role')
		I_F_month = request.POST.getlist('I_F_month')
		I_T_month = request.POST.getlist('I_T_month')

		J_comp_name = request.POST.getlist('J_comp_name')
		J_role = request.POST.getlist('J_role')
		J_F_month = request.POST.getlist('J_F_month')
		J_T_month = request.POST.getlist('J_T_month')

		note = request.POST['note']

		User = SuperUser.objects.create(name = name, email = email_id, ph_no = contact_no, branch = branch,yog = yog,note =note )

		for i in range(len(I_comp_name)):

			if(I_comp_name[i]!=''):
				exp = Experience.objects.create(company_name = I_comp_name[i], joining_date = I_F_month[i], ending_date = I_T_month[i], role = I_role[i], internship_or_job = True, object_name = User)


		for i in range(len(J_comp_name)):

			if(J_comp_name[i]!=''):
				exp = Experience.objects.create(company_name = J_comp_name[i], joining_date = J_F_month[i], ending_date = J_T_month[i], role = J_role[i], internship_or_job = False, object_name = User)
				 


		return HttpResponse("Thanks for filling the form")
		# try:
		# 	pkp = request.POST.getlist('Cname')
		# 	print (pkp)
		# except :
		# 	pkp = 1
		

	return render(request, 'superuser/contactform.html')
# @login_required()
def superuserprofile(request):

#  I am currently taking user with su_id = 54, this value will be passed to this function, right now for testing I have taken 54, and populated fake exp in DB.

	for i in range(SuperUser.objects.count()):
		if (SuperUser.objects.all()[i].su_id == 54):
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


	no_of_obj_returned = Experience.objects.filter(object_name = user).count()

	obj = Experience.objects.filter(object_name = user)


	for i in range(no_of_obj_returned):
		# Considering if true than internship else job experience
		if (obj[i].internship_or_job == True):
			ie.append(intershipexp())
			ie_index+=1
			ie[ie_index].comp_name = obj[i].company_name;
			ie[ie_index].joining_date = obj[i].joining_date;
			ie[ie_index].ending_date = obj[i].ending_date;
			ie[ie_index].role = obj[i].role
			ie[ie_index].present = True
			ie_index += 1
		else:
			je.append(intershipexp())
			je_index += 1
			je[je_index].comp_name = obj[i].company_name;
			je[je_index].joining_date = obj[i].joining_date;
			je[je_index].ending_date = obj[i].ending_date;
			je[je_index].role = obj[i].role
			je[je_index].present = True
			je_index += 1

	
	# return render(request, 'superuser/superuserprofile.html',{'user':user})	
	return render(request, 'superuser/superuserprofile.html',{'user':user,'ie':ie,'je':je})
	# return render(request, 'superuser/superuserprofile.html')


def search_by_year_result(year,request):
    return render(request , 'error.html')

	# for i in range(SuperUser.objects.count()):
	# 	end_date = int(SuperUser.objects.all()[i].ending_date.split('-')[0])
	# 	start_date = int(SuperUser.objects.all()[i].joining_date.split('-')[0])

	# 	if( (end_date == year) or (start_date == year)):
	# 		user = SuperUser.objects.all()[i]











def error(request):
    return render(request , 'error.html')
