from django.db import models
from django.conf import settings

class OperacionComercial(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        FACTURADA = 'FACTURADA', 'Facturada'
        ANULADA = 'ANULADA', 'Anulada'

    class TipoOperacion(models.TextChoices):
        VENTA = 'VENTA', 'Venta de Productos/Servicios'
        CONTRATO = 'CONTRATO', 'Contrato'

    perfil_ref_id = models.UUIDField()
    cliente_ref_id = models.UUIDField()
    tipo_operacion = models.CharField(max_length=20, choices=TipoOperacion.choices, default=TipoOperacion.VENTA)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.BORRADOR)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='admin_operaciones_creadas')

    class Meta:
        app_label = 'admin_comercial'
        verbose_name = "Operación Comercial (Admin)"

class ItemOperacionComercial(models.Model):
    operacion = models.ForeignKey(OperacionComercial, on_delete=models.CASCADE, related_name='admin_items')
    producto_ref_id = models.UUIDField()
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'admin_comercial'

class FacturaVenta(models.Model):
    operacion = models.OneToOneField(OperacionComercial, on_delete=models.PROTECT, related_name='admin_factura')
    perfil_ref_id = models.UUIDField()
    numero_factura = models.CharField(max_length=50)
    fecha_emision = models.DateField()

    class Meta:
        app_label = 'admin_comercial'
        verbose_name = "Factura de Venta (Admin)"

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='admin_items')
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'admin_comercial'

class ReciboCaja(models.Model):
    perfil_ref_id = models.UUIDField()
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='admin_recibos_caja')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'admin_comercial'
        verbose_name = "Recibo de Caja (Admin)"
