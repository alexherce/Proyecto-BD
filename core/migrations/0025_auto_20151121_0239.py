# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20151121_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationbar',
            name='id',
        ),
        migrations.RemoveField(
            model_name='locationclub',
            name='id',
        ),
        migrations.AddField(
            model_name='locationbar',
            name='code',
            field=models.CharField(default=core.models.make_uuid, max_length=36, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='locationclub',
            name='code',
            field=models.CharField(default=core.models.make_uuid, max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
