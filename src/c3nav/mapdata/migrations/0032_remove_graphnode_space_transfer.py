# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0031_auto_20170805_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphnode',
            name='space_transfer',
        ),
    ]