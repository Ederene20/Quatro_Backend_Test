from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant


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
    permission_classes = (AllowAny,)
    serializer_class = RestaurantSerializer

    def get(self, request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

