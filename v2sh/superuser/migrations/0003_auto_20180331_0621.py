# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-31 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0002_auto_20180330_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuser',
            name='su_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
