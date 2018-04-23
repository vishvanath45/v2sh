# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('joining_date', models.CharField(max_length=100)),
                ('ending_date', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('internship_or_job', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('su_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('ph_no', models.TextField()),
                ('branch', models.CharField(default=None, max_length=50)),
                ('yog', models.IntegerField(default=None)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='object_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuser.SuperUser'),
        ),
    ]
