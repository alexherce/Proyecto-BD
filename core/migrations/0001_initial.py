# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import geoposition.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID')),
                ('name', models.CharField(max_length=300, verbose_name=b'Company Name')),
            ],
            options={
                'permissions': (('can_publish', 'Can Publish'),),
            },
        ),
        migrations.CreateModel(
            name='LocationBar',
            fields=[
                ('code', models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID')),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('verified', models.BooleanField(default=False, verbose_name=b'Verified Location')),
                ('description', models.TextField(null=True, verbose_name=b'Description')),
                ('address', models.TextField(null=True, verbose_name=b'Address')),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Map Position')),
                ('hours', models.TextField(null=True, verbose_name=b'Service Hours')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted')),
                ('image_file', models.ImageField(upload_to=core.models.upload_to_location, null=True, verbose_name=b'Picture')),
                ('bar', models.IntegerField(blank=True, null=True, verbose_name=b'Bar Category', choices=[(0, b'None'), (1, b'Sports Bar'), (2, b'Beer Bar'), (3, b'Hookah Bar'), (4, b'Cocktail Bar'), (5, b'Shots Bar'), (6, b'Irish Pub'), (7, b'Hookah Bar'), (8, b'Other')])),
                ('food', models.IntegerField(blank=True, null=True, verbose_name=b'Food Type', choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee')])),
                ('wifi', models.IntegerField(blank=True, null=True, verbose_name=b'Wi-Fi Connection', choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')])),
                ('bathrooms', models.IntegerField(blank=True, null=True, verbose_name=b'Bathrooms', choices=[(0, b'No'), (1, b'Yes')])),
                ('outdoor', models.IntegerField(blank=True, null=True, verbose_name=b'Outdoor Seating', choices=[(0, b'No'), (1, b'Yes')])),
                ('price', models.IntegerField(blank=True, null=True, verbose_name=b'Price Category', choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')])),
                ('credit_card', models.IntegerField(blank=True, null=True, verbose_name=b'Accepts Credit Cards', choices=[(0, b'No'), (1, b'Yes')])),
                ('company_id', models.ForeignKey(verbose_name=b'Company ID', to='core.Company')),
            ],
        ),
        migrations.CreateModel(
            name='LocationClub',
            fields=[
                ('code', models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID')),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('verified', models.BooleanField(default=False, verbose_name=b'Verified Location')),
                ('description', models.TextField(null=True, verbose_name=b'Description')),
                ('address', models.TextField(null=True, verbose_name=b'Address')),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Map Position')),
                ('hours', models.TextField(null=True, verbose_name=b'Service Hours')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted')),
                ('image_file', models.ImageField(upload_to=core.models.upload_to_location, null=True, verbose_name=b'Picture')),
                ('club', models.IntegerField(blank=True, null=True, verbose_name=b'Club Type', choices=[(0, b'None'), (1, b'Dance Club'), (2, b'Adult Entertainment')])),
                ('music', models.IntegerField(blank=True, null=True, verbose_name=b'Music Type', choices=[(0, b'None'), (1, b'Dance/Electronic'), (2, b'Karaoke'), (3, b'60s-70s-80s'), (4, b'Reggaeton'), (5, b'Salsa')])),
                ('bathrooms', models.IntegerField(blank=True, null=True, verbose_name=b'Bathrooms', choices=[(0, b'No'), (1, b'Yes')])),
                ('outdoor', models.IntegerField(blank=True, null=True, verbose_name=b'Outdoor Area', choices=[(0, b'No'), (1, b'Yes')])),
                ('free_bar', models.IntegerField(blank=True, null=True, verbose_name=b'Free Bar', choices=[(0, b'No'), (1, b'Yes')])),
                ('price', models.IntegerField(blank=True, null=True, verbose_name=b'Price Category', choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')])),
                ('entrance_fee', models.IntegerField(blank=True, null=True, verbose_name=b'Entrance Fee', choices=[(0, b'None'), (1, b'$1-$50'), (2, b'$50-$100'), (3, b'$100-$200'), (4, b'$200-$300'), (5, b'$300-$400'), (6, b'$400-$500'), (7, b'$500+')])),
                ('credit_card', models.IntegerField(blank=True, null=True, verbose_name=b'Accepts Credit Cards', choices=[(0, b'No'), (1, b'Yes')])),
                ('avergage', models.IntegerField(null=True, verbose_name=b'Average Ratings', blank=True)),
                ('company_id', models.ForeignKey(verbose_name=b'Company ID', to='core.Company')),
            ],
        ),
        migrations.CreateModel(
            name='LocationRestaurant',
            fields=[
                ('code', models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID')),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('verified', models.BooleanField(default=False, verbose_name=b'Verified Location')),
                ('description', models.TextField(null=True, verbose_name=b'Description')),
                ('address', models.TextField(null=True, verbose_name=b'Address')),
                ('position', geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Map Position')),
                ('hours', models.TextField(null=True, verbose_name=b'Service Hours')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted')),
                ('image_file', models.ImageField(upload_to=core.models.upload_to_location, verbose_name=b'Picture')),
                ('food', models.IntegerField(blank=True, null=True, verbose_name=b'Food Type', choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee')])),
                ('wifi', models.IntegerField(blank=True, null=True, verbose_name=b'Wi-Fi Connection', choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')])),
                ('outlets', models.IntegerField(blank=True, null=True, verbose_name=b'Power Outlets', choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')])),
                ('bathrooms', models.IntegerField(blank=True, null=True, verbose_name=b'Bathrooms', choices=[(0, b'No'), (1, b'Yes')])),
                ('coffee', models.IntegerField(blank=True, null=True, verbose_name=b'Coffee', choices=[(0, b'None'), (1, b'Truck Stop'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')])),
                ('alcohol', models.IntegerField(blank=True, null=True, verbose_name=b'Alcohol', choices=[(0, b'No'), (1, b'Yes')])),
                ('outdoor', models.IntegerField(blank=True, null=True, verbose_name=b'Outdoor Seating', choices=[(0, b'No'), (1, b'Yes')])),
                ('price', models.IntegerField(blank=True, null=True, verbose_name=b'Price Category', choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')])),
                ('credit_card', models.IntegerField(blank=True, null=True, verbose_name=b'Accepts Credit Cards', choices=[(0, b'No'), (1, b'Yes')])),
                ('company_id', models.ForeignKey(verbose_name=b'Company ID', to='core.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewBar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=300, null=True, verbose_name=b'Location Name', blank=True)),
                ('company_id', models.CharField(max_length=36, null=True, verbose_name=b'Company Name', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Comments')),
                ('rating', models.IntegerField(null=True, verbose_name=b'Rating', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted')),
                ('location', models.ForeignKey(verbose_name=b'Location ID', to='core.LocationBar')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewClub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=300, null=True, verbose_name=b'Location Name', blank=True)),
                ('company_id', models.CharField(max_length=36, null=True, verbose_name=b'Company Name', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Comments')),
                ('rating', models.IntegerField(null=True, verbose_name=b'Rating', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted')),
                ('location', models.ForeignKey(verbose_name=b'Location ID', to='core.LocationClub')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRestaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=300, null=True, verbose_name=b'Location Name', blank=True)),
                ('company_id', models.CharField(max_length=36, null=True, verbose_name=b'Company Name', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Comments')),
                ('rating', models.IntegerField(null=True, verbose_name=b'Rating', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted')),
                ('location', models.ForeignKey(verbose_name=b'Location ID', to='core.LocationRestaurant')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(default=b'4kxtZo71SYyAY7fcGrMq1Q', verbose_name=b'Client Company', to='core.Company'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
