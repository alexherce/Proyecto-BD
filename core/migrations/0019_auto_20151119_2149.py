# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20151119_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='hours',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
        ),
    ]
