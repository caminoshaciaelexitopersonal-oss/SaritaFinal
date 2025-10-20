from django.db import models
from api.models import PrestadorServicio

class Producto(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'empresa_producto'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

from django.utils.translation import gettext_lazy as _

class ReglaPrecio(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='reglas_precio')
    nombre_regla = models.CharField(_("Nombre de la Regla"), max_length=200)
    producto_asociado = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="reglas_precio", null=True, blank=True)

    class TipoAjuste(models.TextChoices):
        PORCENTAJE = 'PORCENTAJE', _('Porcentaje')
        MONTO_FIJO = 'MONTO_FIJO', _('Monto Fijo')

    tipo_ajuste = models.CharField(_("Tipo de Ajuste"), max_length=50, choices=TipoAjuste.choices)
    valor_ajuste = models.DecimalField(_("Valor del Ajuste"), max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField(_("Fecha de Inicio"))
    fecha_fin = models.DateField(_("Fecha de Fin"))
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_regla

    class Meta:
        db_table = 'empresa_reglaprecio'
        verbose_name = "Regla de Precio"
        verbose_name_plural = "Reglas de Precios"