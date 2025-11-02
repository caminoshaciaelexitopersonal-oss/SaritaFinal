from django.db import models
from django.conf import settings
from decimal import Decimal
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente

class Producto(models.Model):
    """
    Representa un producto o servicio que un prestador puede vender.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2)
    # Podríamos añadir más campos como SKU, tipo (producto/servicio), etc.

    def __str__(self):
        return self.nombre

class FacturaVenta(models.Model):
    """
    Representa una factura de venta emitida por un prestador.
    """
    class Status(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        EMITIDA = 'EMITIDA', 'Emitida'
        PAGADA = 'PAGADA', 'Pagada'
        ANULADA = 'ANULADA', 'Anulada'

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='facturas')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    total = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    estado = models.CharField(max_length=20, choices=Status.choices, default=Status.BORRADOR)

    def __str__(self):
        return f"Factura #{self.id} para {self.cliente.nombre}"

class ItemFactura(models.Model):
    """
    Representa una línea dentro de una factura de venta.
    """
    factura = models.ForeignKey(FacturaVenta, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=18, decimal_places=2)

    @property
    def total_linea(self):
        return self.cantidad * self.precio_unitario
