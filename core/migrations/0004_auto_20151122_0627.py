# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151122_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationbar',
            name='average',
            field=models.IntegerField(null=True, verbose_name=b'Average Ratings', blank=True),
        ),
        migrations.AddField(
            model_name='locationrestaurant',
            name='average',
            field=models.IntegerField(null=True, verbose_name=b'Average Ratings', blank=True),
        ),
    ]
