# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import SuperUser,Experience
# Register your models here.

admin.site.register(SuperUser)

admin.site.register(Experience)
