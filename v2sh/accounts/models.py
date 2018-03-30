# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    pwd = models.CharField(max_length=100)