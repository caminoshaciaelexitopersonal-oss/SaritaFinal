from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class CategoriaProducto(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='categorias_producto')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Almacen(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='almacenes')
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    descripcion = models.TextField(blank=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    stock_actual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    stock_minimo = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nombre} (SKU: {self.sku})"

class MovimientoInventario(models.Model):
    class TipoMovimiento(models.TextChoices):
        ENTRADA = 'ENTRADA', 'Entrada'
        SALIDA = 'SALIDA', 'Salida'
        AJUSTE_POSITIVO = 'AJUSTE_POSITIVO', 'Ajuste Positivo'
        AJUSTE_NEGATIVO = 'AJUSTE_NEGATIVO', 'Ajuste Negativo'

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    almacen = models.ForeignKey(Almacen, on_delete=models.PROTECT, related_name='movimientos')
    tipo_movimiento = models.CharField(max_length=20, choices=TipoMovimiento.choices)
    cantidad = models.DecimalField(max_digits=18, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.tipo_movimiento} de {self.cantidad} para {self.producto.nombre}"

    def save(self, *args, **kwargs):
        # Actualizar el stock del producto antes de guardar el movimiento
        stock_anterior = self.producto.stock_actual
        if self.tipo_movimiento == self.TipoMovimiento.ENTRADA or self.tipo_movimiento == self.TipoMovimiento.AJUSTE_POSITIVO:
            self.producto.stock_actual += self.cantidad
        elif self.tipo_movimiento == self.TipoMovimiento.SALIDA or self.tipo_movimiento == self.TipoMovimiento.AJUSTE_NEGATIVO:
            if self.producto.stock_actual < self.cantidad:
                raise ValidationError(f"Stock insuficiente para {self.producto.nombre}. Stock actual: {self.producto.stock_actual}")
            self.producto.stock_actual -= self.cantidad

        self.producto.save()
        super().save(*args, **kwargs)
