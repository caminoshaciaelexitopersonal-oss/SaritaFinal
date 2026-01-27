from django.db import models
from django.utils.translation import gettext_lazy as _
from backend.perfil.models import TenantAwareModel

class InventoryItem(TenantAwareModel):
    """
    Modelo para gestionar el inventario de consumibles de un prestador.
    Adaptado para la nueva arquitectura.
    """
    class ItemType(models.TextChoices):
        CONSUMABLE = 'CONSUMABLE', _('Consumible')
        ASSET = 'ASSET', _('Activo Fijo')
        RETAIL = 'RETAIL', _('Producto de Venta')

    nombre_item = models.CharField(_("Nombre del Ítem"), max_length=255)
    item_type = models.CharField(_("Tipo de Ítem"), max_length=20, choices=ItemType.choices, default=ItemType.CONSUMABLE)
    cantidad = models.DecimalField(_("Cantidad Disponible"), max_digits=10, decimal_places=2, default=0.00)
    unidad = models.CharField(_("Unidad de Medida"), max_length=50, help_text=_("Ej: unidades, kg, litros"))
    punto_reorden = models.DecimalField(_("Punto de Reorden"), max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nombre_item} ({self.cantidad} {self.unidad})"

    class Meta:
        verbose_name = "Ítem de Inventario"
        verbose_name_plural = "Ítems de Inventario"
        ordering = ['nombre_item']
        app_label = 'prestadores'
