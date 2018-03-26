# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    password = models.Field()

class SuperUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key = True)
    ph_no = models.TextField()
    # internship = models.TextField()

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    joining_date = models.DateField()
    # take data in YYYY-MM-DD
    ending_date = models.DateField()
    role = models.CharField(max_length=100)
    internship_or_job = models.BooleanField(default = True)
    object_name = models.ForeignKey(SuperUser)

# Create your models here.
