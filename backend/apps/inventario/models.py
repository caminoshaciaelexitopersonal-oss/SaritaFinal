from django.db import models
from apps.prestadores.models import Perfil

class Producto(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    costo_promedio_ponderado = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    cantidad_en_stock = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    def __str__(self): return self.nombre
