# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foll', '0013_auto_20160703_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinparty',
            name='date_accepted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
