from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ...perfil.models import Perfil

class TicketSoporte(models.Model):
    """
    Modelo para gestionar tickets de soporte o ayuda de los prestadores.
    """
    class EstadoTicket(models.TextChoices):
        ABIERTO = 'ABIERTO', _('Abierto')
        EN_PROGRESO = 'EN_PROGRESO', _('En Progreso')
        CERRADO = 'CERRADO', _('Cerrado')

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='tickets_soporte_nuevos') # Renombrado
    asunto = models.CharField(_("Asunto"), max_length=255, blank=True, null=True)
    mensaje = models.TextField(_("Mensaje"), blank=True, null=True)

    estado = models.CharField(
        _("Estado del Ticket"),
        max_length=50,
        choices=EstadoTicket.choices,
        default=EstadoTicket.ABIERTO
    )

    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id}: {self.asunto} - {self.perfil.nombre_comercial}"

    class Meta:
        verbose_name = "Ticket de Soporte"
        verbose_name_plural = "Tickets de Soporte"
        ordering = ['-fecha_creacion']
