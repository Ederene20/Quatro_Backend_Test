from django.urls import path
from .views import RestaurantView, ListRestaurantView

urlpatterns = [
        path('rest/', RestaurantView.as_view()),
        path('list_restaurant/', ListRestaurantView.as_view())
]