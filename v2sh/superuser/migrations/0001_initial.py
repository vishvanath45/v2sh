# Generated by Django 2.0.3 on 2018-04-06 16:20

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
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default=None, max_length=254, primary_key=True, serialize=False)),
                ('ph_no', models.TextField()),
                ('branch', models.CharField(default=None, max_length=50)),
                ('yog', models.IntegerField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='object_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuser.SuperUser'),
        ),
    ]
