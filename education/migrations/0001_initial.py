# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=60)),
                ('District', models.CharField(max_length=46)),
                ('DistID', models.IntegerField()),
                ('SchoolID', models.IntegerField()),
                ('AcademicYear', models.IntegerField()),
                ('Subject', models.CharField(max_length=21)),
                ('Subgroup', models.CharField(max_length=32)),
                ('GradeLevel', models.CharField(max_length=3)),
                ('ParticipationRate2014to2015', models.FloatField()),
                ('PercentageMeetsORExceeds2014to2015', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=60)),
                ('District', models.CharField(max_length=46)),
                ('DistID', models.IntegerField()),
            ],
        ),
    ]
