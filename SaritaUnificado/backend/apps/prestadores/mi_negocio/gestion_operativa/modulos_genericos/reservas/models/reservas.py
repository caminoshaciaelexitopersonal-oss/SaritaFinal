from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ...perfil.models import Perfil
from ...models.crm import Cliente
from ...productos_servicios.models import ProductoServicio

class Reserva(models.Model):
    """
    Modelo para gestionar las reservas o citas de un prestador.
    """
    class EstadoReserva(models.TextChoices):
        PENDIENTE = 'PENDIENTE', _('Pendiente')
        CONFIRMADA = 'CONFIRMADA', _('Confirmada')
        CANCELADA = 'CANCELADA', _('Cancelada')
        COMPLETADA = 'COMPLETADA', _('Completada')

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='reservas_citas') # Renombrado
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservas')
    producto_servicio = models.ForeignKey(ProductoServicio, on_delete=models.SET_NULL, null=True, blank=True)

    fecha_hora_inicio = models.DateTimeField(_("Fecha y Hora de Inicio"), blank=True, null=True)
    fecha_hora_fin = models.DateTimeField(_("Fecha y Hora de Fin"), null=True, blank=True)

    estado = models.CharField(
        _("Estado de la Reserva"),
        max_length=50,
        choices=EstadoReserva.choices,
        default=EstadoReserva.PENDIENTE
    )

    notas = models.TextField(_("Notas Adicionales"), blank=True)
    monto_total = models.DecimalField(_("Monto Total"), max_digits=12, decimal_places=2, default=0.00)

    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva para {self.cliente.nombre if self.cliente else 'N/A'} - {self.fecha_hora_inicio.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Reserva / Cita"
        verbose_name_plural = "Reservas y Citas"
        ordering = ['-fecha_hora_inicio']
