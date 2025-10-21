from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.inventario import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'nombre_item', 'descripcion', 'cantidad', 'unidad', 'punto_reorden']
