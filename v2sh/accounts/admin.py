# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth import get_user_model

User = get_user_model()
# from .models import user
# Register your models here.
admin.site.register(User)