# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20151121_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationrestaurant',
            old_name='id',
            new_name='code',
        ),
    ]
