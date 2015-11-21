# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20151121_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationbar',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='locationclub',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='locationrestaurant',
            name='company_name',
        ),
    ]
