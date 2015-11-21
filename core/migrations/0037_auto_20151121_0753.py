# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20151121_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewclub',
            name='company_id',
            field=models.CharField(max_length=36, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='rating',
            field=models.IntegerField(null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
    ]
