# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151119_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='image_file',
            field=models.ImageField(upload_to=core.models.upload_to_location, blank=True),
        ),
    ]
