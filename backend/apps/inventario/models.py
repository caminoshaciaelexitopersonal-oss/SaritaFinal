# backend/apps/inventario/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.models import Perfil

class Producto(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    costo_promedio_ponderado = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    cantidad_en_stock = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

class MovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')

    class TipoMovimiento(models.TextChoices):
        ENTRADA = 'ENTRADA', _('Entrada por Compra')
        SALIDA = 'SALIDA', _('Salida por Venta')
        AJUSTE = 'AJUSTE', _('Ajuste Manual')

    tipo = models.CharField(max_length=10, choices=TipoMovimiento.choices)
    fecha = models.DateField()
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)
    costo_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    costo_total = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        self.costo_total = self.cantidad * self.costo_unitario
        super().save(*args, **kwargs)
