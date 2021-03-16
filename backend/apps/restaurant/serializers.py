from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['name', 'public_id', 'location', 'created', 'updated']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
