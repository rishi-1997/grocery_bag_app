from django.contrib import admin

# Register your models here.
from app_GroceryBag.models import GrossBag


class CreateAdmin(admin.ModelAdmin):
    list_display = ('Item_Name','Item_Quantity','Item_status','Date')


admin.site.register(GrossBag, CreateAdmin)


