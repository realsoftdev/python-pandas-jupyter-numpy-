# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 09:35
from __future__ import unicode_literals

import benchmark.utils.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0015_auto_20170809_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportrelease',
            name='payload',
        ),
        migrations.AddField(
            model_name='reportperiod',
            name='metadata',
            field=benchmark.utils.models.JSONField(blank=True, help_text='Metadata', null=True),
        ),
    ]
