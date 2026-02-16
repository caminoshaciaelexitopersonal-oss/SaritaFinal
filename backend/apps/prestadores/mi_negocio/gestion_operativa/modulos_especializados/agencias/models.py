from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class TravelPackage(TenantAwareModel):
    """
    Representa un paquete turístico ofrecido por la agencia.
    """
    nombre = models.CharField(_("Nombre del Paquete"), max_length=200)
    descripcion = models.TextField(_("Descripción"))
    precio_base = models.DecimalField(max_digits=12, decimal_places=2)
    duracion_dias = models.PositiveIntegerField(default=1)
    incluye_transporte = models.BooleanField(default=False)
    incluye_alojamiento = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class PackageDestination(models.Model):
    """
    Destinos incluidos en un paquete.
    """
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE, related_name='destinations')
    atractivo_ref_id = models.UUIDField(help_text="Referencia al AtractivoTuristico de la app api")
    orden = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['orden']
        app_label = 'prestadores'

class AgencyBooking(TenantAwareModel):
    """
    Reserva de un paquete por un cliente.
    """
    class BookingStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pendiente')
        CONFIRMED = 'CONFIRMED', _('Confirmada')
        CANCELLED = 'CANCELLED', _('Cancelada')
        COMPLETED = 'COMPLETED', _('Completada')

    package = models.ForeignKey(TravelPackage, on_delete=models.PROTECT)
    cliente_ref_id = models.UUIDField()
    fecha_viaje = models.DateField()
    numero_personas = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=BookingStatus.choices, default=BookingStatus.PENDING)
    total_pago = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Reserva {self.id} - {self.package.nombre}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'
