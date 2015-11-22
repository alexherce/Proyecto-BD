# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151122_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationclub',
            name='average',
            field=models.FloatField(null=True, verbose_name=b'Average Ratings', blank=True),
        ),
    ]
