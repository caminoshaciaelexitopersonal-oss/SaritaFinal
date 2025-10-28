# backend/apps/compras/serializers.py
from rest_framework import serializers
from django.db import transaction
from .models import Proveedor, FacturaProveedor, ItemFacturaProveedor, PagoRealizado

class PagoRealizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoRealizado
        fields = '__all__'
        read_only_fields = ['perfil']

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        read_only_fields = ['perfil']

class ItemFacturaProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFacturaProveedor
        fields = ['id', 'descripcion', 'cantidad', 'costo_unitario']

class FacturaProveedorSerializer(serializers.ModelSerializer):
    items = ItemFacturaProveedorSerializer(many=True)

    class Meta:
        model = FacturaProveedor
        fields = ['id', 'proveedor', 'fecha_emision', 'fecha_vencimiento', 'total', 'estado', 'items']
        read_only_fields = ['perfil', 'created_by']

    def validate_proveedor(self, value):
        user = self.context['request'].user
        if not hasattr(user, 'perfil_prestador') or value.perfil != user.perfil_prestador:
            raise serializers.ValidationError("El proveedor seleccionado no es válido para este perfil.")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        with transaction.atomic():
            factura = FacturaProveedor.objects.create(**validated_data)
            for item_data in items_data:
                ItemFacturaProveedor.objects.create(factura=factura, **item_data)
        return factura
