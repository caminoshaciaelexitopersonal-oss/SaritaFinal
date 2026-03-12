from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel, BaseModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class NightclubProfile(TenantAwareModel):
    """
    Configuración específica para un establecimiento nocturno.
    """
    hora_apertura_estandar = models.TimeField(null=True, blank=True)
    hora_cierre_estandar = models.TimeField(null=True, blank=True)
    capacidad_total = models.PositiveIntegerField(default=0)
    politica_cover = models.TextField(blank=True)

    def __str__(self):
        return f"Perfil Nocturno: {self.provider.nombre_comercial}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class NightEvent(TenantAwareModel):
    """
    Representa un evento específico (fiesta, concierto, etc.)
    """
    class EventType(models.TextChoices):
        FIESTA = 'FIESTA', _('Fiesta Temática')
        CONCIERTO = 'CONCIERTO', _('Concierto / Show en vivo')
        PRIVADO = 'PRIVADO', _('Evento Privado')
        GENERAL = 'GENERAL', _('Apertura General')

    class EventStatus(models.TextChoices):
        PROGRAMADO = 'PROGRAMADO', _('Programado')
        ACTIVO = 'ACTIVO', _('Activo')
        CERRADO = 'CERRADO', _('Cerrado')
        LIQUIDADO = 'LIQUIDADO', _('Liquidado')

    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=EventType.choices, default=EventType.GENERAL)
    capacidad_maxima = models.PositiveIntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EventStatus.choices, default=EventStatus.PROGRAMADO)
    cover_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} ({self.fecha_inicio.date()})"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class NightZone(TenantAwareModel):
    """
    Zonas del establecimiento (VIP, General, Barra, Terraza).
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    recargo_vip = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class NightTable(TenantAwareModel):
    """
    Mesas físicas en el establecimiento.
    """
    class TableStatus(models.TextChoices):
        LIBRE = 'LIBRE', _('Libre')
        OCUPADA = 'OCUPADA', _('Ocupada')
        RESERVADA = 'RESERVADA', _('Reservada')
        BLOQUEADA = 'BLOQUEADA', _('Bloqueada')

    zona = models.ForeignKey(NightZone, on_delete=models.CASCADE, related_name='tables')
    numero = models.CharField(max_length=10)
    capacidad = models.PositiveSmallIntegerField(default=4)
    estado = models.CharField(max_length=20, choices=TableStatus.choices, default=TableStatus.LIBRE)

    def __str__(self):
        return f"Mesa {self.numero} - {self.zona.nombre}"

    class Meta(TenantAwareModel.Meta):
        unique_together = ('provider', 'numero')
        app_label = 'prestadores'

class NightConsumption(TenantAwareModel):
    """
    Registro de consumo de una mesa o cliente en una barra.
    """
    class ConsumptionStatus(models.TextChoices):
        ABIERTO = 'ABIERTO', _('Abierto')
        FACTURADO = 'FACTURADO', _('Facturado')
        PAGADO = 'PAGADO', _('Pagado')
        ANULADO = 'ANULADO', _('Anulado')

    evento = models.ForeignKey(NightEvent, on_delete=models.CASCADE, related_name='consumptions')
    mesa = models.ForeignKey(NightTable, on_delete=models.SET_NULL, null=True, blank=True, related_name='consumptions')
    cliente_ref_id = models.UUIDField(null=True, blank=True) # Referencia al cliente (CRM)
    staff_responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    estado = models.CharField(max_length=20, choices=ConsumptionStatus.choices, default=ConsumptionStatus.ABIERTO)

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.estado in [self.ConsumptionStatus.FACTURADO, self.ConsumptionStatus.PAGADO]:
            raise ValueError("No se puede eliminar un consumo que ya ha sido facturado o pagado. Debe anularlo.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Consumo #{self.id} - {self.mesa if self.mesa else 'Barra'}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class NightConsumptionItem(models.Model):
    """
    Línea de consumo individual.
    """
    consumption = models.ForeignKey(NightConsumption, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    observaciones = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'prestadores'

class LiquorInventory(TenantAwareModel):
    """
    Inventario especializado de bebidas y licores.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='liquor_data')
    stock_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lote = models.CharField(max_length=50, blank=True)
    ubicacion_almacen = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Stock: {self.product.nombre}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class InventoryMovement(TenantAwareModel):
    """
    Log inmutable de movimientos de inventario.
    """
    class MovementType(models.TextChoices):
        ENTRADA = 'ENTRADA', _('Entrada por Compra')
        SALIDA_CONSUMO = 'SALIDA_CONSUMO', _('Salida por Consumo')
        AJUSTE = 'AJUSTE', _('Ajuste de Inventario')
        TRASLADO = 'TRASLADO', _('Traslado Interno')

    liquor = models.ForeignKey(LiquorInventory, on_delete=models.CASCADE, related_name='movements')
    tipo = models.CharField(max_length=20, choices=MovementType.choices)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    referencia_consumo = models.ForeignKey(NightConsumption, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    justificacion = models.TextField(blank=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class CashClosing(TenantAwareModel):
    """
    Cierre de caja por turno o evento.
    """
    evento = models.ForeignKey(NightEvent, on_delete=models.CASCADE, related_name='cash_closings')
    staff_cierre = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    total_efectivo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_tarjeta = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_monedero = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_esperado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_real = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    diferencia = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    observaciones = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class EventLiquidation(TenantAwareModel):
    """
    Resumen financiero final de un evento.
    """
    evento = models.OneToOneField(NightEvent, on_delete=models.CASCADE, related_name='liquidation')
    total_ingresos_cover = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_ingresos_consumo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_egresos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    utilidad_neta = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    liquidado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha_liquidacion = models.DateTimeField(auto_now_add=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'
