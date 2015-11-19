# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20151118_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationClub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, blank=True)),
                ('hours', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ImageField(null=True, upload_to=core.models.upload_to_location, blank=True)),
                ('club', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Dance Club'), (2, b'Adult Entertainment')])),
                ('music', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Dance/Electronic'), (2, b'Karaoke'), (3, b'60s-70s-80s'), (4, b'Reggaeton'), (5, b'Salsa')])),
                ('bathrooms', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
                ('outdoor', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
                ('free_bar', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
                ('price', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')])),
                ('entrance_fee', models.CharField(max_length=4)),
                ('credit_card', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
            ],
        ),
        migrations.CreateModel(
            name='ReviewClub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('rating', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(to='core.LocationClub')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
