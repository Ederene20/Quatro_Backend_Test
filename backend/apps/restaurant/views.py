from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import exceptions
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


# Create your views here.


class RestaurantView(APIView):
    # Save the restaurant into the database
    permission_classes = (AllowAny,)
    serializer_class = RestaurantSerializer

    def post(self, request):
        restaurant = request.data.get('restaurant', {})
        serializer = self.serializer_class(data=restaurant)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListRestaurantView(APIView):
    # Display all restaurant in the databases
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer

    def get(self):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LocationView(APIView):
    # list of restaurants in a 3km radius of "lng", "lat" coordinates.
    permission_classes = [HasAPIKey]
    serializer_class = RestaurantSerializer

    def post(self, request):
        public_key = request.META["X_PUBLIC_KEY"]
        print(public_key)
        secret_key = request.META["X_SECRET_KEY"]

        try:
            APIKey.objects.is_valid(public_key)
            APIKey.objects.is_valid(secret_key)

        except:
            msg = 'One of your api keys is incorrect'
            raise exceptions.AuthenticationFailed(msg)

        data = request.data
        lng = float(data['lng'])
        lat = float(data['lat'])
        radius = 3
        point = Point(lng, lat)
        restaurant = Restaurant.objects.filter(location__distance_lt=(point, Distance(km=radius)))
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
