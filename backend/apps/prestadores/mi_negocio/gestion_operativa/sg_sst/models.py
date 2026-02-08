from django.db import models
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class RiesgoLaboral(TenantAwareModel):
    class NivelRiesgo(models.TextChoices):
        LOW = 'LOW', 'Bajo'
        MEDIUM = 'MEDIUM', 'Medio'
        HIGH = 'HIGH', 'Alto'

    area = models.CharField(max_length=100)
    factor_riesgo = models.CharField(max_length=200)
    nivel = models.CharField(max_length=10, choices=NivelRiesgo.choices, default=NivelRiesgo.LOW)
    medida_control = models.TextField()

    class Meta: app_label = 'prestadores'

class IncidenteSST(TenantAwareModel):
    class EstadoIncidente(models.TextChoices):
        OPEN = 'OPEN', 'Abierto'
        CLOSED = 'CLOSED', 'Cerrado'

    fecha = models.DateField()
    tipo = models.CharField(max_length=100) # Ej: Accidente, Incidente
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=EstadoIncidente.choices, default=EstadoIncidente.OPEN)

    class Meta: app_label = 'prestadores'
