# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20151121_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='code',
            field=models.CharField(default=core.models.make_uuid, max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
