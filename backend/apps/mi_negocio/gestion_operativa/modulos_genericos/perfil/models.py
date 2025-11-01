
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from decimal import Decimal

# Se asume que los modelos Departamento y Municipio están en 'api.models'
# ya que es la app principal de la API. Esta importación podría necesitar
# ajuste si están en otro lugar.
from api.models import Department, Municipality

class CategoriaPrestador(models.Model):
    """
    Categorías para los prestadores de servicios turísticos (Hotel, Restaurante, etc.)
    """
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoría")
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="Slug auto-generado para URLs amigables.")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Prestador"
        verbose_name_plural = "Categorías de Prestadores"

class Perfil(models.Model):
    """
    El perfil principal para un prestador de servicios turísticos.
    Este modelo contiene toda la información de negocio y está vinculado al usuario.
    """
    # Relación fundamental con el usuario del sistema
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_prestador',
        verbose_name="Usuario Asociado"
    )

    # Información de negocio
    nombre_comercial = models.CharField(max_length=255, verbose_name="Nombre Comercial")
    nit = models.CharField(max_length=20, unique=True, verbose_name="NIT")
    razon_social = models.CharField(max_length=255, verbose_name="Razón Social")

    # Categorización y Ubicación
    categoria = models.ForeignKey(
        CategoriaPrestador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='perfiles',
        verbose_name="Categoría del Prestador"
    )
    departamento = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Departamento"
    )
    municipio = models.ForeignKey(
        Municipality,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Municipio"
    )
    direccion = models.CharField(max_length=255, blank=True, verbose_name="Dirección")

    # Campos heredados de puntuación para compatibilidad
    # Estos campos son requeridos por otras partes del sistema (ej. admin, lógica de scoring)
    puntuacion_calidad = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.00'))
    puntuacion_servicio = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.00'))
    puntuacion_precio = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.00'))
    puntuacion_total = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.00'), editable=False)

    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def recalcular_puntuacion_total(self):
        """
        Método heredado para compatibilidad. Calcula el promedio de las puntuaciones.
        """
        self.puntuacion_total = (self.puntuacion_calidad + self.puntuacion_servicio + self.puntuacion_precio) / 3
        self.save(update_fields=['puntuacion_total'])

    def __str__(self):
        return f"{self.nombre_comercial} ({self.user.email})"

    class Meta:
        verbose_name = "Perfil de Prestador"
        verbose_name_plural = "Perfiles de Prestadores"
        ordering = ['nombre_comercial']
