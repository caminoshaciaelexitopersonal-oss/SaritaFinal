from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class RawMaterial(TenantAwareModel):
    """
    Inventario de materias primas para el artesano (Barro, Madera, Lana, etc.)
    """
    nombre = models.CharField(max_length=200)
    unidad_medida = models.CharField(max_length=50, help_text="Ej: Kg, Gramos, Metros")
    stock_actual = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    costo_por_unidad = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} ({self.stock_actual} {self.unidad_medida})"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class ArtisanProduct(models.Model):
    """
    Extensión del producto genérico con detalles artesanales.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='artisan_details')
    tecnica_usada = models.CharField(max_length=200, help_text="Ej: Torneado, Tejido manual")
    tiempo_estimado_produccion = models.DurationField(null=True, blank=True)
    es_por_encargo = models.BooleanField(default=False)

    def __str__(self):
        return self.product.nombre

    class Meta:
        app_label = 'prestadores'

class WorkshopOrder(TenantAwareModel):
    """
    Órdenes de trabajo específicas para el taller (Proyectos a medida).
    """
    class OrderStatus(models.TextChoices):
        DISENO = 'DISENO', _('En Diseño')
        MATERIALES = 'MATERIALES', _('Preparación de Materiales')
        PRODUCCION = 'PRODUCCION', _('En Producción')
        ACABADO = 'ACABADO', _('En Acabado')
        TERMINADO = 'TERMINADO', _('Terminado')
        ENTREGADO = 'ENTREGADO', _('Entregado')

    cliente_ref_id = models.UUIDField()
    artisan_product = models.ForeignKey(ArtisanProduct, on_delete=models.PROTECT)
    especificaciones = models.TextField(blank=True)
    fecha_entrega_prometida = models.DateField()
    estado = models.CharField(max_length=30, choices=OrderStatus.choices, default=OrderStatus.DISENO)

    total_precio = models.DecimalField(max_digits=12, decimal_places=2)
    anticipo_pagado = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Orden {self.id} - {self.artisan_product.product.nombre}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class ProductionLog(models.Model):
    """
    Seguimiento de las etapas de producción de una pieza.
    """
    order = models.ForeignKey(WorkshopOrder, on_delete=models.CASCADE, related_name='production_logs')
    etapa = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    evidencia_ref_id = models.UUIDField(null=True, blank=True) # Ref a Galería/Archivo

    class Meta:
        app_label = 'prestadores'

class MaterialConsumption(models.Model):
    """
    Registro de qué materiales se usaron en qué orden.
    """
    order = models.ForeignKey(WorkshopOrder, on_delete=models.CASCADE, related_name='consumptions')
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    cantidad_usada = models.DecimalField(max_digits=12, decimal_places=2)
    costo_aplicado = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'prestadores'
