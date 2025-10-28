# backend/apps/activos/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.models import Perfil
from decimal import Decimal

class ActivoFijo(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='activos_fijos')
    nombre = models.CharField(max_length=255)
    fecha_adquisicion = models.DateField()
    costo_inicial = models.DecimalField(max_digits=15, decimal_places=2)
    valor_residual = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    vida_util_meses = models.PositiveIntegerField()

    depreciacion_acumulada = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    valor_en_libros = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.valor_en_libros = self.costo_inicial - self.depreciacion_acumulada
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class RegistroDepreciacion(models.Model):
    activo = models.ForeignKey(ActivoFijo, on_delete=models.CASCADE, related_name='registros_depreciacion')
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ('activo', 'fecha') # Solo un registro por mes
