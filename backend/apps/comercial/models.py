from django.db import models
from django.conf import settings
from apps.prestadores.models import Perfil
from apps.inventario.models import Producto

class Cliente(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='clientes_comerciales')
    nombre = models.CharField(max_length=255)
    def __str__(self): return self.nombre

class FacturaVenta(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='facturas_venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    estado = models.CharField(max_length=10, default='BORRADOR')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"Factura #{self.id}"

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    total_item = models.DecimalField(max_digits=15, decimal_places=2)
    def save(self, *args, **kwargs):
        self.total_item = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
