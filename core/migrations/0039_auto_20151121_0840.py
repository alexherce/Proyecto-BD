# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20151121_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': (('can_publish', 'Can Publish'),)},
        ),
    ]
