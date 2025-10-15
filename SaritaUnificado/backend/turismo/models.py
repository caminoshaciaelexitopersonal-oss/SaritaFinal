from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio

class DetallesHotel(models.Model):
    prestador = models.OneToOneField(PrestadorServicio, on_delete=models.CASCADE, related_name="detalles_hotel", limit_choices_to={'categoria__slug': 'hoteles'})
    reporte_ocupacion_nacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")
    reporte_ocupacion_internacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")

    def __str__(self):
        return f"Detalles de Hotel para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Detalles de Hotel"
        verbose_name_plural = "Detalles de Hoteles"
        db_table = 'api_detalleshotel'