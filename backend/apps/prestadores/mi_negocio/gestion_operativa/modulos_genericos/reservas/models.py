from django.db import models
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class CancellationPolicy(TenantAwareModel):
    """
    Define una política de cancelación para un producto o servicio.
    """
    class Meta:
        app_label = 'reservas'

    nombre = models.CharField(max_length=100, help_text="Ej: Estricta, Flexible, No reembolsable")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'prestadores'
