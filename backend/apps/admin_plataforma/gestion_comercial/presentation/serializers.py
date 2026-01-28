from rest_framework import serializers
from ..domain.models import FacturaVenta, ItemFactura, ReciboCaja
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.serializers import ClienteSerializer

class ItemFacturaSerializer(serializers.ModelSerializer):
    producto_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = ItemFactura
        fields = ['id', 'producto', 'producto_id', 'descripcion', 'cantidad', 'precio_unitario', 'subtotal', 'impuestos']
        read_only_fields = ('subtotal', 'producto',)

    def create(self, validated_data):
        # Mapear producto_id al campo 'producto' del modelo
        validated_data['producto_id'] = validated_data.pop('producto_id')
        return super().create(validated_data)

class FacturaVentaListSerializer(serializers.ModelSerializer):
    """
    Serializador BFF para la lista de facturas. Optimizado para lectura.
    """
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = FacturaVenta
        fields = ['id', 'numero_factura', 'cliente_nombre', 'fecha_emision', 'total', 'estado', 'estado_display']
        read_only_fields = fields

class FacturaVentaDetailSerializer(serializers.ModelSerializer):
    """
    CONTRATO DE LECTURA V1 - Detalle de Factura

    Expone una vista completa y enriquecida de una factura. Utilizado para
    mostrar el detalle de una factura al usuario. Todos los campos son de
    solo lectura.
    """
    items = ItemFacturaSerializer(many=True, read_only=True)
    cliente = ClienteSerializer(read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)
    tasa_impuesto_aplicada = serializers.SerializerMethodField()

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'numero_factura', 'cliente', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'tasa_impuesto_aplicada', 'total', 'total_pagado',
            'estado', 'estado_display', 'items'
        ]
        read_only_fields = fields

    def get_tasa_impuesto_aplicada(self, obj):
        # En una implementación futura, esta tasa podría venir de la configuración del perfil,
        # de los productos, etc. Por ahora, se explicita la regla de negocio del 19%.
        return "19.00"


class FacturaVentaWriteSerializer(serializers.ModelSerializer):
    """
    CONTRATO DE ESCRITURA V1 - Creación/Actualización de Factura

    Define el contrato estricto para la creación y actualización de facturas.
    - El cliente envía solo los datos de entrada requeridos.
    - El servidor calcula subtotales, impuestos, totales y gestiona el estado.
    - Cualquier intento de enviar campos calculados resultará en un error 400.
    - No se permite la modificación de facturas en estados finales (PAGADA, ANULADA).
    """
    items = ItemFacturaSerializer(many=True)
    creado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # No exponemos 'cliente' para lectura, solo 'cliente_id' para escritura.
    cliente_id = serializers.IntegerField(write_only=True)

    # --- INICIO DE CONTRATOS EXPLÍCITOS ---
    subtotal = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True,
        help_text="Campo calculado por el servidor. No enviar."
    )
    impuestos = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True,
        help_text="Campo calculado por el servidor. No enviar."
    )
    total = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True,
        help_text="Campo calculado por el servidor. No enviar."
    )
    total_pagado = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True,
        help_text="Campo calculado por el servidor. No enviar."
    )
    estado = serializers.CharField(
        read_only=True,
        # El default del modelo ya lo establece, pero aquí lo hacemos explícito en el contrato.
        default=FacturaVenta.Estado.BORRADOR,
        help_text="El estado es gestionado por el servidor y el valor inicial siempre es 'Borrador'."
    )
    # --- FIN DE CONTRATOS EXPLÍCITOS ---

    class Meta:
        model = FacturaVenta
        fields = [
            'id', 'cliente_id', 'numero_factura', 'fecha_emision', 'fecha_vencimiento',
            'subtotal', 'impuestos', 'total', 'total_pagado', 'estado', 'creado_por', 'items'
        ]
        # Los campos ahora están definidos explícitamente arriba con read_only=True,
        # por lo que esta tupla ya no es necesaria.
        read_only_fields = ()

    def validate(self, data):
        """
        Validación a nivel de objeto para reforzar el contrato.
        """
        # CRÍTICO: Rechaza explícitamente cualquier intento de enviar campos calculados.
        # Un campo read_only=True es ignorado silenciosamente, pero queremos que el contrato falle ruidosamente.
        campos_prohibidos = ['subtotal', 'impuestos', 'total', 'total_pagado', 'estado']
        for campo in campos_prohibidos:
            if campo in self.initial_data:
                raise serializers.ValidationError({
                    campo: f"Este campo es calculado por el servidor y no debe ser enviado."
                })
        return data

    def validate_numero_factura(self, value):
        perfil = self.context['request'].user.perfil_prestador
        # Al crear (self.instance es None), verifica si ya existe.
        if self.instance is None and FacturaVenta.objects.filter(perfil=perfil, numero_factura=value).exists():
            raise serializers.ValidationError("Ya existe una factura con este número.")
        # Al actualizar, solo valida si el número cambió y el nuevo ya existe.
        if self.instance and self.instance.numero_factura != value and FacturaVenta.objects.filter(perfil=perfil, numero_factura=value).exists():
            raise serializers.ValidationError("Ya existe una factura con este número.")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        factura = FacturaVenta.objects.create(**validated_data)
        for item_data in items_data:
            ItemFactura.objects.create(factura=factura, **item_data)
        factura.recalcular_totales()
        return factura

    def update(self, instance, validated_data):
        if instance.estado in [FacturaVenta.Estado.PAGADA, FacturaVenta.Estado.ANULADA]:
            raise serializers.ValidationError(f"No se puede modificar una factura en estado '{instance.estado}'.")

        items_data = validated_data.pop('items', None)

        # Actualiza los campos de la factura
        instance = super().update(instance, validated_data)

        # Si se incluyen items, se reemplazan los existentes
        if items_data is not None:
            instance.items.all().delete()
            for item_data in items_data:
                ItemFactura.objects.create(factura=instance, **item_data)
            instance.recalcular_totales()

        return instance

class ReciboCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReciboCaja
        fields = ['id', 'factura', 'cuenta_bancaria', 'fecha_pago', 'monto', 'metodo_pago']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        recibo = ReciboCaja.objects.create(**validated_data)
        return recibo
