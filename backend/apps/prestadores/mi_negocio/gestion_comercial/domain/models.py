from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product
from apps.prestadores.mi_negocio.gestion_financiera.models import CuentaBancaria

class OperacionComercial(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        FACTURADA = 'FACTURADA', 'Facturada'
        ANULADA = 'ANULADA', 'Anulada'

    class TipoOperacion(models.TextChoices):
        VENTA = 'VENTA', 'Venta de Productos/Servicios'
        CONTRATO = 'CONTRATO', 'Contrato'
        # Otros tipos se pueden añadir aquí

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='operaciones_comerciales')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='operaciones_comerciales')
    tipo_operacion = models.CharField(max_length=20, choices=TipoOperacion.choices, default=TipoOperacion.VENTA)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.BORRADOR)

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Operación #{self.id} para {self.cliente.nombre}"

    def recalcular_totales(self):
        subtotal = self.items.aggregate(total=Sum('subtotal'))['total'] or Decimal('0.00')
        self.subtotal = subtotal
        self.impuestos = self.subtotal * Decimal('0.19') # Lógica de impuestos simplificada
        self.total = self.subtotal + self.impuestos
        self.save()

class ItemOperacionComercial(models.Model):
    operacion = models.ForeignKey(OperacionComercial, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Product, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)


class FacturaVenta(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        EMITIDA = 'EMITIDA', 'Emitida'
        PAGADA = 'PAGADA', 'Pagada'
        ANULADA = 'ANULADA', 'Anulada'

    class EstadoDIAN(models.TextChoices):
        PENDIENTE_ENVIO = 'PENDIENTE_ENVIO', 'Pendiente de Envío'
        ENVIADA = 'ENVIADA', 'Enviada'
        ACEPTADA = 'ACEPTADA', 'Aceptada'
        RECHAZADA = 'RECHAZADA', 'Rechazada con Errores'
        CONTINGENCIA = 'CONTINGENCIA', 'Contingencia'

    operacion = models.OneToOneField(OperacionComercial, on_delete=models.PROTECT, related_name='factura')
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='facturas_venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='facturas')
    numero_factura = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_pagado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.BORRADOR)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='facturas_creadas')

    # --- Campos de Facturación Electrónica ---
    estado_dian = models.CharField(
        max_length=20,
        choices=EstadoDIAN.choices,
        default=EstadoDIAN.PENDIENTE_ENVIO,
        null=True,
        blank=True
    )
    cufe = models.CharField(max_length=255, null=True, blank=True, help_text="Código Único de Factura Electrónica")
    track_id_dian = models.CharField(max_length=255, null=True, blank=True, help_text="ID de seguimiento de la DIAN")
    xml_dian = models.TextField(null=True, blank=True, help_text="XML de la factura electrónica enviada a la DIAN")
    pdf_dian = models.FileField(upload_to='facturas_electronicas/', null=True, blank=True, help_text="PDF de la representación gráfica de la factura")
    dian_response_log = models.JSONField(default=dict, null=True, blank=True, help_text="Log de respuestas de la DIAN")


    class Meta:
        unique_together = ('perfil', 'numero_factura')
        ordering = ['-fecha_emision', '-numero_factura']

    def __str__(self):
        return f"Factura #{self.numero_factura} - {self.cliente.nombre}"

    def recalcular_totales(self):
        subtotal = self.items.aggregate(total=Sum('subtotal'))['total'] or Decimal('0.00')
        self.subtotal = subtotal
        # Asumimos una tasa de impuestos fija por ahora. Una implementación real sería más compleja.
        self.impuestos = self.subtotal * Decimal('0.19')
        self.total = self.subtotal + self.impuestos
        self.save()

    def actualizar_estado_pago(self):
        pagado = self.recibos_caja.aggregate(total=Sum('monto'))['total'] or Decimal('0.00')
        self.total_pagado = pagado
        if self.total_pagado >= self.total:
            self.estado = self.Estado.PAGADA
        self.save()

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Product, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class ReciboCaja(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='recibos_caja')
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='recibos_caja')
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.PROTECT)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Recibo de Caja #{self.id} para Factura #{self.factura.numero_factura}"
