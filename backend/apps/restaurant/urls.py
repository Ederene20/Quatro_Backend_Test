from django.urls import path
from .views import RestaurantView, ListRestaurantView, Location

urlpatterns = [
        path('rest/', RestaurantView.as_view()), # Save restaurant
        path('list_restaurant/', ListRestaurantView.as_view()), # Show all restaurant
        path('restaurant/', Location.as_view()) # Show restaurants in a 3 km radius of coordinate
]