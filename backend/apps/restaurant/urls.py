from django.urls import path
from .views import RestaurantView, ListRestaurantView, LocationView

urlpatterns = [
        path('register/', RestaurantView.as_view()), # Save restaurant
        path('list_restaurants/', ListRestaurantView.as_view()), # Show all restaurant
        path('restaurants_locations/', LocationView.as_view()) # Show restaurants in a 3 km radius of coordinate
]