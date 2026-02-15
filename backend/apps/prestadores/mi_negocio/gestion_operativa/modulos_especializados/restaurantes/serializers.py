from rest_framework import serializers
from .models import KitchenStation, MenuItemDetail, RestaurantTable

class KitchenStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenStation
        fields = '__all__'

class MenuItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemDetail
        fields = '__all__'

class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = '__all__'
