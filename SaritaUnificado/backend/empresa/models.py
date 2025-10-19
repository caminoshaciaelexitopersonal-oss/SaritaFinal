from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio

class Vacante(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='vacantes', verbose_name=_("Empresa Ofertante"))
    titulo = models.CharField(_("Título de la Vacante"), max_length=200)
    descripcion = models.TextField(_("Descripción del Puesto"))

    class TipoContrato(models.TextChoices):
        TIEMPO_COMPLETO = 'TIEMPO_COMPLETO', _('Tiempo Completo')
        MEDIO_TIEMPO = 'MEDIO_TIEMPO', _('Medio Tiempo')
        POR_HORAS = 'POR_HORAS', _('Por Horas')
        TEMPORAL = 'TEMPORAL', _('Temporal')
        PRACTICAS = 'PRACTICAS', _('Prácticas / Pasantía')

    tipo_contrato = models.CharField(_("Tipo de Contrato"), max_length=50, choices=TipoContrato.choices)
    ubicacion = models.CharField(_("Ubicación"), max_length=255, help_text="Ej: 'Puerto Gaitán, Meta' o 'Remoto'")
    salario = models.CharField(_("Salario o Rango Salarial"), max_length=150, blank=True, null=True, help_text="Ej: '$2.000.000 - $2.500.000 COP' o 'A convenir'")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(_("Fecha de Vencimiento"), blank=True, null=True)
    activa = models.BooleanField(_("Vacante Activa"), default=True, db_index=True)

    def __str__(self):
        return f"{self.titulo} en {self.empresa.nombre_negocio}"

    class Meta:
        verbose_name = "Vacante de Empleo"
        verbose_name_plural = "Vacantes de Empleo"
        ordering = ['-fecha_publicacion']

class Inventario(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='inventarios')
    nombre_item = models.CharField(_("Nombre del Ítem"), max_length=255)
    descripcion = models.TextField(_("Descripción"), blank=True, null=True)
    cantidad = models.PositiveIntegerField(_("Cantidad Disponible"), default=0)
    unidad = models.CharField(_("Unidad de Medida"), max_length=50, help_text=_("Ej: unidades, kg, litros"))
    punto_reorden = models.PositiveIntegerField(_("Punto de Reorden"), default=0, help_text=_("Cantidad mínima antes de necesitar reabastecimiento"))
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_item} ({self.cantidad} {self.unidad})"

    class Meta:
        verbose_name = "Ítem de Inventario"
        verbose_name_plural = "Ítems de Inventario"
        ordering = ['nombre_item']

class Costo(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='costos')
    concepto = models.CharField(_("Concepto del Costo"), max_length=255)
    monto = models.DecimalField(_("Monto"), max_digits=12, decimal_places=2)
    fecha = models.DateField(_("Fecha del Costo"))
    es_recurrente = models.BooleanField(_("¿Es Recurrente?"), default=False)

    class Tipo(models.TextChoices):
        FIJO = 'FIJO', _('Fijo')
        VARIABLE = 'VARIABLE', _('Variable')

    tipo_costo = models.CharField(_("Tipo de Costo"), max_length=50, choices=Tipo.choices, default=Tipo.VARIABLE)

    def __str__(self):
        return f"{self.concepto} - ${self.monto}"

    class Meta:
        verbose_name = "Costo Operativo"
        verbose_name_plural = "Costos Operativos"
        ordering = ['-fecha']

class Recurso(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='recursos')
    nombre = models.CharField(_("Nombre del Recurso"), max_length=200)

    class Tipo(models.TextChoices):
        HUMANO = 'HUMANO', _('Humano')
        LOGISTICO = 'LOGISTICO', _('Logístico') # Ej: Vehículo, Herramienta
        TECNOLOGICO = 'TECNOLOGICO', _('Tecnológico')

    tipo_recurso = models.CharField(_("Tipo de Recurso"), max_length=50, choices=Tipo.choices)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_recurso_display()})"

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

