import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'v2sh.settings')

import django

django.setup()

import random

from superuser.models import SuperUser, Experience

from faker import Faker

fake = Faker()

i = 0

for entry in range(90):

    # fake_suid = int(i)
    su_id = SuperUser.objects.count() + 1

    i += 1

    fake_name = fake.name()

    fake_email = fake.email()

    fake_phone = fake.phone_number()

    branch = ['IT', 'CSE', 'BT', 'ECE', 'CH', 'CE', 'ME', 'MME']

    fake_branch = random.choice(branch)

    yog = [2015, 2016, 2017, 2018, 2019]

    fake_yog = random.choice(yog)

    suprusrobj = \
    SuperUser.objects.get_or_create(su_id=su_id, name=fake_name, email=fake_email, ph_no=fake_phone, branch=fake_branch,
                                    yog=fake_yog)[0]

    for j in range(3):
        fake_company = fake.company()

        month = ['JAN', 'FEB', 'MAR', 'JUN', 'DEC', 'AUG']

        year = ['2011', '2012', '2013', '2014', '2015', '2015', '2016', '2017', '2018', '2019']

        fake_jd = random.choice(month) + "  " + random.choice(year)

        fake_ed = random.choice(month) + "  " + random.choice(year)

        role = ['SDE I', 'Research', 'SDE II', 'SDE III']

        fake_role = random.choice(role)

        intern_or_job = [True, False]

        fake_i_or_j = random.choice(intern_or_job)

        exp_rec = \
        Experience.objects.get_or_create(object_name=suprusrobj, company_name=fake_company, joining_date=fake_jd,
                                         ending_date=fake_ed, role=fake_role, internship_or_job=fake_i_or_j)[0]






