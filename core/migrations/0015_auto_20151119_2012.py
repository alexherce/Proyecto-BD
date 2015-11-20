# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20151119_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='verified',
            field=models.BooleanField(default=0, editable=False, choices=[(0, b'No'), (1, b'Yes')]),
        ),
    ]
