# backend/apps/comercial/serializers.py
from rest_framework import serializers
from django.db import transaction
from .models import FacturaVenta, ItemFactura, Cliente, PagoRecibido, NotaCredito
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
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'cliente', 'cliente_nombre', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'total', 'pagado', 'estado', 'estado_display',
            'items'
        ]
        read_only_fields = ('perfil', 'subtotal', 'impuestos', 'total', 'pagado')

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        factura = FacturaVenta.objects.create(**validated_data)

        subtotal = 0
        for item_data in items_data:
            item = ItemFactura.objects.create(factura=factura, **item_data)
            subtotal += item.total_item

        # Actualizar totales de la factura
        factura.subtotal = subtotal
        # (Lógica de impuestos podría ir aquí)
        factura.total = subtotal + factura.impuestos
        factura.save()

        return factura

    @transaction.atomic
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)

        # Actualizar campos de la factura
        instance = super().update(instance, validated_data)

        if items_data is not None:
            # Eliminar items viejos
            instance.items.all().delete()

            subtotal = 0
            # Crear items nuevos
            for item_data in items_data:
                item = ItemFactura.objects.create(factura=instance, **item_data)
                subtotal += item.total_item

            # Actualizar totales
            instance.subtotal = subtotal
            instance.total = subtotal + instance.impuestos
            instance.save()

        return instance

class PagoRecibidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoRecibido
        fields = '__all__'
        read_only_fields = ('perfil',)

class NotaCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaCredito
        fields = '__all__'
        read_only_fields = ('perfil',)
