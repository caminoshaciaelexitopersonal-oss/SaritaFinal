from django.db import models
from django.conf import settings
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class CategoriaActivo(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='categorias_activo')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ActivoFijo(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='activos_fijos')
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaActivo, on_delete=models.PROTECT, related_name='activos')
    fecha_adquisicion = models.DateField()
    valor_adquisicion = models.DecimalField(max_digits=18, decimal_places=2)
    vida_util_meses = models.PositiveIntegerField()
    valor_residual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_en_libros = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.pk is None: # Si es un objeto nuevo
            self.valor_en_libros = self.valor_adquisicion
        super().save(*args, **kwargs)

class Depreciacion(models.Model):
    activo = models.ForeignKey(ActivoFijo, on_delete=models.CASCADE, related_name='depreciaciones')
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        ordering = ['-fecha']
        unique_together = ('activo', 'fecha')

    def __str__(self):
        return f"Depreciación de {self.activo.nombre} en {self.fecha}"

    def save(self, *args, **kwargs):
        # Actualizar valor en libros del activo
        super().save(*args, **kwargs) # Guardar primero para tener un ID
        total_depreciado = Depreciacion.objects.filter(activo=self.activo).aggregate(total=models.Sum('valor'))['total'] or Decimal('0.00')
        self.activo.valor_en_libros = self.activo.valor_adquisicion - total_depreciado
        if self.activo.valor_en_libros < self.activo.valor_residual:
            self.activo.valor_en_libros = self.activo.valor_residual
        self.activo.save()
