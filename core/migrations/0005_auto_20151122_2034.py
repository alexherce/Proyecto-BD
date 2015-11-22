# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151122_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationclub',
            name='average',
            field=models.DecimalField(null=True, verbose_name=b'Average Ratings', max_digits=2, decimal_places=1, blank=True),
        ),
    ]
