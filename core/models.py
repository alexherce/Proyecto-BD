from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User

import os
import uuid
import base64

import string

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
 (12, 'Food Truck'),
 (13, 'Gourmet'),
 (14, 'Japanese'),
 (15, 'American'),
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
 (8, 'Sushi Bar'),
 (9, 'Other'),
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
 (1, '$1-$49'),
 (2, '$50-$99'),
 (3, '$100-$199'),
 (4, '$200-$299'),
 (5, '$300-$399'),
 (6, '$400-$499'),
 (7, '$500+'),
 )

# -------------------------------------------------
# UPLOAD PICTURES TO AMAZON S3
# -------------------------------------------------

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    #instance.title = blocks[0]
    return os.path.join('uploads/', filename)

# -------------------------------------------------
# MAKES UNIQUE UUID BASE64 TO USE AS PRIMARY KEYS
# -------------------------------------------------

def make_uuid():
	return base64.b64encode(uuid.uuid4().bytes).replace('=', '').replace('+', '-').replace('/', '-')
 
# -------------------------------------------------
# COMPANY (FOR ADMIN PANEL CREATE ONLY)
# ------------------------------------------------- 

class Company(models.Model):
   
   company_id = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False, verbose_name="ID")
   name = models.CharField(max_length=300, verbose_name="Company Name")
   
   class Meta:
        permissions = (
            ("can_publish", "Can Publish"),
        )
   
   def get_absolute_url(self):
		  return reverse(viewname="company_list", args=[self.company_id])
   
   def __unicode__(self):
		  return self.name
		  
# -------------------------------------------------
# CLIENT (EXTENDS DJANGO'S USER MODEL TO ADD
# THE COMPANY TO THEIR PROFILE)
# -------------------------------------------------

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, default='a956e-QARFCDstd9IG6WsQ', verbose_name="Client Company")

# -------------------------------------------------
# RESTAURANTS
# -------------------------------------------------

class LocationRestaurant(models.Model):
    code = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False, verbose_name="ID")
    company_id = models.ForeignKey(Company, verbose_name="Company ID")
    title = models.CharField(max_length=300, verbose_name="Title")
    verified = models.BooleanField(default=False, verbose_name="Verified Location")
    description = models.TextField(null=True, verbose_name="Description")
    address = models.TextField(null=True, verbose_name="Address")
    position = GeopositionField(null=True, verbose_name="Map Position")
    hours = models.TextField(null=True, verbose_name="Service Hours")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    image_file = models.ImageField(upload_to = upload_to_location, verbose_name="Picture")
    food = models.IntegerField(choices=FOODTYPE_CHOICES, null=True, blank=True, verbose_name="Food Type")
    wifi = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True, verbose_name="Wi-Fi Connection")
    outlets = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True, verbose_name="Power Outlets")
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Bathrooms")
    coffee = models.IntegerField(choices=COFFEE_CHOICES, null=True, blank=True, verbose_name="Coffee")
    alcohol = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Alcohol")
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Outdoor Seating")
    price = models.IntegerField(choices=PRICE_CHOICES, null=True, blank=True, verbose_name="Price Category")
    credit_card = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Accepts Credit Cards")
    average = models.FloatField(null=True, blank=True, verbose_name="Average Ratings")

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="locationres_list", args=[self.code])

    def get_average_rating(self):
    	average = self.reviewrestaurant_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return average
    	else:
    		return average

    def get_reviews(self):
    	return self.reviewrestaurant_set.all()

class ReviewRestaurant(models.Model):
   location_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Location Name")
   location = models.ForeignKey(LocationRestaurant, verbose_name="Location ID")
   company_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="Company Name")
   user = models.ForeignKey(User)
   description = models.TextField(null=True, verbose_name="Comments")
   rating = models.IntegerField(choices=RATING_CHOICES, null=True, verbose_name="Rating")
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")

# -------------------------------------------------
# BARS
# -------------------------------------------------

