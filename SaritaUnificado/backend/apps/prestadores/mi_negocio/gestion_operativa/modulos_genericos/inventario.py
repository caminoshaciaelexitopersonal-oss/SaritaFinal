from django.db import models
from django.utils.translation import gettext_lazy as _
from .perfil import Perfil

class Inventario(models.Model):
    """
    Modelo para gestionar el inventario de un prestador.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='inventario')
    nombre_item = models.CharField(_("Nombre del Ítem"), max_length=255)
    descripcion = models.TextField(_("Descripción"), blank=True, null=True)
    cantidad = models.PositiveIntegerField(_("Cantidad Disponible"), default=0)
    unidad = models.CharField(_("Unidad de Medida"), max_length=50, help_text=_("Ej: unidades, kg, litros"))
    punto_reorden = models.PositiveIntegerField(_("Punto de Reorden"), default=0, help_text=_("Cantidad mínima antes de necesitar reabastecimiento"))
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_item} ({self.cantidad} {self.unidad})"

    class Meta:
        verbose_name = "Ítem de Inventario"
        verbose_name_plural = "Ítems de Inventario"
        ordering = ['nombre_item']
