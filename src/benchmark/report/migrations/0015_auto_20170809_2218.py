# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0014_auto_20170809_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportperiod',
            options={'ordering': ['-created'], 'verbose_name': 'Report Period', 'verbose_name_plural': 'Report Periods'},
        ),
        migrations.AddField(
            model_name='reportperiod',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Date when object was created. Should be assigned automatically only.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportperiod',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date when object was modified. Should be assigned automatically only.'),
        ),
        migrations.AddField(
            model_name='reportupload',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date when object was modified. Should be assigned automatically only.'),
        ),
    ]
