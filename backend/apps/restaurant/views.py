from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RestaurantSerializer, LocationSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


# Create your views here.


class RestaurantView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RestaurantSerializer

    def post(self, request):
        restaurant = request.data.get('restaurant', {})
        serializer = self.serializer_class(data=restaurant)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListRestaurantView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer

    def get(self, request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Location(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LocationSerializer

    def post(self, request):
        lat = request.data.get('lat', None)
        lng = request.data.get('lng', None)
        radius = 3
        point = Point(lng, lat)
        restaurant = Restaurant.objects.filter(location__distance_lt=(point, Distance(km=radius)))
        # serializer = LocationSerializer(restaurant, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(restaurant)


class LocationRadiusView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LocationSerializer

    def post(self, request):
        restaurant_location = request.data.get('restaurant', {})
        serializer = self.serializer_class(data=restaurant_location)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
