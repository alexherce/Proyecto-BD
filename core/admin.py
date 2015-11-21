from django.contrib import admin
import core.models as coremodels
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ClientInline(admin.StackedInline):
    model = coremodels.Client
    can_delete = False
    verbose_name_plural = 'clients'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ClientInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(coremodels.ReviewRestaurant)
admin.site.register(coremodels.LocationBar)
admin.site.register(coremodels.ReviewBar)
admin.site.register(coremodels.LocationClub)
admin.site.register(coremodels.ReviewClub)
admin.site.register(coremodels.Company)
admin.site.register(coremodels.LocationRestaurant)