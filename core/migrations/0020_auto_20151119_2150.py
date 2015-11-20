# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20151119_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbar',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='hours',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='image_file',
            field=models.ImageField(null=True, upload_to=core.models.upload_to_location),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='hours',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='image_file',
            field=models.ImageField(null=True, upload_to=core.models.upload_to_location),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
        ),
    ]
