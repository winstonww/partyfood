# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 20:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foll', '0021_auto_20160707_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='desc',
        ),
        migrations.AlterField(
            model_name='party',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 16, 19, 58, 297464)),
        ),
    ]
