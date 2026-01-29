
from django.db import models
from django.conf import settings
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Plan(models.Model):
    """
    Define un plan de suscripción que la plataforma Sarita puede vender.
    """
    class TipoUsuario(models.TextChoices):
        GOBIERNO = 'GOBIERNO', 'Gobierno'
        PRESTADOR = 'PRESTADOR', 'Prestador'

    class Frecuencia(models.TextChoices):
        MENSUAL = 'MENSUAL', 'Mensual'
        SEMESTRAL = 'SEMESTRAL', 'Semestral'
        ANUAL = 'ANUAL', 'Anual'

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frecuencia = models.CharField(max_length=20, choices=Frecuencia.choices, default=Frecuencia.MENSUAL)
    tipo_usuario_objetivo = models.CharField(max_length=20, choices=TipoUsuario.choices, default=TipoUsuario.PRESTADOR)
    is_active = models.BooleanField(default=True, help_text="Indica si el plan está disponible para nuevas suscripciones.")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        app_label = 'admin_plataforma'

class Suscripcion(models.Model):
    """
    Representa la suscripción de un cliente a un plan específico.
    """
    cliente = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="admin_suscripciones"
    )
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="admin_suscripciones")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'admin_plataforma'
