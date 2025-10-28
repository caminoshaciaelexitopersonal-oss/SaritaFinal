# backend/apps/inventario/serializers.py
from rest_framework import serializers
from .models import Producto, MovimientoInventario

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ['perfil', 'costo_promedio_ponderado', 'cantidad_en_stock']

class MovimientoInventarioSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    class Meta:
        model = MovimientoInventario
        fields = '__all__'
