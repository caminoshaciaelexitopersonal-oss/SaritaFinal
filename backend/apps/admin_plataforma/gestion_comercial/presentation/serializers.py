from rest_framework import serializers
# IMPORTAR DESDE PRESTADORES (CANÓNICO)
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta, ItemFactura, ReciboCaja
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.serializers import ClienteSerializer

class ItemFacturaSerializer(serializers.ModelSerializer):
    producto_ref_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = ItemFactura
        fields = ['id', 'producto_ref_id', 'descripcion', 'cantidad', 'precio_unitario', 'subtotal', 'impuestos']
        read_only_fields = ('subtotal',)

class FacturaVentaListSerializer(serializers.ModelSerializer):
    """
    Serializador BFF para la lista de facturas. Optimizado para lectura.
    """
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = ['id', 'numero_factura', 'fecha_emision', 'total', 'estado', 'estado_display']
        read_only_fields = fields

class FacturaVentaDetailSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True, read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'fecha_emision',
            'subtotal', 'impuestos', 'total',
            'estado', 'estado_display', 'items'
        ]
        read_only_fields = fields

class FacturaVentaWriteSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'fecha_emision',
            'subtotal', 'impuestos', 'total', 'estado', 'items'
        ]

class ReciboCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReciboCaja
        fields = ['id', 'factura', 'fecha_pago', 'monto', 'metodo_pago']
