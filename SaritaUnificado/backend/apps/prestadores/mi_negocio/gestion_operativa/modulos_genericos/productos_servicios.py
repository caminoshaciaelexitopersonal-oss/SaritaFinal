from django.db import models
from django.utils.translation import gettext_lazy as _
from .perfil import Perfil

class ProductoServicio(models.Model):
    """
    Modelo para gestionar los productos o servicios ofrecidos por un prestador.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos_servicios')
    nombre = models.CharField(_("Nombre del Producto/Servicio"), max_length=255)
    descripcion = models.TextField(_("Descripción"), blank=True, null=True)
    precio = models.DecimalField(_("Precio"), max_digits=12, decimal_places=2, default=0.00)

    class Tipo(models.TextChoices):
        PRODUCTO = 'PRODUCTO', _('Producto')
        SERVICIO = 'SERVICIO', _('Servicio')

    tipo = models.CharField(_("Tipo"), max_length=50, choices=Tipo.choices, default=Tipo.PRODUCTO)

    # Campos específicos para productos (inventario)
    cantidad_disponible = models.PositiveIntegerField(_("Cantidad Disponible"), default=1, help_text=_("Para servicios, usualmente es 1 o se deja en blanco."))
    unidad_medida = models.CharField(_("Unidad de Medida"), max_length=50, blank=True, help_text=_("Ej: unidades, kg, horas, etc."))

    activo = models.BooleanField(_("Activo"), default=True, help_text=_("Indica si el producto/servicio está disponible para la venta."))
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.perfil.nombre_comercial}"

    class Meta:
        verbose_name = "Producto o Servicio"
        verbose_name_plural = "Productos y Servicios"
        ordering = ['nombre']
