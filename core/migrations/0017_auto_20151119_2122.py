# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151119_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='verified',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
