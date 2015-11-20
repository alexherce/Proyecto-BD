# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151119_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationrestaurant',
            name='verified',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='bar',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Sports Bar'), (2, b'Beer Bar'), (3, b'Hookah Bar'), (4, b'Cocktail Bar'), (5, b'Shots Bar'), (6, b'Irish Pub'), (7, b'Hookah Bar'), (8, b'Other')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='image_file',
            field=models.ImageField(null=True, upload_to=core.models.upload_to_location, blank=True),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
    ]
