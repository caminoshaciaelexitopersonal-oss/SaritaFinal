from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class Vehicle(TenantAwareModel):
    """
    Flota de la transportadora.
    """
    class VehicleStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', _('Disponible')
        IN_SERVICE = 'IN_SERVICE', _('En Servicio')
        MAINTENANCE = 'MAINTENANCE', _('En Mantenimiento')
        INACTIVE = 'INACTIVE', _('Inactivo')

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='vehicle_details',
        null=True, blank=True
    )
    placa = models.CharField(_("Placa"), max_length=10, unique=True, null=True, blank=True)
    modelo_ano = models.PositiveIntegerField(_("Modelo (Año)"), null=True, blank=True)
    capacidad = models.PositiveSmallIntegerField(_("Capacidad de Pasajeros"), default=1)
    status = models.CharField(_("Estado"), max_length=20, choices=VehicleStatus.choices, default=VehicleStatus.AVAILABLE)

    insurance_expiry_date = models.DateField(_("Vencimiento de Póliza"), null=True, blank=True)

    def __str__(self):
        return f"{self.product.nombre} ({self.placa})"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class TransportRoute(TenantAwareModel):
    """
    Rutas frecuentes.
    """
    nombre = models.CharField(max_length=200)
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    distancia_km = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}: {self.origen} - {self.destino}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'
