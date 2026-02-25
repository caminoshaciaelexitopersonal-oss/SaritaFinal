from django.db import models
from django.conf import settings
from apps.domain_business.operativa.models import ProviderProfile

class CategoriaProducto(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_categorias_inventario')
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_inventario'

class Producto(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_productos_inventario')
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True, related_name='admin_productos')
    nombre = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, blank=True)
    stock_actual = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    precio_venta = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    costo = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        app_label = 'admin_inventario'

from apps.core_erp.base.base_models import BaseWarehouse, BaseInventoryMovement

class Almacen(BaseWarehouse):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_almacenes')

    class Meta:
        app_label = 'admin_inventario'

class MovimientoInventario(BaseInventoryMovement):
    class TipoMovimiento(models.TextChoices):
        ENTRADA = 'ENTRADA', 'Entrada'
        SALIDA = 'SALIDA', 'Salida'

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='admin_movimientos')
    almacen = models.ForeignKey(Almacen, on_delete=models.PROTECT, related_name='admin_movimientos')
    tipo_movimiento = models.CharField(max_length=20, choices=TipoMovimiento.choices)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='admin_movimientos_inventario')

    class Meta:
        app_label = 'admin_inventario'
