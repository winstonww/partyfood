# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foll', '0005_auto_20160625_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinparty',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
