# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foll', '0017_auto_20160705_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 0, 23, 59, 783837)),
        ),
    ]
