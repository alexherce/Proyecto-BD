# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151118_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationclub',
            name='entrance_fee',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'$1-$50'), (2, b'$50-$100'), (3, b'$100-$200'), (4, b'$200-$300'), (5, b'$300-$400'), (6, b'$400-$500'), (7, b'$500+')]),
        ),
    ]
