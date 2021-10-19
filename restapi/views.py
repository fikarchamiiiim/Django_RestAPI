from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers, status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, AllowAny, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import VehicleBrand, VehicleType, VehicleModel, VehicleYear, PriceList
from .serializers import VehicleBrandSerializer, VehicleTypeSerializer, VehicleModelSerializer, VehicleYearSerializer, PriceListSerializer

def get_object(model, id):
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        raise Http404

def filter_object(model, id):
    try:
        return model.objects.filter(id=id)
    except model.DoesNotExist:
        raise Http404


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# Create your views here.
class VehicleBrandAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = [IsAdminUser|ReadOnly]

    queryset = VehicleBrand.objects.order_by("-id")
    serializer_class = VehicleBrandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VehicleTypeAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    permission_classes = [IsAdminUser|ReadOnly]

    queryset = VehicleType.objects.order_by("-id")
    serializer_class = VehicleTypeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)      


class VehicleModelAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    permission_classes = [IsAdminUser|ReadOnly]

    queryset = VehicleModel.objects.order_by("-id")
    serializer_class = VehicleModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VehicleYearAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    permission_classes = [IsAdminUser|ReadOnly]

    queryset = VehicleYear.objects.order_by("-id")
    serializer_class = VehicleYearSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PriceListAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    permission_classes = [IsAdminUser|ReadOnly]

    queryset = PriceList.objects.order_by("-id")
    serializer_class = PriceListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ======== DETAIL ==================
class VehicleBrandDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser|ReadOnly]

    def get(self, request, id, format=None):
        vehicle_data = filter_object(VehicleBrand, id)
        serializer = VehicleBrandSerializer(vehicle_data, many=True)
        return Response(serializer.data)    

    def patch(self, request, id, format=None):
        vehicle_brand = get_object(VehicleBrand, id)
        serializer = VehicleBrandSerializer(vehicle_brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        vehicle_brand = get_object(VehicleBrand, id)
        vehicle_brand.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)


class VehicleTypeDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser|ReadOnly]

    def get(self, request, id, format=None):
        vehicle_data = filter_object(VehicleType, id)
        serializer = VehicleTypeSerializer(vehicle_data, many=True)
        return Response(serializer.data)
    
    
    def patch(self, request, id, format=None):
        vehicle_type = get_object(VehicleType, id)
        serializer = VehicleTypeSerializer(vehicle_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        vehicle_type = get_object(VehicleType, id)
        vehicle_type.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)


class VehicleModelDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser|ReadOnly]

    def get(self, request, id, format=None):
        vehicle_data = filter_object(VehicleModel, id)
        serializer = VehicleModelSerializer(vehicle_data, many=True)
        return Response(serializer.data)
    
    def patch(self, request, id, format=None):
        vehicle_model = get_object(VehicleModel, id)
        serializer = VehicleModelSerializer(vehicle_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        vehicle_model = get_object(VehicleModel, id)
        vehicle_model.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)


class VehicleYearDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser|ReadOnly]


    def get(self, request, id, format=None):
        vehicle_data = filter_object(VehicleYear, id)
        serializer = VehicleYearSerializer(vehicle_data, many=True)
        return Response(serializer.data)
    
    def patch(self, request, id, format=None):
        vehicle_year = get_object(VehicleYear, id)
        serializer = VehicleYearSerializer(vehicle_year, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        vehicle_year = get_object(VehicleYear, id)
        vehicle_year.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)

class PriceListDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser|ReadOnly]
    
    def get(self, request, id, format=None):
        vehicle_data = filter_object(PriceList, id)
        serializer = PriceListSerializer(vehicle_data, many=True)
        return Response(serializer.data)
    
    
    def patch(self, request, id, format=None):
        price_list = get_object(PriceList, id)
        serializer = PriceListSerializer(price_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        price_list = get_object(PriceList, id)
        price_list.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
