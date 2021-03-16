from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (RegistrationSerializer, LoginSerializer, UserAPISerializer)
from rest_framework import status
from rest_framework_api_key.models import APIKey


# Create your views here.


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #public_key = APIKey.objects.create_key(name="public_key" + "-" + request.data.get(user.username))
        #private_key = APIKey.objects.create_key(name="private_key" + "-" + request.data.get(user.username))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class APIKeyView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAPISerializer

    def get(self, request):
        user = request.user()
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

