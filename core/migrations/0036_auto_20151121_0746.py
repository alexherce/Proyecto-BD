# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_locationclub_avergage'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewclub',
            name='company_id',
            field=models.ForeignKey(related_name='company', default=datetime.datetime(2015, 11, 21, 7, 46, 23, 141772, tzinfo=utc), to='core.LocationClub'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='location',
            field=models.ForeignKey(related_name='location_id', to='core.LocationClub'),
        ),
    ]
