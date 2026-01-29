from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_especializados.restaurantes.models import KitchenStation, RestaurantTable

class KitchenStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenStation
        fields = ['id', 'nombre']

class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = ['id', 'table_number', 'capacity', 'status', 'pos_x', 'pos_y']
