# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(default=b'a956e-QARFCDstd9IG6WsQ', verbose_name=b'Client Company', to='core.Company'),
        ),
    ]
