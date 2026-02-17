from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class KitchenStation(TenantAwareModel):
    """
    Representa una estación de trabajo en la cocina (ej. Parrilla, Postres).
    """
    nombre = models.CharField(_("Nombre de la Estación"), max_length=100)

    def __str__(self):
        return self.nombre

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class MenuItemDetail(models.Model):
    """
    Detalles especializados para un plato.
    """
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='menu_item_details'
    )
    assigned_station = models.ForeignKey(
        KitchenStation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_vegetarian = models.BooleanField(default=False)
    allergens = models.TextField(blank=True)

    def __str__(self):
        return f"Plato: {self.product.nombre}"

    class Meta:
        app_label = 'prestadores'

class RestaurantTable(TenantAwareModel):
    """
    Representa una mesa física.
    """
    class TableStatus(models.TextChoices):
        FREE = 'FREE', _('Libre')
        OCCUPIED = 'OCCUPIED', _('Ocupada')
        RESERVED = 'RESERVED', _('Reservada')
        DIRTY = 'DIRTY', _('Sucia')

    table_number = models.CharField(_("Número de Mesa"), max_length=10)
    capacity = models.PositiveSmallIntegerField(_("Capacidad"))
    status = models.CharField(
        _("Estado"),
        max_length=20,
        choices=TableStatus.choices,
        default=TableStatus.FREE
    )

    def __str__(self):
        return f"Mesa {self.table_number}"

    class Meta(TenantAwareModel.Meta):
        unique_together = ('provider', 'table_number')
        app_label = 'prestadores'
