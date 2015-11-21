# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20151121_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationclub',
            name='avergage',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
