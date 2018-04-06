from __future__ import unicode_literals

from django.db import models

import uuid

class SuperUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( default = None , primary_key = True)
    ph_no = models.TextField()
    branch = models.CharField(max_length=50 , default= None)
    yog = models.IntegerField(default= None)
    # internship = models.TextField()

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    # take data in YYYY-MM-DD
    ending_date = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    internship_or_job = models.BooleanField(default =True)
    object_name = models.ForeignKey(SuperUser,on_delete=models.CASCADE)
