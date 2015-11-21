# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationrestaurant',
            name='company_id',
            field=models.ForeignKey(default=datetime.datetime(2015, 11, 21, 1, 26, 17, 966873, tzinfo=utc), to='core.Company'),
            preserve_default=False,
        ),
    ]
