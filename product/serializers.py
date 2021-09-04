from rest_framework import serializers
from product.models import Category, Item


class CategorySerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'
        # fields = ['id', 'name']
