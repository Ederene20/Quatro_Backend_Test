from django.db import models
#from django.contrib.gis.db import models
#from django.contrib.gis.measure import Distance
from apps.abstract.models import AbstractModel


# Create your models here.

class RestaurantManager(models.Manager):
    pass


class Restaurant(AbstractModel):
    name = models.CharField(max_length=255, unique=True)
    #location = models.PointField()
    #location = models.JSONField(null=True)
    #lat = models.FloatField(default=0, max_length=32)
    #lng = models.FloatField(default=0,max_length=32)

    objects = RestaurantManager()

    def __str__(self):
        return self.name

    #@property
    #def location(self):
     #   location = [self.lat, self.lng]
      #   return location
