# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20151119_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbar',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
