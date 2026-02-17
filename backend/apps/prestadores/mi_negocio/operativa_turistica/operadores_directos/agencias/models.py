from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel, ProviderProfile

class TravelPackage(TenantAwareModel):
    """
    Representa un paquete turístico unificado (Fase 14).
    """
    class PackageStatus(models.TextChoices):
        BORRADOR = 'BORRADOR', _('Borrador')
        PUBLICADO = 'PUBLICADO', _('Publicado')
        RESERVADO = 'RESERVADO', _('Reservado')
        CONFIRMADO = 'CONFIRMADO', _('Confirmado')
        EN_EJECUCION = 'EN_EJECUCION', _('En Ejecución')
        FINALIZADO = 'FINALIZADO', _('Finalizado')
        LIQUIDADO = 'LIQUIDADO', _('Liquidado')

    nombre = models.CharField(_("Nombre del Paquete"), max_length=200)
    descripcion = models.TextField(_("Descripción"))
    precio_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    margen_agencia = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de ganancia", default=10.0)
    estado = models.CharField(max_length=20, choices=PackageStatus.choices, default=PackageStatus.BORRADOR)
    duracion_dias = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} ({self.estado})"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class PackageComponent(models.Model):
    """
    Componentes individuales del paquete (Fase 14.1.4).
    """
    class ServiceType(models.TextChoices):
        HOTEL = 'HOTEL', _('Alojamiento')
        TRANSPORTE = 'TRANSPORTE', _('Transporte')
        GUIA = 'GUIA', _('Guía Turístico')
        EVENTO = 'EVENTO', _('Evento/Actividad')
        ARTESANO = 'ARTESANO', _('Artesanía/Taller')
        OTROS = 'OTROS', _('Otros')

    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE, related_name='components')
    tipo_servicio = models.CharField(max_length=20, choices=ServiceType.choices)
    proveedor = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='components_as_provider')
    referencia_id = models.UUIDField(help_text="ID del servicio específico en su módulo original")
    precio_proveedor = models.DecimalField(max_digits=12, decimal_places=2)
    comision_proveedor = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    is_active = models.BooleanField(default=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo_servicio} - {self.proveedor.nombre_comercial}"

    class Meta:
        app_label = 'prestadores'

class AgencyBooking(TenantAwareModel):
    """
    Reserva consolidada del paquete (Fase 14.1.5).
    """
    class BookingStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pendiente')
        CONFIRMED = 'CONFIRMED', _('Confirmada')
        CANCELLED = 'CANCELLED', _('Cancelada')
        COMPLETED = 'COMPLETED', _('Completada')

    package = models.ForeignKey(TravelPackage, on_delete=models.PROTECT)
    cliente_ref_id = models.UUIDField()
    fecha_inicio = models.DateField()
    numero_personas = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=BookingStatus.choices, default=BookingStatus.PENDING)
    total_facturado = models.DecimalField(max_digits=12, decimal_places=2)

    # Referencias ERP
    asiento_contable_id = models.UUIDField(null=True, blank=True)
    factura_ref_id = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.package.nombre}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class AgencyLiquidation(TenantAwareModel):
    """
    Liquidación final de la agencia (Fase 14.1.6).
    """
    booking = models.OneToOneField(AgencyBooking, on_delete=models.CASCADE, related_name='liquidation')
    monto_total_ingresado = models.DecimalField(max_digits=12, decimal_places=2)
    total_costo_proveedores = models.DecimalField(max_digits=12, decimal_places=2)
    utilidad_agencia = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_liquidacion = models.DateTimeField(auto_now_add=True)
    procesado = models.BooleanField(default=False)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class ProviderCommission(models.Model):
    """
    Trazabilidad de comisiones por proveedor dentro de un paquete.
    """
    liquidation = models.ForeignKey(AgencyLiquidation, on_delete=models.CASCADE, related_name='provider_commissions')
    proveedor = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    monto_base = models.DecimalField(max_digits=12, decimal_places=2)
    monto_comision = models.DecimalField(max_digits=12, decimal_places=2)
    pagado = models.BooleanField(default=False)

    class Meta:
        app_label = 'prestadores'

class PackageIncident(TenantAwareModel):
    """
    Registro de incidencias en la ejecución del paquete.
    """
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    booking = models.ForeignKey(AgencyBooking, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField()
    nivel_gravedad = models.CharField(max_length=20, default='LOW')
    resuelta = models.BooleanField(default=False)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'
