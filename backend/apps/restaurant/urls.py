from django.urls import path
from .views import RestaurantView, ListRestaurantView, LocationRadiusView, Location

urlpatterns = [
        path('rest/', RestaurantView.as_view()),
        path('list_restaurant/', ListRestaurantView.as_view()),
        path('restaurant/', Location.as_view())
]