from django.db import models
from django.utils.translation import gettext_lazy as _
from ..modulos_genericos.perfil import Perfil

class Habitacion(models.Model):
    """
    Modelo para gestionar las habitaciones de un hotel.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='habitaciones', limit_choices_to={'categoria__slug': 'hoteles'})

    nombre_habitacion = models.CharField(_("Nombre o Número de Habitación"), max_length=100)
    tipo_habitacion = models.CharField(_("Tipo de Habitación"), max_length=100, help_text=_("Ej: Sencilla, Doble, Suite"))
    capacidad = models.PositiveIntegerField(_("Capacidad de Personas"), default=1)
    precio_base = models.DecimalField(_("Precio Base por Noche"), max_digits=10, decimal_places=2)

    descripcion = models.TextField(_("Descripción"), blank=True)

    disponible = models.BooleanField(_("Disponible para Reservas"), default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_habitacion} ({self.tipo_habitacion}) - {self.perfil.nombre_comercial}"

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        ordering = ['nombre_habitacion']

class ServicioAdicionalHotel(models.Model):
    """
    Modelo para gestionar servicios adicionales de un hotel.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='servicios_adicionales_hotel')

    nombre_servicio = models.CharField(_("Nombre del Servicio"), max_length=150)
    descripcion = models.TextField(_("Descripción"), blank=True)
    precio = models.DecimalField(_("Precio"), max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_servicio} - {self.perfil.nombre_comercial}"

    class Meta:
        verbose_name = "Servicio Adicional de Hotel"
        verbose_name_plural = "Servicios Adicionales de Hotel"
