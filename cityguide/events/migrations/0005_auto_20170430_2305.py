# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170427_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='when',
            new_name='starts_at',
        ),
        migrations.AddField(
            model_name='event',
            name='age_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='ends_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]