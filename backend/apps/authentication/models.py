import jwt
from datetime import datetime, timedelta
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.conf import settings
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, name, password=None):

        if username is None:
            raise TypeError("User must have a name")

        if name is None:
            raise TypeError("User must have a username")

        user = self.model(username=username, name=name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, name, password):

        if password is None:
            raise TypeError("User must have a password")

        user = self.create_user(username, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_name(self):
        return self.name

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode(
            {
                'id': self.pk,
                'exp': int(dt.strftime("%d"))
            }, settings.SECRET_KEY, algorithm='HS256'
        )

        return token



