from django.contrib import admin
from .models import VehicleModel, VehicleType, VehicleBrand, VehicleYear, PriceList

# Register your models here.
admin.site.register(VehicleBrand)
admin.site.register(VehicleType)
admin.site.register(VehicleModel)
admin.site.register(VehicleYear)
admin.site.register(PriceList)