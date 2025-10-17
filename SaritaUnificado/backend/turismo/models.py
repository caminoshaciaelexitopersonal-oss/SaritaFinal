from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio

class Hotel(models.Model):
    prestador = models.OneToOneField(PrestadorServicio, on_delete=models.CASCADE, primary_key=True, related_name='hotel_profile')
    categoria_estrellas = models.PositiveIntegerField(default=3, help_text=_("Número de estrellas del hotel"))
    reporte_ocupacion_nacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")
    reporte_ocupacion_internacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")

    def __str__(self):
        return f"Perfil de Hotel para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Perfil de Hotel"
        verbose_name_plural = "Perfiles de Hotel"

class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='habitaciones')
    nombre_o_numero = models.CharField(max_length=100)

    class Tipo(models.TextChoices):
        INDIVIDUAL = 'INDIVIDUAL', _('Individual')
        DOBLE = 'DOBLE', _('Doble')
        SUITE = 'SUITE', _('Suite')
        FAMILIAR = 'FAMILIAR', _('Familiar')

    tipo_habitacion = models.CharField(max_length=50, choices=Tipo.choices)
    capacidad = models.PositiveIntegerField(default=1)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_o_numero} ({self.hotel.prestador.nombre_negocio})"

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"