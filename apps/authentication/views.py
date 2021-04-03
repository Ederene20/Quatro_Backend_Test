from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from .serializers import (RegistrationSerializer, LoginSerializer)
from rest_framework import status
from .renderers import UserJSONRenderer
from .models import User
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    # drf_yasg

    @swagger_auto_schema(request_body=RegistrationSerializer, operation_description="Create a new user")
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @swagger_auto_schema(request_body=LoginSerializer, operation_description="Connect the user into his account.")
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class APIKeyView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_description="Get the API Keys using the token")
    def get(self, request):
        return Response({
            'username': request.user.username,
            'X-Secret-Key': request.user.secret_key,
            'X-Public-Key': request.user.public_key,

        })


class UserListView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(operation_description="Get the list of all users in the database using the token")
    def get(self, request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)