# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-08 18:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20170424_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='support',
            name='user',
        ),
        migrations.DeleteModel(
            name='Support',
        ),
    ]
