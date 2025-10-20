from rest_framework import serializers
# Eliminadas las importaciones de Cliente y Producto
from .models import Vacante, Inventario, Costo

# Eliminado ClienteSerializer

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'nombre_item', 'descripcion', 'cantidad', 'unidad', 'punto_reorden', 'fecha_actualizacion']
        read_only_fields = ['id', 'fecha_actualizacion', 'prestador']

class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = ['id', 'concepto', 'monto', 'fecha', 'es_recurrente', 'tipo_costo']
        read_only_fields = ['id', 'prestador']

class VacanteSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.CharField(source='empresa.nombre_comercial', read_only=True) # Corregido a nombre_comercial

    class Meta:
        model = Vacante
        fields = [
            'id', 'titulo', 'descripcion', 'tipo_contrato', 'ubicacion',
            'salario', 'fecha_publicacion', 'fecha_vencimiento', 'activa',
            'empresa', 'empresa_nombre'
        ]
        read_only_fields = ['id', 'fecha_publicacion', 'empresa', 'empresa_nombre']
