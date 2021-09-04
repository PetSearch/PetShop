from rest_framework import serializers
from sellers.models import SellerProfile
from django.contrib.auth.models import User

class SellerProfileSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = SellerProfile
        fields = '__all__'
        # fields = ['id', 'name']

class SellerSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'name']
