from rest_framework import serializers
from ..domain.models import OperacionComercial, ItemOperacionComercial, FacturaVenta, ItemFactura, ReciboCaja
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.serializers import ClienteSerializer
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class ItemOperacionComercialSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='producto'
    )

    class Meta:
        model = ItemOperacionComercial
        fields = ['producto_id', 'descripcion', 'cantidad', 'precio_unitario']

class OperacionComercialSerializer(serializers.ModelSerializer):
    items = ItemOperacionComercialSerializer(many=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source='cliente'
    )
    estado = serializers.CharField(read_only=True)

    class Meta:
        model = OperacionComercial
        fields = ['id', 'cliente_id', 'tipo_operacion', 'estado', 'subtotal', 'impuestos', 'total', 'items']
        read_only_fields = ('subtotal', 'impuestos', 'total')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        validated_data['creado_por'] = self.context['request'].user

        operacion = OperacionComercial.objects.create(**validated_data)
        for item_data in items_data:
            ItemOperacionComercial.objects.create(operacion=operacion, **item_data)

        operacion.recalcular_totales()
        return operacion


class ItemFacturaSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='producto', write_only=True
    )

    class Meta:
        model = ItemFactura
        fields = ['id', 'producto', 'producto_id', 'descripcion', 'cantidad', 'precio_unitario', 'subtotal', 'impuestos']
        read_only_fields = ('subtotal', 'producto',)

class FacturaVentaListSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = ['id', 'numero_factura', 'cliente_nombre', 'fecha_emision', 'total', 'estado', 'estado_display']
        read_only_fields = fields

class FacturaVentaDetailSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True, read_only=True)
    cliente = ClienteSerializer(read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'cliente', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'total', 'total_pagado',
            'estado', 'estado_display', 'items', 'estado_dian', 'cufe'
        ]
        read_only_fields = fields


class FacturaVentaWriteSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True)
    creado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cliente_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'cliente_id', 'numero_factura', 'fecha_emision', 'fecha_vencimiento',
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
