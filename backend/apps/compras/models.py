# backend/apps/compras/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.prestadores.models import Perfil
from apps.inventario.models import Producto

class Proveedor(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='proveedores')
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class FacturaProveedor(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='facturas_proveedor')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    total = models.DecimalField(max_digits=15, decimal_places=2)

    class EstadoChoices(models.TextChoices):
        PENDIENTE = 'PENDIENTE', _('Pendiente')
        PAGADA = 'PAGADA', _('Pagada')
        VENCIDA = 'VENCIDA', _('Vencida')

    estado = models.CharField(max_length=10, choices=EstadoChoices.choices, default=EstadoChoices.PENDIENTE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    centro_costo = models.ForeignKey('contabilidad.CostCenter', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Factura de {self.proveedor.nombre} - Total: {self.total}"

class ItemFacturaProveedor(models.Model):
    factura = models.ForeignKey(FacturaProveedor, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    costo_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    total_item = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_item = self.cantidad * self.costo_unitario
        super().save(*args, **kwargs)

class PagoRealizado(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='pagos_realizados')
    factura = models.ForeignKey(FacturaProveedor, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, blank=True)
