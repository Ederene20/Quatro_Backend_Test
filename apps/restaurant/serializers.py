from rest_framework import serializers
from .models import Restaurant
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


class RestaurantSerializer(serializers.ModelSerializer):
    location = serializers.CharField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'lng', 'lat', 'location', 'created', 'updated']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)


class LocationSerializer(serializers.Serializer):
    lat = serializers.CharField()
    lng = serializers.CharField()


