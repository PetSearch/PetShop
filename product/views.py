from django.shortcuts import render
from product.models import Category, Item
from product.serializers import CategorySerializer, ItemSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = CategorySerializer

    def get_queryset(self):

        try:
            return Category.objects.all()
        except Exception as err:
            return {}


class ItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = ItemSerializer

    def get_queryset(self):

        try:
            return Item.objects.all()
        except Exception as err:
            return {}
