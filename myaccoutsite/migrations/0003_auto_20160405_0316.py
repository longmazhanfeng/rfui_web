# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccoutsite', '0002_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(),
        ),
    ]
