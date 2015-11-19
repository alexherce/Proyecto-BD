# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, blank=True)),
                ('hours', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ImageField(null=True, upload_to=core.models.upload_to_location, blank=True)),
                ('wifi', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')])),
                ('seating', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')])),
                ('outlets', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')])),
                ('bathrooms', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
                ('coffee', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Truck Stop'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')])),
                ('alcohol', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
                ('outdoor', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
                ('food', models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')])),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('rating', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(to='core.Location')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
