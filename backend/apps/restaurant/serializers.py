from rest_framework import serializers
from .models import Restaurant
#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import Distance


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['name', 'public_id', 'location', 'created', 'updated']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)


class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    lat = serializers.FloatField()
    lng = serializers.FloatField()

    #def get(self, data):
    #    lat = float(data.get('lat', None))
    #    lng = float(data.get('lng', None))
    #    radius = 3
     #   point = Point(lng, lat)
      #  maps = Restaurant.objects.filter(location__distance_lt=(point, Distance(km=radius)))
       # return maps
