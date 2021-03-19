from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from .serializers import (RegistrationSerializer, LoginSerializer)
from rest_framework import status
# from rest_framework_api_key.models import APIKey
from .renderers import UserJSONRenderer

# Create your views here.


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    #renderer_classes = (UserJSONRenderer,)

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
    #renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class APIKeyView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LoginSerializer

    def get(self, request):
        return Response( {
            'name': request.user.username,
            'private_key': request.user.private_key,
            'public_key': request.user.public_key,

        })

