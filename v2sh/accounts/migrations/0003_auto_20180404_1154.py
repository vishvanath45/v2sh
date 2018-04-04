# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-04 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180404_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pwd',
        ),
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Hasan', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='dadad', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
