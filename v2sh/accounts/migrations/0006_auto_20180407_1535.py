# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-07 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='active',
            new_name='is_active',
        ),
    ]
