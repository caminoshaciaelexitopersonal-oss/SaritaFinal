# backend/apps/comercial/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.prestadores.models import Perfil

class Cliente(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='clientes_comerciales')
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class FacturaVenta(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='facturas_venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class EstadoChoices(models.TextChoices):
        BORRADOR = 'BORRADOR', _('Borrador')
        EMITIDA = 'EMITIDA', _('Emitida')
        PAGADA = 'PAGADA', _('Pagada')
        VENCIDA = 'VENCIDA', _('Vencida')
        ANULADA = 'ANULADA', _('Anulada')

    estado = models.CharField(max_length=10, choices=EstadoChoices.choices, default=EstadoChoices.BORRADOR)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    centro_costo = models.ForeignKey('contabilidad.CostCenter', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.nombre}"

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='items')
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    total_item = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_item = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

class PagoRecibido(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='pagos_recibidos')
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    metodo_pago = models.CharField(max_length=50) # Ej. Efectivo, Transferencia

class NotaCredito(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='notas_credito')
    factura_original = models.ForeignKey(FacturaVenta, on_delete=models.PROTECT)
    fecha = models.DateField()
    motivo = models.TextField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
