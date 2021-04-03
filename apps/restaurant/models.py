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
    lng = models.FloatField(default=0, max_length=128)
    lat = models.FloatField(default=0, max_length=128)
    location = models.PointField(null=True, blank=True, default=None)
    objects = RestaurantManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['lng', 'lat']

    objects = RestaurantManager()

    def save(self, *args, **kwargs):
        # Take lng and lat and store them as a coordinates in the database
        self.location = Point(self.lng, self.lat)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
