# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='company_id',
            field=models.ForeignKey(default=b'4kxtZo71SYyAY7fcGrMq1Q', to='core.Company'),
        ),
    ]
