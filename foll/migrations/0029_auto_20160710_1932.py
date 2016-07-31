# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 23:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foll', '0028_auto_20160710_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foll.Food')),
                ('rated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopRatedFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foll.Food')),
            ],
        ),
        migrations.RemoveField(
            model_name='foodinparty',
            name='food',
        ),
        migrations.RemoveField(
            model_name='foodinparty',
            name='rated_by',
        ),
        migrations.DeleteModel(
            name='FoodinParty',
        ),
    ]
