from django.db import models
from django.utils.translation import gettext_lazy as _
from .perfil.models import ProviderProfile

class Reporte(models.Model):
    """
    Modelo para guardar reportes generados o personalizados por el administrador.
    """
    class TipoReporte(models.TextChoices):
        VENTAS = 'VENTAS', _('Ventas')
        OCUPACION = 'OCUPACION', _('Ocupación')
        CLIENTES = 'CLIENTES', _('Clientes')
        PERSONALIZADO = 'PERSONALIZADO', _('Personalizado')

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_reportes')
    nombre_reporte = models.CharField(_("Nombre del Reporte"), max_length=255)
    tipo_reporte = models.CharField(
        _("Tipo de Reporte"),
        max_length=50,
        choices=TipoReporte.choices,
        default=TipoReporte.PERSONALIZADO
    )

    fecha_inicio = models.DateField(_("Fecha de Inicio del Reporte"))
    fecha_fin = models.DateField(_("Fecha de Fin del Reporte"))

    datos = models.JSONField(_("Datos del Reporte"), help_text=_("Almacena los datos agregados del reporte en formato JSON."))

    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[ADMIN] {self.nombre_reporte} ({self.fecha_inicio} - {self.fecha_fin})"

    class Meta:
        app_label = 'admin_operativa'
        verbose_name = "Reporte / Estadística (Admin)"
        verbose_name_plural = "Reportes y Estadísticas (Admin)"
        ordering = ['-fecha_generacion']
