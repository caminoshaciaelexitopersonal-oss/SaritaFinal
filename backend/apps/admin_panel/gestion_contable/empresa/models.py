from django.db import models
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class InformacionEmpresa(models.Model):
    perfil = models.OneToOneField(ProviderProfile, on_delete=models.CASCADE, related_name='informacion_empresa')
    razon_social = models.CharField(max_length=255)
    nit = models.CharField(max_length=20, unique=True)
    # ... (otros campos)

    def __str__(self):
        return self.razon_social

class Tercero(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='terceros')
    nombre = models.CharField(max_length=255)
    nit_o_cedula = models.CharField(max_length=20, unique=True)
    # ... (otros campos)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'empresa'
        unique_together = ('perfil', 'nit_o_cedula')
