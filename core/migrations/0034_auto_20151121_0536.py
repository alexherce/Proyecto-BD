# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20151121_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationbar',
            name='company_id',
            field=models.ForeignKey(default=datetime.datetime(2015, 11, 21, 5, 36, 28, 633395, tzinfo=utc), to='core.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationclub',
            name='company_id',
            field=models.ForeignKey(default=datetime.datetime(2015, 11, 21, 5, 36, 37, 528749, tzinfo=utc), to='core.Company'),
            preserve_default=False,
        ),
    ]
