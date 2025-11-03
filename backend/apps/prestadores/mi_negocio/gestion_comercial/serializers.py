from rest_framework import serializers
from .models import FacturaVenta, ItemFactura, ReciboCaja
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.serializers import ClienteSerializer

class ItemFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFactura
        fields = ['id', 'producto', 'descripcion', 'cantidad', 'precio_unitario', 'subtotal', 'impuestos']
        read_only_fields = ('subtotal',)

class FacturaVentaSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True)
    creado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'cliente', 'cliente_id', 'numero_factura', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'total', 'total_pagado', 'estado', 'creado_por', 'items'
        ]
        read_only_fields = ('subtotal', 'impuestos', 'total', 'total_pagado', 'estado')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        factura = FacturaVenta.objects.create(**validated_data)
        for item_data in items_data:
            ItemFactura.objects.create(factura=factura, **item_data)
        factura.recalcular_totales()
        return factura

class ReciboCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReciboCaja
        fields = ['id', 'factura', 'cuenta_bancaria', 'fecha_pago', 'monto', 'metodo_pago']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        recibo = ReciboCaja.objects.create(**validated_data)
        return recibo
