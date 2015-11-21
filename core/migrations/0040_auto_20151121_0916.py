# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20151121_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationbar',
            name='company_name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Company Name', blank=True),
        ),
        migrations.AddField(
            model_name='locationclub',
            name='company_name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Company Name', blank=True),
        ),
        migrations.AddField(
            model_name='locationrestaurant',
            name='company_name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Company Name', blank=True),
        ),
        migrations.AddField(
            model_name='reviewbar',
            name='company_id',
            field=models.CharField(max_length=36, null=True, verbose_name=b'Company Name', blank=True),
        ),
        migrations.AddField(
            model_name='reviewbar',
            name='location_name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Location Name', blank=True),
        ),
        migrations.AddField(
            model_name='reviewrestaurant',
            name='company_id',
            field=models.CharField(max_length=36, null=True, verbose_name=b'Company Name', blank=True),
        ),
        migrations.AddField(
            model_name='reviewrestaurant',
            name='location_name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Location Name', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(default=b'4kxtZo71SYyAY7fcGrMq1Q', verbose_name=b'Client Company', to='core.Company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=300, verbose_name=b'Company Name'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='address',
            field=models.TextField(null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='bar',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Bar Category', choices=[(0, b'None'), (1, b'Sports Bar'), (2, b'Beer Bar'), (3, b'Hookah Bar'), (4, b'Cocktail Bar'), (5, b'Shots Bar'), (6, b'Irish Pub'), (7, b'Hookah Bar'), (8, b'Other')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Bathrooms', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='code',
            field=models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='company_id',
            field=models.ForeignKey(verbose_name=b'Company ID', to='core.Company'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='credit_card',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Accepts Credit Cards', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='food',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Food Type', choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='hours',
            field=models.TextField(null=True, verbose_name=b'Service Hours'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='image_file',
            field=models.ImageField(upload_to=core.models.upload_to_location, null=True, verbose_name=b'Picture'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Outdoor Seating', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Map Position'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Price Category', choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')]),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='title',
            field=models.CharField(max_length=300, verbose_name=b'Title'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified Location'),
        ),
        migrations.AlterField(
            model_name='locationbar',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Wi-Fi Connection', choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='address',
            field=models.TextField(null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='avergage',
            field=models.IntegerField(null=True, verbose_name=b'Average Ratings', blank=True),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Bathrooms', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='club',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Club Type', choices=[(0, b'None'), (1, b'Dance Club'), (2, b'Adult Entertainment')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='code',
            field=models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='company_id',
            field=models.ForeignKey(verbose_name=b'Company ID', to='core.Company'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='credit_card',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Accepts Credit Cards', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='entrance_fee',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Entrance Fee', choices=[(0, b'None'), (1, b'$1-$50'), (2, b'$50-$100'), (3, b'$100-$200'), (4, b'$200-$300'), (5, b'$300-$400'), (6, b'$400-$500'), (7, b'$500+')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='free_bar',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Free Bar', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='hours',
            field=models.TextField(null=True, verbose_name=b'Service Hours'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='image_file',
            field=models.ImageField(upload_to=core.models.upload_to_location, null=True, verbose_name=b'Picture'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='music',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Music Type', choices=[(0, b'None'), (1, b'Dance/Electronic'), (2, b'Karaoke'), (3, b'60s-70s-80s'), (4, b'Reggaeton'), (5, b'Salsa')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Outdoor Area', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Map Position'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Price Category', choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')]),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='title',
            field=models.CharField(max_length=300, verbose_name=b'Title'),
        ),
        migrations.AlterField(
            model_name='locationclub',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified Location'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='address',
            field=models.TextField(null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Alcohol', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Bathrooms', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='code',
            field=models.CharField(primary_key=True, default=core.models.make_uuid, serialize=False, editable=False, max_length=36, verbose_name=b'ID'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='coffee',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Coffee', choices=[(0, b'None'), (1, b'Truck Stop'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='company_id',
            field=models.ForeignKey(verbose_name=b'Company ID', to='core.Company'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='credit_card',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Accepts Credit Cards', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='food',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Food Type', choices=[(0, b'None'), (1, b'Fast Food'), (2, b'Chinese'), (3, b'Sushi'), (4, b'Mexican'), (5, b'Argentine'), (6, b'Vegetarian/Vegan'), (7, b'Italian'), (8, b'Brazilian'), (9, b'Seafood'), (10, b'Street vendors'), (11, b'Coffee')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='hours',
            field=models.TextField(null=True, verbose_name=b'Service Hours'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='image_file',
            field=models.ImageField(upload_to=core.models.upload_to_location, verbose_name=b'Picture'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Outdoor Seating', choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='outlets',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Power Outlets', choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Map Position'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Price Category', choices=[(0, b'None'), (1, b'$'), (2, b'$$'), (3, b'$$$')]),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='title',
            field=models.CharField(max_length=300, verbose_name=b'Title'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified Location'),
        ),
        migrations.AlterField(
            model_name='locationrestaurant',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Wi-Fi Connection', choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
        migrations.AlterField(
            model_name='reviewbar',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted'),
        ),
        migrations.AlterField(
            model_name='reviewbar',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Comments'),
        ),
        migrations.AlterField(
            model_name='reviewbar',
            name='location',
            field=models.ForeignKey(verbose_name=b'Location ID', to='core.LocationBar'),
        ),
        migrations.AlterField(
            model_name='reviewbar',
            name='rating',
            field=models.IntegerField(null=True, verbose_name=b'Rating', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='company_id',
            field=models.CharField(max_length=36, null=True, verbose_name=b'Company Name', blank=True),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted'),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Comments'),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='location',
            field=models.ForeignKey(verbose_name=b'Location ID', to='core.LocationClub'),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='location_name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Location Name', blank=True),
        ),
        migrations.AlterField(
            model_name='reviewclub',
            name='rating',
            field=models.IntegerField(null=True, verbose_name=b'Rating', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='reviewrestaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Posted'),
        ),
        migrations.AlterField(
            model_name='reviewrestaurant',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Comments'),
        ),
        migrations.AlterField(
            model_name='reviewrestaurant',
            name='location',
            field=models.ForeignKey(verbose_name=b'Location ID', to='core.LocationRestaurant'),
        ),
        migrations.AlterField(
            model_name='reviewrestaurant',
            name='rating',
            field=models.IntegerField(null=True, verbose_name=b'Rating', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
    ]
