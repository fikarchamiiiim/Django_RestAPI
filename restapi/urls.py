from django.urls import path, include
from .views import PriceListDetail, VehicleBrandAPI, VehicleBrandDetail, VehicleModelDetail, VehicleTypeAPI, VehicleModelAPI, VehicleTypeDetail, VehicleYearAPI, PriceListAPI, VehicleYearDetail

urlpatterns = [
    # List
    path('brands/', VehicleBrandAPI.as_view()),
    path('types/', VehicleTypeAPI.as_view()),
    path('models/', VehicleModelAPI.as_view()),
    path('years/', VehicleYearAPI.as_view()),
    path('pricelists/', PriceListAPI.as_view()),
    
    # Detail
    path('brand/<int:id>', VehicleBrandDetail.as_view()),
    path('type/<int:id>', VehicleTypeDetail.as_view()),
    path('model/<int:id>', VehicleModelDetail.as_view()),
    path('year/<int:id>', VehicleYearDetail.as_view()),
    path('pricelist/<int:id>', PriceListDetail.as_view()),

    # Filter
    # path()
    
]