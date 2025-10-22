from django.db import models
from django.conf import settings

class CategoriaPrestador(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Versión del nombre amigable para URLs")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Categoría de Prestador"
        verbose_name_plural = "Categorías de Prestadores"

class Perfil(models.Model):
    """
    Modelo unificado para el perfil del prestador de servicios turísticos.
    """
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_prestador'
    )
    nombre_comercial = models.CharField(max_length=255, verbose_name="Nombre Comercial")
    categoria = models.ForeignKey(CategoriaPrestador, on_delete=models.SET_NULL, null=True, blank=True)
    telefono_principal = models.CharField(max_length=50, blank=True)
    email_comercial = models.EmailField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    descripcion_corta = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos_prestadores/', blank=True, null=True)
    sitio_web = models.URLField(max_length=255, blank=True)
    redes_sociales = models.JSONField(blank=True, null=True, default=dict)

    class EstadoChoices(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente de Revisión'
        ACTIVO = 'Activo', 'Activo y Visible'
        RECHAZADO = 'Rechazado', 'Rechazado'
        INACTIVO = 'Inactivo', 'Inactivo por el Usuario'

    estado = models.CharField(
        max_length=20,
        choices=EstadoChoices.choices,
        default=EstadoChoices.PENDIENTE
    )

    # --- Scoring Fields ---
    puntuacion_verificacion = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado de verificaciones de cumplimiento.")
    puntuacion_capacitacion = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado por asistencia a capacitaciones.")
    puntuacion_reseñas = models.PositiveIntegerField(default=0, help_text="Puntaje acumulado por reseñas de turistas.")
    puntuacion_formularios = models.PositiveIntegerField(default=0, help_text="Puntaje por completar formularios de caracterización.")
    puntuacion_total = models.PositiveIntegerField(default=0, db_index=True, help_text="Puntaje total para posicionamiento. Se calcula automáticamente.")

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_comercial

    def recalcular_puntuacion_total(self):
        """
        Calcula la puntuación total y guarda todos los campos de puntuación
        parciales y el total en una sola operación de base de datos.
        """
        self.puntuacion_total = (
            getattr(self, 'puntuacion_verificacion', 0) +
            getattr(self, 'puntuacion_capacitacion', 0) +
            getattr(self, 'puntuacion_reseñas', 0) +
            getattr(self, 'puntuacion_formularios', 0)
        )
        self.save(update_fields=[
            'puntuacion_verificacion',
            'puntuacion_capacitacion',
            'puntuacion_reseñas',
            'puntuacion_formularios',
            'puntuacion_total'
        ])

    class Meta:
        verbose_name = "Perfil de Prestador"
        verbose_name_plural = "Perfiles de Prestadores"
