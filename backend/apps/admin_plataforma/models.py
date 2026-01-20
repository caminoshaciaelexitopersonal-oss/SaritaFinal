
from django.db import models
from django.conf import settings
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

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
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    frecuencia = models.CharField(max_length=20, choices=Frecuencia.choices)
    tipo_usuario_objetivo = models.CharField(max_length=20, choices=TipoUsuario.choices)
    is_active = models.BooleanField(default=True, help_text="Indica si el plan está disponible para nuevas suscripciones.")

    def __str__(self):
        return f"{self.nombre} ({self.get_frecuencia_display()}) - ${self.precio}"

class Suscripcion(models.Model):
    """
    Representa la suscripción de un cliente a un plan específico.
    """
    cliente = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="suscripciones_como_cliente"
    )
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="suscripciones")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Suscripción de {self.cliente.nombre_negocio} a {self.plan.nombre}"

    class Meta:
        verbose_name_plural = "Suscripciones"
        ordering = ['-fecha_inicio']
