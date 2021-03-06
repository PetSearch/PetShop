from django.shortcuts import render
from users.models import UserProfile
from users.serializers import UserProfileSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = UserProfileSerializer

    def get_queryset(self):

        try:
            return UserProfile.objects.all()
        except Exception as err:
            return {}


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = UserSerializer

    def get_queryset(self):

        try:
            return User.objects.all()
        except Exception as err:
            return {}
