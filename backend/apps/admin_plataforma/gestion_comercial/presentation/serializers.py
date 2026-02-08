from rest_framework import serializers
# IMPORTAR DESDE PRESTADORES (CANÓNICO)
from apps.admin_plataforma.gestion_comercial.domain.models import FacturaVenta, ItemFactura, ReciboCaja
from apps.admin_plataforma.gestion_operativa.modulos_genericos.clientes.serializers import AdminClienteSerializer

class AdminItemFacturaSerializer(serializers.ModelSerializer):
    producto_ref_id = serializers.UUIDField(write_only=True)
    impuestos = serializers.DecimalField(default=0, max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = ItemFactura
        fields = ['id', 'producto_ref_id', 'descripcion', 'cantidad', 'precio_unitario', 'subtotal', 'impuestos']
        read_only_fields = ('subtotal',)

class AdminFacturaVentaListSerializer(serializers.ModelSerializer):
    """
    Serializador BFF para la lista de facturas. Optimizado para lectura.
    """
    estado_display = serializers.CharField(source='operacion.get_estado_display', read_only=True)
    total = serializers.DecimalField(source='operacion.total', max_digits=12, decimal_places=2, read_only=True)
    estado = serializers.CharField(source='operacion.estado', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = ['id', 'numero_factura', 'fecha_emision', 'total', 'estado', 'estado_display']
        read_only_fields = fields

class AdminFacturaVentaDetailSerializer(serializers.ModelSerializer):
    items = AdminItemFacturaSerializer(many=True, read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)
    total = serializers.DecimalField(source='operacion.total', max_digits=12, decimal_places=2, read_only=True)
    estado = serializers.CharField(source='operacion.estado', read_only=True)
    subtotal = serializers.DecimalField(source='operacion.total', max_digits=12, decimal_places=2, read_only=True) # Assuming subtotal approx for now or add to model
    impuestos = serializers.DecimalField(default=0, max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'fecha_emision',
            'subtotal', 'impuestos', 'total',
            'estado', 'estado_display', 'items'
        ]
        read_only_fields = fields

    def get_estado_display(self, obj):
        # Fallback if operacion is missing
        if hasattr(obj, 'operacion') and obj.operacion:
            return obj.operacion.get_estado_display()
        return "Pendiente"

class AdminFacturaVentaWriteSerializer(serializers.ModelSerializer):
    items = AdminItemFacturaSerializer(many=True, required=False)

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'fecha_emision', 'operacion', 'items'
        ]

class AdminReciboCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReciboCaja
        fields = ['id', 'factura', 'fecha_pago', 'monto', 'metodo_pago']
