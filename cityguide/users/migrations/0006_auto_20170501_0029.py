# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170427_0318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='group_person_count',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(related_name='user_interests', to='interests.Interest'),
        ),
    ]
