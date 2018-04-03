from __future__ import unicode_literals

from django.db import models


class SuperUser(models.Model):
    su_id = models.IntegerField( primary_key = True)
    name = models.CharField(max_length=100)
    email = models.EmailField(default = None)
    ph_no = models.TextField()
    branch = models.CharField(max_length=50 , default= None)
    yog = models.IntegerField(default= None)
    # internship = models.TextField()

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    joining_date = models.DateField()
    # take data in YYYY-MM-DD
    ending_date = models.DateField()
    role = models.CharField(max_length=100)
    internship_or_job = models.BooleanField(default =True)
    object_name = models.ForeignKey(SuperUser,on_delete=models.CASCADE)
