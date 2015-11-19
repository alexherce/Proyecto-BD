# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_location_locationbar_review_reviewbar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='location',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RenameField(
            model_name='locationbar',
            old_name='alcohol',
            new_name='credit_card',
        ),
        migrations.RemoveField(
            model_name='locationbar',
            name='coffee',
        ),
        migrations.RemoveField(
            model_name='locationbar',
            name='outlets',
        ),
        migrations.AddField(
            model_name='locationbar',
            name='bar',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Sports Bar'), (2, b'Beer Bar'), (3, b'Hookah Bar'), (4, b'Cocktail Bar'), (5, b'Shots Bar'), (6, b'Irish Pub'), (7, b'Hookah Bar'), (8, b'Other')]),
        ),
        migrations.AddField(
            model_name='locationrestaurant',
            name='credit_card',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
