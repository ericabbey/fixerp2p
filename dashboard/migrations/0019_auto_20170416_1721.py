# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-16 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20170415_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='securityA',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='securityQ',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
