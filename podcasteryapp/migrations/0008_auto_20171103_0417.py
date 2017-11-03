# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasteryapp', '0007_auto_20171103_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='read',
            name='slot',
        ),
        migrations.AddField(
            model_name='slot',
            name='read',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='podcasteryapp.Read'),
        ),
    ]
