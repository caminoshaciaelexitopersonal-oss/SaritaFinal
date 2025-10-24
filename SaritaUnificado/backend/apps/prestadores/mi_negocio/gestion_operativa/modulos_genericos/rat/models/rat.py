from django.db import models
from django.utils.translation import gettext_lazy as _
from ...perfil.models import Perfil
from ..utils import rat_directory_path # Importación corregida

class RegistroActividadTuristica(models.Model):
    """
    Modelo para guardar la información y documentos que exige el gobierno
    o las autoridades de turismo (RAT).
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='registros_rat')
    nombre_documento = models.CharField(_("Nombre del Documento o Registro"), max_length=255)
    descripcion = models.TextField(_("Descripción"), blank=True)
    archivo = models.FileField(_("Archivo Adjunto"), upload_to=rat_directory_path, blank=True, null=True)
    fecha_presentacion = models.DateField(_("Fecha de Presentación"))
    entidad_reguladora = models.CharField(_("Entidad Reguladora"), max_length=255, blank=True, help_text=_("Ej: Ministerio de Turismo, DIAN, etc."))

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_documento} - {self.perfil.nombre_comercial}"

    class Meta:
        verbose_name = "Registro de Actividad Turística (RAT)"
        verbose_name_plural = "Registros de Actividad Turística (RAT)"
        ordering = ['-fecha_presentacion']
