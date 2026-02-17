from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from decimal import Decimal
import uuid

from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class Vehicle(TenantAwareModel):
    """
    Flota de la transportadora turística.
    """
    class VehicleStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', _('Disponible')
        ASSIGNED = 'ASSIGNED', _('Asignado')
        MAINTENANCE = 'MAINTENANCE', _('En Mantenimiento')
        SUSPENDED = 'SUSPENDED', _('Suspendido')
        INACTIVE = 'INACTIVE', _('Inactivo')

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='vehicle_details',
        null=True, blank=True
    )
    placa = models.CharField(_("Placa"), max_length=10, unique=True, null=True, blank=True)
    tipo = models.CharField(_("Tipo de Vehículo"), max_length=50, null=True, blank=True, help_text=_("Ej: Van, Bus, Automóvil"))
    modelo_ano = models.PositiveIntegerField(_("Modelo (Año)"), null=True, blank=True)
    capacidad_maxima = models.PositiveSmallIntegerField(_("Capacidad de Pasajeros"), default=1)
    status = models.CharField(_("Estado"), max_length=20, choices=VehicleStatus.choices, default=VehicleStatus.AVAILABLE)

    last_technical_review = models.DateField(_("Última Revisión Técnico-Mecánica"), null=True, blank=True)
    insurance_expiry_date = models.DateField(_("Vencimiento de Póliza"), null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.placa}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class VehicleCertification(TenantAwareModel):
    """
    Control de documentos legales del vehículo (SOAT, Contractual, Extracontractual).
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='certifications')
    document_type = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    document_ref_id = models.UUIDField(null=True, blank=True) # Ref a Gestión Archivística
    is_valid = models.BooleanField(default=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class Conductor(TenantAwareModel):
    """
    Capital humano de la transportadora.
    """
    class ConductorStatus(models.TextChoices):
        ACTIVO = 'ACTIVO', _('Activo')
        SUSPENDIDO = 'SUSPENDIDO', _('Suspendido')
        VENCIDO_DOC = 'VENCIDO_DOCUMENTAL', _('Vencido por Documentación')

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_conductor'
    )
    licencia_conduccion = models.CharField(max_length=50, unique=True)
    categoria_licencia = models.CharField(max_length=10)
    fecha_vencimiento_licencia = models.DateField()
    estado = models.CharField(max_length=20, choices=ConductorStatus.choices, default=ConductorStatus.ACTIVO)

    def __str__(self):
        return self.usuario.get_full_name()

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class TransportRoute(TenantAwareModel):
    """
    Rutas de transporte definidas.
    """
    nombre = models.CharField(max_length=200)
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    distancia_km = models.FloatField(null=True, blank=True)
    precio_base = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre}: {self.origen} - {self.destino}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class ScheduledTrip(TenantAwareModel):
    """
    Un viaje específico programado en una ruta.
    """
    class TripStatus(models.TextChoices):
        PROGRAMADO = 'PROGRAMADO', _('Programado')
        CONFIRMADO = 'CONFIRMADO', _('Confirmado')
        EN_TRANSITO = 'EN_TRANSITO', _('En Tránsito')
        FINALIZADO = 'FINALIZADO', _('Finalizado')
        CANCELADO = 'CANCELADO', _('Cancelado')
        LIQUIDADO = 'LIQUIDADO', _('Liquidado')

    ruta = models.ForeignKey(TransportRoute, on_delete=models.PROTECT, related_name='trips')
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()

    vehiculo = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True, related_name='trips')
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True, blank=True, related_name='trips')

    capacidad_total = models.PositiveSmallIntegerField()
    capacidad_reservada = models.PositiveSmallIntegerField(default=0)

    estado = models.CharField(max_length=20, choices=TripStatus.choices, default=TripStatus.PROGRAMADO)

    precio_por_pasajero = models.DecimalField(max_digits=12, decimal_places=2)
    comision_conductor = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def remaining_capacity(self):
        return self.capacidad_total - self.capacidad_reservada

    def __str__(self):
        return f"{self.ruta.nombre} - {self.fecha_salida} {self.hora_salida}"

    def delete(self, *args, **kwargs):
        if self.estado in [self.TripStatus.LIQUIDADO, self.TripStatus.FINALIZADO]:
            raise ValueError("No se puede eliminar un viaje que ya ha sido finalizado o liquidado.")
        super().delete(*args, **kwargs)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'
        indexes = [
            models.Index(fields=['fecha_salida', 'vehiculo']),
            models.Index(fields=['estado']),
        ]

class TransportBooking(TenantAwareModel):
    """
    Reserva de uno o más asientos en un viaje programado.
    """
    trip = models.ForeignKey(ScheduledTrip, on_delete=models.CASCADE, related_name='bookings')
    cliente_ref_id = models.UUIDField()
    numero_pasajeros = models.PositiveIntegerField(default=1)
    total_pago = models.DecimalField(max_digits=12, decimal_places=2)

    fecha_reserva = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    operacion_comercial_ref_id = models.UUIDField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.trip.estado in [ScheduledTrip.TripStatus.LIQUIDADO, ScheduledTrip.TripStatus.FINALIZADO]:
            raise ValueError("No se puede eliminar una reserva de un viaje ya finalizado o liquidado.")
        super().delete(*args, **kwargs)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class PassengerManifest(models.Model):
    """
    Lista oficial de pasajeros en un viaje.
    """
    booking = models.ForeignKey(TransportBooking, on_delete=models.CASCADE, related_name='passengers')
    nombre_completo = models.CharField(max_length=255)
    documento_identidad = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField(null=True, blank=True)
    eps = models.CharField(max_length=100, blank=True)

    def delete(self, *args, **kwargs):
        if self.booking.trip.estado in [ScheduledTrip.TripStatus.LIQUIDADO, ScheduledTrip.TripStatus.FINALIZADO]:
            raise ValueError("No se puede eliminar un pasajero de un manifiesto de un viaje ya finalizado o liquidado.")
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'prestadores'

class TripLiquidation(TenantAwareModel):
    """
    Liquidación financiera del viaje (Ingresos vs Comisiones).
    """
    trip = models.OneToOneField(ScheduledTrip, on_delete=models.CASCADE, related_name='liquidation')
    total_ingresos = models.DecimalField(max_digits=12, decimal_places=2)
    total_comisiones = models.DecimalField(max_digits=12, decimal_places=2)
    utilidad_neta = models.DecimalField(max_digits=12, decimal_places=2)

    fecha_liquidacion = models.DateTimeField(auto_now_add=True)
    asiento_contable_ref_id = models.UUIDField(null=True, blank=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class TransportIncident(TenantAwareModel):
    """
    Reporte de retrasos, fallas mecánicas o incidentes viales.
    """
    class Gravedad(models.TextChoices):
        BAJA = 'BAJA', _('Baja')
        MEDIA = 'MEDIA', _('Media')
        ALTA = 'ALTA', _('Alta')
        CRITICA = 'CRITICA', _('Crítica')

    trip = models.ForeignKey(ScheduledTrip, on_delete=models.CASCADE, related_name='incidents')
    descripcion = models.TextField()
    gravedad = models.CharField(max_length=20, choices=Gravedad.choices, default=Gravedad.BAJA)
    staff_reporta = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    bloquea_operacion = models.BooleanField(default=False)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'
