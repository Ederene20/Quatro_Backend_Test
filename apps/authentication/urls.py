from django.urls import path
from .views import (RegistrationAPIView, LoginAPIView, APIKeyView, UserListView)

app_name = 'authentication'

urlpatterns = [
        path('register/', RegistrationAPIView.as_view()),
        path('login/', LoginAPIView.as_view()),
        path('api_keys/', APIKeyView.as_view()),
        path('list_users/', UserListView.as_view())
]
