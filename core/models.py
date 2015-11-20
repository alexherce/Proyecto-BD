from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField

import os
import uuid

RATING_CHOICES = (
    (0, 'None'),
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
    )

YESNO_CHOICES = (
 (0, 'No'),
 (1, 'Yes')
 )

PLURAL_CHOICES = (
 (0, 'None'),
 (1, 'Minimal'),
 (2, 'Some'),
 (3, 'Ample')
 )

WIFI_CHOICES = (
 (0, 'None'),
 (1, 'Spotty'),
 (2, 'Strong')
 )

COFFEE_CHOICES = (
 (0, 'None'),
 (1, 'Truck Stop'),
 (2, 'Good'),
 (3, 'Really Good'),
 (4, 'Great'),
 )
 
FOODTYPE_CHOICES = (
 (0, 'None'),
 (1, 'Fast Food'),
 (2, 'Chinese'),
 (3, 'Sushi'),
 (4, 'Mexican'),
 (5, 'Argentine'),
 (6, 'Vegetarian/Vegan'),
 (7, 'Italian'),
 (8, 'Brazilian'),
 (9, 'Seafood'),
 (10, 'Street vendors'),
 (11, 'Coffee'),
 )
 
PRICE_CHOICES = (
 (0, 'None'),
 (1, '$'),
 (2, '$$'),
 (3, '$$$'),
 )
 
BARTYPE_CHOICES = (
 (0, 'None'),
 (1, 'Sports Bar'),
 (2, 'Beer Bar'),
 (3, 'Hookah Bar'),
 (4, 'Cocktail Bar'),
 (5, 'Shots Bar'),
 (6, 'Irish Pub'),
 (7, 'Hookah Bar'),
 (8, 'Other'),
 )
 
CLUBTYPE_CHOICES = (
 (0, 'None'),
 (1, 'Dance Club'),
 (2, 'Adult Entertainment'),
 )
 
MUSICTYPE_CHOICES = (
 (0, 'None'),
 (1, 'Dance/Electronic'),
 (2, 'Karaoke'),
 (3, '60s-70s-80s'),
 (4, 'Reggaeton'),
 (5, 'Salsa'),
 )
 
ENTRANCEFEE_CHOICES = (
 (0, 'None'),
 (1, '$1-$50'),
 (2, '$50-$100'),
 (3, '$100-$200'),
 (4, '$200-$300'),
 (5, '$300-$400'),
 (6, '$400-$500'),
 (7, '$500+'),
 )

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)


# Create your models here.
# -------------------------------------------------
# RESTAURANTS
# -------------------------------------------------

class LocationRestaurant(models.Model):
    title = models.CharField(max_length=300)
    verified = models.BooleanField(default=False)
    description = models.TextField(null=True)
    address = models.TextField(null=True)
    position = GeopositionField(null=True)
    hours = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to = upload_to_location)
    food = models.IntegerField(choices=FOODTYPE_CHOICES, null=True, blank=True)
    wifi = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    outlets = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True)
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    coffee = models.IntegerField(choices=COFFEE_CHOICES, null=True, blank=True)
    alcohol = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    price = models.IntegerField(choices=PRICE_CHOICES, null=True, blank=True)
    credit_card = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="locationres_list", args=[self.id])

    def get_average_rating(self):
    	average = self.reviewrestaurant_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return average
    	else:
    		return int(average)

    def get_reviews(self):
    	return self.reviewrestaurant_set.all()

class ReviewRestaurant(models.Model):
	location = models.ForeignKey(LocationRestaurant)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

# -------------------------------------------------
# BARS
# -------------------------------------------------

class LocationBar(models.Model):
    title = models.CharField(max_length=300)
    verified = models.BooleanField(default=False)
    description = models.TextField(null=True)
    address = models.TextField(null=True)
    position = GeopositionField(null=True)
    hours = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to = upload_to_location, null=True)
    bar = models.IntegerField(choices=BARTYPE_CHOICES, null=True, blank=True)
    food = models.IntegerField(choices=FOODTYPE_CHOICES, null=True, blank=True)
    wifi = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    price = models.IntegerField(choices=PRICE_CHOICES, null=True, blank=True)
    credit_card = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="locationbar_list", args=[self.id])

    def get_average_rating(self):
    	average = self.reviewbar_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return average
    	else:
    		return int(average)

    def get_reviews(self):
     rev = self.reviewbar_set.all()
     return rev

class ReviewBar(models.Model):
	location = models.ForeignKey(LocationBar)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	
# -------------------------------------------------
# NIGHT CLUBS
# -------------------------------------------------

class LocationClub(models.Model):
    title = models.CharField(max_length=300)
    verified = models.BooleanField(default=False)
    description = models.TextField(null=True)
    address = models.TextField(null=True)
    position = GeopositionField(null=True)
    hours = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to = upload_to_location, null=True)
    club = models.IntegerField(choices=CLUBTYPE_CHOICES, null=True, blank=True)
    music = models.IntegerField(choices=MUSICTYPE_CHOICES, null=True, blank=True)
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    free_bar = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    price = models.IntegerField(choices=PRICE_CHOICES, null=True, blank=True)
    entrance_fee = models.IntegerField(choices=ENTRANCEFEE_CHOICES, null=True, blank=True)
    credit_card = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="locationclub_list", args=[self.id])

    def get_average_rating(self):
    	average = self.reviewclub_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return average
    	else:
    		return int(average)

    def get_reviews(self):
    	return self.reviewclub_set.all()

class ReviewClub(models.Model):
	location = models.ForeignKey(LocationClub)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)