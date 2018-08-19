from __future__ import unicode_literals

from django.db import models
from mongoengine import *
import uuid


class SuperUser(models.Model):
    su_id = models.IntegerField( default = 0, primary_key = True )
    name = models.CharField(max_length=100)
    email = models.EmailField( default = None )
    ph_no = models.TextField()
    branch = models.CharField(max_length=50 , default= None)
    yog = models.IntegerField(default= None)
    note = models.CharField(max_length=500)
    # internship = models.TextField()

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    # take data in YYYY-MM-DD
    ending_date = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    # This will be true if internship, False if JOB
    internship_or_job = models.BooleanField(default =True)
    object_name = models.ForeignKey(SuperUser,on_delete=models.CASCADE)
