from rest_framework import serializers
from coupon.models import Coupon


class CouponSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = Coupon
        fields = ['code', 'discount_type', 'discount_value', 'valid_from', 'valid_till', 'status', 'id']