class LocationBar(models.Model):
    code = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False, verbose_name="ID")
    company_id = models.ForeignKey(Company, verbose_name="Company ID")
    title = models.CharField(max_length=300, verbose_name="Title")
    verified = models.BooleanField(default=False, verbose_name="Verified Location")
    description = models.TextField(null=True, verbose_name="Description")
    address = models.TextField(null=True, verbose_name="Address")
    position = GeopositionField(null=True, verbose_name="Map Position")
    hours = models.TextField(null=True, verbose_name="Service Hours")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    image_file = models.ImageField(upload_to = upload_to_location, null=True, verbose_name="Picture")
    bar = models.IntegerField(choices=BARTYPE_CHOICES, null=True, blank=True, verbose_name="Bar Category")
    food = models.IntegerField(choices=FOODTYPE_CHOICES, null=True, blank=True, verbose_name="Food Type")
    wifi = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True, verbose_name="Wi-Fi Connection")
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Bathrooms")
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Outdoor Seating")
    price = models.IntegerField(choices=PRICE_CHOICES, null=True, blank=True, verbose_name="Price Category")
    credit_card = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Accepts Credit Cards")
    average = models.FloatField(null=True, blank=True, verbose_name="Average Ratings")

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="locationbar_list", args=[self.code])

    def get_average_rating(self):
    	average = self.reviewbar_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return average
    	else:
    		return average

    def get_reviews(self):
     rev = self.reviewbar_set.all()
     return rev

class ReviewBar(models.Model):
   location_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Location Name")
   location = models.ForeignKey(LocationBar, verbose_name="Location ID")
   company_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="Company Name")
   user = models.ForeignKey(User)
   description = models.TextField(null=True, verbose_name="Comments")
   rating = models.IntegerField(choices=RATING_CHOICES, null=True, verbose_name="Rating")
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
	
	
# -------------------------------------------------
# NIGHT CLUBS
# -------------------------------------------------

class LocationClub(models.Model):
    code = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False, verbose_name="ID")
    #user = models.ForeignKey(User)
    company_id = models.ForeignKey(Company, verbose_name="Company ID")
    title = models.CharField(max_length=300, verbose_name="Title")
    verified = models.BooleanField(default=False, verbose_name="Verified Location")
    description = models.TextField(null=True, verbose_name="Description")
    address = models.TextField(null=True, verbose_name="Address")
    position = GeopositionField(null=True, verbose_name="Map Position")
    hours = models.TextField(null=True, verbose_name="Service Hours")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    image_file = models.ImageField(upload_to = upload_to_location, null=True, verbose_name="Picture")
    club = models.IntegerField(choices=CLUBTYPE_CHOICES, null=True, blank=True, verbose_name="Club Type")
    music = models.IntegerField(choices=MUSICTYPE_CHOICES, null=True, blank=True, verbose_name="Music Type")
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Bathrooms")
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Outdoor Area")
    free_bar = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Free Bar")
    price = models.IntegerField(choices=PRICE_CHOICES, null=True, blank=True, verbose_name="Price Category")
    entrance_fee = models.IntegerField(choices=ENTRANCEFEE_CHOICES, null=True, blank=True, verbose_name="Entrance Fee")
    credit_card = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Accepts Credit Cards")
    average = models.FloatField(null=True, blank=True, verbose_name="Average Ratings")

    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="locationclub_list", args=[self.code])

    def get_average_rating(self):
    	average = self.reviewclub_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return 0
    	else:
    		return average

    def get_reviews(self):
    	return self.reviewclub_set.all()

class ReviewClub(models.Model):
   location_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Location Name")
   location = models.ForeignKey(LocationClub, verbose_name="Location ID")
   company_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="Company Name")
   user = models.ForeignKey(User)
   description = models.TextField(null=True, verbose_name="Comments")
   rating = models.IntegerField(choices=RATING_CHOICES, null=True, verbose_name="Rating")
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")