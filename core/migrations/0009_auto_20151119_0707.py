# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151119_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbar',
            name='bar',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Sports Bar'), (2, b'Beer Bar'), (3, b'Hookah Bar'), (4, b'Cocktail Bar'), (5, b'Shots Bar'), (6, b'Irish Pub'), (7, b'Sushi Bar'), (8, b'Other')]),
        ),
    ]
