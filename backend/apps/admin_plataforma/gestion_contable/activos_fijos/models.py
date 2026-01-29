from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class CategoriaActivo(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_categorias_activos')
    nombre = models.CharField(max_length=100)
    vida_util_meses = models.IntegerField()

    class Meta:
        app_label = 'admin_activos_fijos'

class ActivoFijo(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_activos_fijos')
    categoria = models.ForeignKey(CategoriaActivo, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)
    fecha_adquisicion = models.DateField()
    valor_adquisicion = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_activos_fijos'

class CalculoDepreciacion(models.Model):
    activo = models.ForeignKey(ActivoFijo, on_delete=models.CASCADE, related_name='admin_depreciaciones')
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_activos_fijos'
