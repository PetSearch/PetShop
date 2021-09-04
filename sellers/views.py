from django.shortcuts import render
from sellers.models import SellerProfile
from sellers.serializers import SellerProfileSerializer, SellerSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.


class SellerProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = SellerProfileSerializer

    def get_queryset(self):

        try:
            return SellerProfile.objects.all()
        except Exception as err:
            return {}


class SellerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = SellerSerializer

    def get_queryset(self):

        try:
            return User.objects.all()
        except Exception as err:
            return {}
