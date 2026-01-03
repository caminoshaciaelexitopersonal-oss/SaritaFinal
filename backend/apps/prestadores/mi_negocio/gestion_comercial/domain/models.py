from django.db import models
from django.conf import settings
from decimal import Decimal
from django.db.models import Sum
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product as Producto
from apps.prestadores.mi_negocio.gestion_financiera.models import CuentaBancaria

class FacturaVenta(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        COMERCIAL_CONFIRMADA = 'COMERCIAL_CONFIRMADA', 'Comercial Confirmada'
        ENVIADA = 'ENVIADA', 'Enviada'
        PAGADA = 'PAGADA', 'Pagada'
        VENCIDA = 'VENCIDA', 'Vencida'
        ANULADA = 'ANULADA', 'Anulada'

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='facturas_venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='facturas')
    numero_factura = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    impuestos = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_pagado = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=50, choices=Estado.choices, default=Estado.BORRADOR)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"Factura {self.numero_factura} a {self.cliente.nombre}"

    def recalcular_totales(self):
        items = self.items.all()
        self.subtotal = items.aggregate(total=Sum('subtotal'))['total'] or Decimal('0.00')
        self.impuestos = items.aggregate(total=Sum('impuestos'))['total'] or Decimal('0.00')
        self.total = self.subtotal + self.impuestos
        self.save()

    def actualizar_estado_pago(self):
        self.total_pagado = self.recibos.aggregate(total=Sum('monto'))['total'] or Decimal('0.00')
        if self.total_pagado >= self.total:
            self.estado = self.Estado.PAGADA
        else:
            self.estado = self.Estado.ENVIADA
        self.save()

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=18, decimal_places=2)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2)
    impuestos = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

class ReciboCaja(models.Model):
    class MetodoPago(models.TextChoices):
        EFECTIVO = 'EFECTIVO', 'Efectivo'
        TRANSFERENCIA = 'TRANSFERENCIA', 'Transferencia'
        TARJETA = 'TARJETA', 'Tarjeta'
        OTRO = 'OTRO', 'Otro'

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='recibos_caja')
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='recibos')
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.PROTECT, help_text="Cuenta donde se recibe el pago")
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=MetodoPago.choices)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.factura.actualizar_estado_pago()
        # Aquí se podría crear una TransaccionBancaria de INGRESO automáticamente
