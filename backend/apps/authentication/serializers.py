from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    private_key = serializers.CharField(max_length=32, min_length=32, read_only=True)
    public_key = serializers.CharField(max_length=32, min_length=32, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'name', 'password', 'token', 'public_key', 'private_key', 'public_id', 'created', 'updated']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    private_key = serializers.CharField(max_length=32, min_length=32, read_only=True)
    public_key = serializers.CharField(max_length=32, min_length=32, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('A username is required to log in')

        if password is None:
            raise serializers.ValidationError('A password is required to log in')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this username and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('Seems like this user has been deactivated')

        return {
            'username': user.username,
            'name': user.name,
            'token': user.token,
        }

class UserAPISerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    private_key = serializers.CharField(max_length=32, min_length=32, read_only=True)
    public_key = serializers.CharField(max_length=32, min_length=32, read_only=True)

    def validate(self, data):
        private_key = data.get('private_key', None)
        public_key = data.get('public_key', None)

        return {
            'private_key': private_key,
            'public_key': public_key,
        }
