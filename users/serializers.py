
from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'name']
