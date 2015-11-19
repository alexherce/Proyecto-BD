from django.contrib import admin
import core.models as coremodels

# Register your models here.
admin.site.register(coremodels.LocationRestaurant)
admin.site.register(coremodels.ReviewRestaurant)
admin.site.register(coremodels.LocationBar)
admin.site.register(coremodels.ReviewBar)
admin.site.register(coremodels.LocationClub)
admin.site.register(coremodels.ReviewClub)