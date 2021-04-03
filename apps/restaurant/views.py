from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import exceptions
from .serializers import RestaurantSerializer, LocationSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RestaurantView(APIView):
    # Save the restaurant into the database
    permission_classes = (AllowAny,)
    serializer_class = RestaurantSerializer

    @swagger_auto_schema(request_body=RestaurantSerializer, operation_description="Create a new restaurant.")
    def post(self, request):
        restaurant = request.data
        serializer = self.serializer_class(data=restaurant)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListRestaurantView(APIView):
    # Display all restaurant in the databases
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer

    @swagger_auto_schema(operation_description="Get all restaurants in the database with the token.")
    def get(self, request):
        restaurant = Restaurant.objects.all()
        i = 0
        for element in restaurant:
            i = i + 1
        total = "Total : {}".format(i)+" restaurants"

        serializer = RestaurantSerializer(restaurant, many=True)
        return Response([total, serializer.data], status=status.HTTP_200_OK)


class LocationView(APIView):
    # list of restaurants in a 3km radius of "lng", "lat" coordinates.

    @swagger_auto_schema(request_body=LocationSerializer, operation_description="list of restaurants in a 3km radius of 'lng','lat' given coordinates. The user should put his secret and public api keys in the header.")
    def post(self, request):
        public_key = request.META["HTTP_X_PUBLIC_KEY"]
        print(public_key)
        secret_key = request.META["HTTP_X_SECRET_KEY"]

        try:
            APIKey.objects.get_from_key(public_key)
            APIKey.objects.get_from_key(secret_key)

        except:
            msg = 'One of your api keys is incorrect'
            raise exceptions.AuthenticationFailed(msg)

        data = request.data
        lng = float(data['lng'])
        lat = float(data['lat'])
        radius = 3
        point = Point(lng, lat)
        restaurant = Restaurant.objects.filter(location__distance_lt=(point, Distance(km=radius)))
        j = 0
        for elements in restaurant:
            j = j + 1
        total = "Total : {}".format(j) + " restaurant(s) was found."
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response([total, serializer.data], status=status.HTTP_200_OK)
