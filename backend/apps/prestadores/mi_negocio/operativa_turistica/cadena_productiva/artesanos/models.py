from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class RawMaterial(TenantAwareModel):
    """
    Gestión de materias primas para el taller artesanal.
    Fase 15: Cadena Productiva.
    """
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    stock_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unidad_medida = models.CharField(max_length=50) # Ej: kg, metros, unidades
    punto_reorden = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} ({self.stock_actual} {self.unidad_medida})"

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Materia Prima"
        verbose_name_plural = "Materias Primas"
        app_label = 'prestadores'

class WorkshopOrder(TenantAwareModel):
    """
    Órdenes de producción del taller (Mi Taller).
    """
    class EstadoOrden(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO', 'En Proceso'
        TERMINADO = 'TERMINADO', 'Terminado'
        ENTREGADO = 'ENTREGADO', 'Entregado'
        CANCELADO = 'CANCELADO', 'Cancelada'

    producto_nombre = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_entrega_estimada = models.DateField()
    estado = models.CharField(max_length=20, choices=EstadoOrden.choices, default=EstadoOrden.PENDIENTE)
    cliente_nombre = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Orden: {self.producto_nombre} ({self.estado})"

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Orden de Taller"
        verbose_name_plural = "Órdenes de Taller"
        app_label = 'prestadores'

class ProductionLog(TenantAwareModel):
    """
    Bitácora de producción diaria y consumo de materiales.
    """
    order = models.ForeignKey(WorkshopOrder, on_delete=models.CASCADE, related_name='logs')
    material = models.ForeignKey(RawMaterial, on_delete=models.SET_NULL, null=True, related_name='consumos')
    cantidad_consumida = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_avance = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log: {self.order.producto_nombre} - {self.fecha_registro}"

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Registro de Producción"
        verbose_name_plural = "Registros de Producción"
        app_label = 'prestadores'
