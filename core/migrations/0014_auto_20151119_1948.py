# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20151119_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
