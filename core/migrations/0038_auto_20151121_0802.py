# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20151121_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewclub',
            name='location_name',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='location',
            field=models.ForeignKey(to='core.LocationClub'),
        ),
    ]
