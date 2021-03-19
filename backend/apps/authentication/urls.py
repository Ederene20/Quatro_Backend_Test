from django.urls import path
from .views import (RegistrationAPIView, LoginAPIView, APIKeyView)

app_name = 'authentication'

urlpatterns = [
        path('register/', RegistrationAPIView.as_view()),
        path('login/', LoginAPIView.as_view()),
        path('login/api_key/', APIKeyView.as_view())
]
