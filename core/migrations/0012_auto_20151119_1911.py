# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20151119_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationbar',
            name='verified',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='locationclub',
            name='verified',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
