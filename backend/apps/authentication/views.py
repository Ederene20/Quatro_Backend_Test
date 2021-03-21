from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from .serializers import (RegistrationSerializer, LoginSerializer)
from rest_framework import status
from .renderers import UserJSONRenderer
from .models import User


# Create your views here.


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
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
    permission_classes = (IsAuthenticated,)
    serializer_class = LoginSerializer

    def get(self, request):
        return Response({
            'username': request.user.username,
            'X-Private-Key': request.user.secret_key,
            'X-Public-Key': request.user.public_key,

        })


class UserListView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)