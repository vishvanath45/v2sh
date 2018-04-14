import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'v2sh.settings')

import django

django.setup()

import random 

from superuser.models import SuperUser, Experience

from faker import Faker 

fake = Faker()

i = 0
for entry in range(200):

	# fake_suid = int(i)

	i += 1

	fake_name = fake.name()

	fake_email = fake.email()

	fake_phone = fake.phone_number()

	branch = ['IT', 'CSE', 'BT', 'ECE', 'CH','CE']

	fake_branch = random.choice(branch)

	yog = [2015, 2016, 2017, 2018,2019]

	fake_yog = random.choice(yog)

	fake_company = fake.company()

	fake_jd = fake.date()

	fake_ed = fake.date()

	role = ['SDE', 'Research', 'SDE2']

	fake_role = random.choice(role)

	intern_or_job = [True, False]

	fake_i_or_j = random.choice(intern_or_job)


	suprusrobj = SuperUser.objects.get_or_create( name = fake_name, email = fake_email,  ph_no =  fake_phone,  branch = fake_branch, yog= fake_yog)[0]


	exp_rec = Experience.objects.get_or_create(object_name = suprusrobj,company_name = fake_company, joining_date = fake_jd ,ending_date = fake_ed ,role = fake_role,internship_or_job = fake_i_or_j)[0]






