# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superuser',
            name='id',
        ),
        migrations.AddField(
            model_name='superuser',
            name='su_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
