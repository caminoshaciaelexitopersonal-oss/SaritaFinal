from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.inventario.models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['provider']
