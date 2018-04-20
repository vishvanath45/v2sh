from __future__ import unicode_literals

from django.db import models

import uuid

class Feedback(models.Model):
    note = models.TextField(max_length=2000)
    rating = models.IntegerField(default=None)
    ask = models.CharField(max_length=50 , default= None)

class report(models.Model):
    email = models.EmailField( default = None )
    issuetype = models.CharField( max_length=100, default=None )
    details = models.TextField(max_length=2000)
    device = models.CharField(max_length=50, default =None)
