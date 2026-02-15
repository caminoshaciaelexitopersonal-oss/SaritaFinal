from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class Amenity(TenantAwareModel):
    """
    Representa una comodidad o servicio (ej. WiFi, AC, Piscina).
    """
    nombre = models.CharField(_("Nombre de la Amenidad"), max_length=100)

    def __str__(self):
        return self.nombre

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class RoomType(TenantAwareModel):
    """
    Define un 'tipo' de habitación vinculado a un producto vendible.
    """
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='room_type_details'
    )
    capacidad = models.PositiveSmallIntegerField(_("Capacidad de Personas"))
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return f"Tipo: {self.product.nombre}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class Room(TenantAwareModel):
    """
    Representa una habitación física individual.
    """
    class HousekeepingStatus(models.TextChoices):
        CLEAN = 'CLEAN', _('Limpia')
        DIRTY = 'DIRTY', _('Sucia')
        IN_PROGRESS = 'IN_PROGRESS', _('En Limpieza')
        INSPECTION = 'INSPECTION', _('Para Inspección')
        OUT_OF_ORDER = 'OUT_OF_ORDER', _('Fuera de Servicio')

    class RoomStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', _('Disponible')
        OCCUPIED = 'OCCUPIED', _('Ocupada')
        RESERVED = 'RESERVED', _('Reservada')
        MAINTENANCE = 'MAINTENANCE', _('Mantenimiento')

    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    numero_habitacion = models.CharField(_("Número de Habitación"), max_length=10)
    status = models.CharField(
        _("Estado de Ocupación"),
        max_length=20,
        choices=RoomStatus.choices,
        default=RoomStatus.AVAILABLE
    )
    housekeeping_status = models.CharField(
        _("Estado de Limpieza"),
        max_length=20,
        choices=HousekeepingStatus.choices,
        default=HousekeepingStatus.CLEAN
    )

    def __str__(self):
        return f"Hab {self.numero_habitacion} ({self.room_type.product.nombre})"

    class Meta(TenantAwareModel.Meta):
        unique_together = ('provider', 'numero_habitacion')
        app_label = 'prestadores'
