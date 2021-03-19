from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models import Manager
from apps.abstract.models import AbstractModel


# Create your models here.

class RestaurantManager(models.Manager):
    pass


class Restaurant(AbstractModel):
    name = models.CharField(max_length=255, unique=True)
    location = models.PointField(null=True, blank=True)
    objects = RestaurantManager()
    #objects = GeoManager()
    #mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

    #@property
    #def location(self):
     #   location = [self.lat, self.lng]
      #   return location
