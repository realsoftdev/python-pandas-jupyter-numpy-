# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_auto_20170727_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportrelease',
            name='csv_fields',
            field=models.CharField(blank=True, help_text='CSV fields', max_length=250),
        ),
        migrations.AddField(
            model_name='reportrelease',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date when object was modified. Should be assigned automatically only.'),
        ),
        migrations.AlterField(
            model_name='reportrelease',
            name='report',
            field=models.OneToOneField(help_text='Report upload', null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportUpload'),
        ),
        migrations.AlterField(
            model_name='reportrelease',
            name='user',
            field=models.ForeignKey(help_text='Owner account', null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account'),
        ),
    ]
