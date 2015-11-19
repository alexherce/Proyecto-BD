# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151119_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbar',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendor'), (11, b'Coffee Shop'), (12, b'American')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendor'), (11, b'Coffee Shop'), (12, b'American')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
    ]
