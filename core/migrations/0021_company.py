# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20151119_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(default=core.models.make_uuid, max_length=36, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
