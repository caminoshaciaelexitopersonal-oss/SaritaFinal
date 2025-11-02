from rest_framework import serializers
from .models import Producto, FacturaVenta, ItemFactura

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio']
        read_only_fields = ('perfil',)

class ItemFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFactura
        fields = ['id', 'producto', 'cantidad', 'precio_unitario']

class FacturaVentaReadSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True, read_only=True)
    # Podríamos añadir un serializador para Cliente si fuera necesario
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = ['id', 'cliente', 'cliente_nombre', 'fecha_emision', 'fecha_vencimiento', 'total', 'estado', 'items']

class FacturaVentaWriteSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True)

    class Meta:
        model = FacturaVenta
        fields = ['cliente', 'fecha_emision', 'fecha_vencimiento', 'items']
