from django.contrib import admin
import core.models as coremodels

# Register your models here.
admin.site.register(coremodels.ReviewRestaurant)
admin.site.register(coremodels.LocationBar)
admin.site.register(coremodels.ReviewBar)
admin.site.register(coremodels.LocationClub)
admin.site.register(coremodels.ReviewClub)

class LocationRestaurantAdmin(admin.ModelAdmin):
    normaluser_fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'food', 'outlet', 'bathrooms', 'coffee', 'alcohol', 'outdoor', 'price', 'credit_card',]
    superuser_fields = ['verified', 'wifi',]
    
    def get_form(self, request, obj=None, **kwargs):                             
        if request.user.is_superuser:
            self.fields = self.normaluser_fields + self.superuser_fields 
        else:                                                                    
            self.fields = self.normaluser_fields
        return super(LocationRestaurantAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(coremodels.LocationRestaurant, LocationRestaurantAdmin)