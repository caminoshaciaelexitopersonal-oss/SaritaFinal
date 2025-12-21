from django.db import models
from django.conf import settings
from django.utils import timezone
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class CategoriaActivo(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='categorias_activos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class ActivoFijo(models.Model):
    class MetodoDepreciacion(models.TextChoices):
        LINEA_RECTA = 'LINEA_RECTA', 'Línea Recta'
        # Se pueden añadir otros métodos en el futuro

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='activos_fijos')
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaActivo, on_delete=models.PROTECT, related_name='activos')
    descripcion = models.TextField(blank=True)
    fecha_adquisicion = models.DateField()
    costo_adquisicion = models.DecimalField(max_digits=18, decimal_places=2)
    valor_residual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    vida_util_meses = models.PositiveIntegerField()
    metodo_depreciacion = models.CharField(max_length=20, choices=MetodoDepreciacion.choices, default=MetodoDepreciacion.LINEA_RECTA)
    depreciacion_acumulada = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_en_libros = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.valor_en_libros = self.costo_adquisicion - self.depreciacion_acumulada
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class CalculoDepreciacion(models.Model):
    activo = models.ForeignKey(ActivoFijo, on_delete=models.CASCADE, related_name='calculos_depreciacion')
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Depreciación de {self.activo.nombre} en {self.fecha} por {self.monto}"

    def save(self, *args, **kwargs):
        # Usar una transacción para asegurar la consistencia de los datos
        from django.db import transaction
        with transaction.atomic():
            super().save(*args, **kwargs)
            # Actualizar la depreciación acumulada en el activo
            self.activo.depreciacion_acumulada += self.monto
            self.activo.save()
