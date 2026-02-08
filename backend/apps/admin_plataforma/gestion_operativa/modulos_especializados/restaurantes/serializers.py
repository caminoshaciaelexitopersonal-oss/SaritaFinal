from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_especializados.restaurantes.models import KitchenStation, RestaurantTable

class AdminKitchenStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenStation
        fields = ['id', 'nombre']

class AdminRestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = ['id', 'numero', 'capacidad']
