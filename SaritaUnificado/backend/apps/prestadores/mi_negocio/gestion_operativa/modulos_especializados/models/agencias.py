# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/models/agencias.py
from django.db import models
from ...modulos_genericos.models.base import Perfil
from .hoteles import Habitacion
from .restaurantes import ProductoMenu
from .guias import Ruta
from .transporte import Vehiculo

class PaqueteTuristico(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='paquetes_turisticos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion_dias = models.PositiveIntegerField(default=1)
    precio_base = models.DecimalField(max_digits=12, decimal_places=2, help_text="Precio base del paquete por persona.")
    foto_principal = models.ImageField(upload_to='paquetes_turisticos/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    habitaciones_incluidas = models.ManyToManyField(Habitacion, blank=True)
    comidas_incluidas = models.ManyToManyField(ProductoMenu, blank=True)
    rutas_incluidas = models.ManyToManyField(Ruta, blank=True)
    transporte_incluido = models.ManyToManyField(Vehiculo, blank=True)

    class Meta:
        verbose_name = "Paquete Turístico"
        verbose_name_plural = "Paquetes Turísticos"

    def __str__(self):
        return self.nombre

class Itinerario(models.Model):
    paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE, related_name='itinerarios')
    dia = models.PositiveIntegerField(help_text="Número del día dentro del paquete (ej. 1, 2, 3...)")
    titulo_actividad = models.CharField(max_length=255, help_text="Título principal para el día (ej. 'Llegada y City Tour')")
    descripcion = models.TextField(help_text="Descripción detallada de las actividades del día.")

    class Meta:
        verbose_name = "Itinerario"
        verbose_name_plural = "Itinerarios"
        ordering = ['dia']
        unique_together = ('paquete', 'dia')

    def __str__(self):
        return f"Día {self.dia}: {self.titulo_actividad} (Paquete: {self.paquete.nombre})"
