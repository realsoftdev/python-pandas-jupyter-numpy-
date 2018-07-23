# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 14:04
from __future__ import unicode_literals

import benchmark.utils.models
from django.db import migrations
import queued_storage.backends


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_auto_20170726_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportupload',
            name='file',
            field=benchmark.utils.models.CSVFileField(help_text='File storage', storage=queued_storage.backends.QueuedStorage(local='django.core.files.storage.FileSystemStorage', local_options={'location': 'data-science/data/raw'}, remote='storages.backends.s3boto3.S3Boto3Storage', remote_options={'location': 'data-science/data/raw'}), upload_to=benchmark.utils.models.cvsfield_upload_to, validators=[benchmark.utils.models.validate_upload_file_extension]),
        ),
        migrations.DeleteModel(
            name='FileStorage',
        ),
    ]
