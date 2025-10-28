# backend/apps/comercial/serializers.py
from rest_framework import serializers
from django.db import transaction
from .models import Cliente, FacturaVenta, ItemFactura, PagoRecibido, NotaCredito

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['perfil']

class ItemFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFactura
        fields = ['id', 'descripcion', 'cantidad', 'precio_unitario', 'total_item']

class FacturaVentaSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True)
    class Meta:
        model = FacturaVenta
        fields = ['id', 'cliente', 'fecha_emision', 'fecha_vencimiento', 'subtotal', 'impuestos', 'total', 'pagado', 'estado', 'items']
        read_only_fields = ['perfil', 'created_by']

    def validate_cliente(self, value):
        user = self.context['request'].user
        if not hasattr(user, 'perfil_prestador') or value.perfil != user.perfil_prestador:
            raise serializers.ValidationError("El cliente seleccionado no es válido para este perfil.")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        factura = FacturaVenta.objects.create(**validated_data)
        for item_data in items_data:
            ItemFactura.objects.create(factura=factura, **item_data)
        return factura

class PagoRecibidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoRecibido
        fields = '__all__'
        read_only_fields = ['perfil']

    def validate_factura(self, value):
        user = self.context['request'].user
        if not hasattr(user, 'perfil_prestador') or value.perfil != user.perfil_prestador:
            raise serializers.ValidationError("La factura seleccionada no es válida para este perfil.")
        return value

class NotaCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaCredito
        fields = '__all__'
        read_only_fields = ['perfil']
