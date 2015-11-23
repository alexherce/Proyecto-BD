# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0007_auto_20151122_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbar',
            name='food',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Food Type', choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee'), (12, b'Food Truck'), (13, b'Gourmet'), (14, b'Japanese')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='food',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Food Type', choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee'), (12, b'Food Truck'), (13, b'Gourmet'), (14, b'Japanese')]),
        ),
    ]
