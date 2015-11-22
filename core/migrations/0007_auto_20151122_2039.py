# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151122_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbar',
            name='average',
            field=models.FloatField(null=True, verbose_name=b'Average Ratings', blank=True),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='average',
            field=models.FloatField(null=True, verbose_name=b'Average Ratings', blank=True),
        ),
    ]
