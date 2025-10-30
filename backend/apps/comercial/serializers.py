# backend/apps/comercial/serializers.py
from rest_framework import serializers
from django.db import transaction
from .models import FacturaVenta, ItemFactura, Cliente
from apps.inventario.models import Producto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ('perfil',)

class ItemFacturaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = ItemFactura
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'precio_unitario', 'total_item']
        read_only_fields = ('total_item',)

class FacturaVentaSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True)
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'cliente', 'cliente_nombre', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'total', 'estado', 'items'
        ]
        read_only_fields = ('perfil', 'subtotal', 'impuestos', 'total')

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        factura = FacturaVenta.objects.create(**validated_data)
        subtotal = 0
        for item_data in items_data:
            item = ItemFactura.objects.create(factura=factura, **item_data)
            subtotal += item.total_item
        factura.subtotal = subtotal
        factura.total = subtotal + factura.impuestos
        factura.save()
        return factura
