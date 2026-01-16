
from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import OperacionComercial, ItemOperacionComercial, FacturaVenta, ItemFactura, ReciboCaja
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.serializers import ClienteSerializer
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

# NOTA PARA ADMIN: Los serializadores se mantienen en su mayoría para la lectura.
# La creación de nuevas operaciones por un admin podría requerir lógica adicional
# para asignar correctamente el perfil del prestador.

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
        fields = ['id', 'perfil', 'cliente_id', 'tipo_operacion', 'estado', 'subtotal', 'impuestos', 'total', 'items']
        read_only_fields = ('subtotal', 'impuestos', 'total')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # El perfil se debe inferir del cliente seleccionado.
        # Se asume que el cliente tiene una relación directa con un ProviderProfile.
        cliente = validated_data.get('cliente')
        if not cliente or not hasattr(cliente, 'perfil_prestador'):
             raise serializers.ValidationError("El cliente seleccionado no está asociado a ningún prestador.")

        validated_data['perfil'] = cliente.perfil_prestador
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
    # Añadimos el perfil para que el admin sepa a quién pertenece
    prestador_nombre = serializers.CharField(source='perfil.nombre_comercial', read_only=True, allow_null=True)


    class Meta:
        model = FacturaVenta
        fields = ['id', 'numero_factura', 'cliente_nombre', 'prestador_nombre', 'fecha_emision', 'total', 'estado', 'estado_display']
        read_only_fields = fields

class FacturaVentaDetailSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True, read_only=True)
    cliente = ClienteSerializer(read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)
    prestador_nombre = serializers.CharField(source='perfil.nombre_comercial', read_only=True, allow_null=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'cliente', 'prestador_nombre', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'total', 'total_pagado',
            'estado', 'estado_display', 'items', 'estado_dian', 'cufe'
        ]
        read_only_fields = fields

# Los serializadores de escritura no se exponen al admin por ahora para simplificar.
# La gestión se centrará en la lectura y supervisión.

class ReciboCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReciboCaja
        fields = ['id', 'factura', 'cuenta_bancaria', 'fecha_pago', 'monto', 'metodo_pago']

    def create(self, validated_data):
        # La lógica de creación debe asegurar que el perfil se asigne correctamente.
        factura = validated_data.get('factura')
        if not factura:
            raise serializers.ValidationError("Se requiere una factura para crear un recibo de caja.")
        validated_data['perfil'] = factura.perfil
        recibo = ReciboCaja.objects.create(**validated_data)
        return recibo
