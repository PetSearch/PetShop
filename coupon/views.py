from django.shortcuts import render
from coupon.models import Coupon
from coupon.serializers import CouponSerializer
from rest_framework import viewsets
class CouponViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = CouponSerializer

    def get_queryset(self):

        try:
            return Coupon.objects.all()
        except Exception as err:
            return {}
