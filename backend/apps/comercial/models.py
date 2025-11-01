from django.db import models
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class Cliente(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='clientes_comerciales',
        verbose_name='Perfil del Prestador'
    )
    nombre = models.CharField(max_length=255, verbose_name='Nombre completo')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

# Stub models for tests to pass
class FacturaVenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
