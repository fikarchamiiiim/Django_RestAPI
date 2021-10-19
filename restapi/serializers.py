from django.db.models import fields
from rest_framework import serializers
from .models import VehicleBrand, VehicleType, VehicleModel, VehicleYear, PriceList

class VehicleBrandSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(VehicleBrandSerializer, self).__init__(many=many, *args, **kwargs)]
    type = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = VehicleBrand
        fields = ['id', 'name', 'type', 'created_at', 'update_at']

class VehicleTypeSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = VehicleType
        fields = ['id', 'name', 'model', 'brand_id','created_at', 'update_at']

class VehicleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleModel
        fields = ['id', 'name', 'type_id', 'created_at', 'update_at']

class VehicleYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleYear
        fields = ['id', 'year', 'created_at', 'update_at']

class PriceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceList
        fields = ['id', 'code', 'price', 'year_id', 'model_id', 'created_at', 'update_at']