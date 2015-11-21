# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20151121_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='locationrestaurant',
            old_name='company_id',
            new_name='company',
        ),
    ]
