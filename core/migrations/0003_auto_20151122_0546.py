# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151121_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationclub',
            old_name='avergage',
            new_name='average',
        ),
    ]
