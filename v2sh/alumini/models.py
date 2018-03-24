# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    password = models.Field()


class SuperUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    ph_no = models.TextField()
    internship = models.TextField()
# Create your models here.
