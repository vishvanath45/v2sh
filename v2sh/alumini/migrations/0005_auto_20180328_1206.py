# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-28 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumini', '0004_auto_20180326_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='superuser',
            name='branch',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='superuser',
            name='yog',
            field=models.IntegerField(default=None),
        ),
    ]
