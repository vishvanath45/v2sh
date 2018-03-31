# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import SuperUser, Experience

# Create your views here.
def contactform(request):
	return render(request, 'superuser/contactform.html')

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

	ie_index = 0

	ie = []
	for i in range(5):
		ie.append(intershipexp())



	class jobexp(object):
		comp_name = str()
		joining_date = str()
		ending_date = str()
		role = str()
		present = False

	je_index = 0
	je = []
	for i in range(5):
		je.append(jobexp())


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

	print obj

	for i in range(no_of_obj_returned):
		# Considering if true than internship else job experience
		if (obj[i].internship_or_job == True):
			ie[ie_index].comp_name = obj[i].company_name;
			ie[ie_index].joining_date = obj[i].joining_date;
			ie[ie_index].ending_date = obj[i].ending_date;
			ie[ie_index].role = obj[i].role
			ie[ie_index].present = True
			ie_index += 1
		else:
			je[je_index].comp_name = obj[i].company_name;
			je[je_index].joining_date = obj[i].joining_date;
			je[je_index].ending_date = obj[i].ending_date;
			je[je_index].role = obj[i].role
			je[je_index].present = True
			je_index += 1

	
	# return render(request, 'superuser/superuserprofile.html',{'user':user})	
	return render(request, 'superuser/superuserprofile.html',{'user':user,'ie1':ie[0],'ie2':ie[1],'ie3':ie[2],'ie4':ie[3],'ie5':ie[4],'je1':je[0],'je2':je[1],'je3':je[2],'je4':je[3],'je5':je[4]})
	# return render(request, 'superuser/superuserprofile.html')
