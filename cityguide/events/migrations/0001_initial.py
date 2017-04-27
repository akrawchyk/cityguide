# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateTimeField(blank=True)),
                ('location', models.CharField(max_length=64)),
                ('age_min', models.IntegerField(blank=True)),
            ],
        ),
    ]