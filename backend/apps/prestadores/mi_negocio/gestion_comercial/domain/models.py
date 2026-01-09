# backend/apps/prestadores/mi_negocio/gestion_comercial/domain/models.py
from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal

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
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    documento_archivistico_ref_id = models.UUIDField(null=True, blank=True)

class ItemOperacionComercial(models.Model):
    operacion = models.ForeignKey(OperacionComercial, on_delete=models.CASCADE, related_name='items')
    producto_ref_id = models.UUIDField()
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

class FacturaVenta(models.Model):
    # ... (estados sin cambios) ...
    operacion = models.OneToOneField(OperacionComercial, on_delete=models.PROTECT, related_name='factura')
    perfil_ref_id = models.UUIDField()
    cliente_ref_id = models.UUIDField()
    numero_factura = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    # ... (otros campos) ...
    documento_archivistico_ref_id = models.UUIDField(null=True, blank=True)

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='items')
    producto_ref_id = models.UUIDField()
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class ReciboCaja(models.Model):
    perfil_ref_id = models.UUIDField()
    cuenta_bancaria_ref_id = models.UUIDField()
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='recibos_caja')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
