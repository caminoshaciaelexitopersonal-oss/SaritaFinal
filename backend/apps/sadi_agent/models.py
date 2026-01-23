from django.conf import settings
from django.db import models

class SadiAuditLog(models.Model):
    """
    Registra cada comando de voz procesado por el Orquestador SADI.
    """
    # El administrador que ejecutó el comando.
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sadi_commands'
    )

    # El texto original del comando de voz.
    comando_original = models.TextField(
        help_text="El comando de voz original en texto plano."
    )

    # La acción estructurada que el LLM interpretó.
    accion_ejecutada = models.JSONField(
        null=True,
        blank=True,
        help_text="La acción y parámetros interpretados por el LLM."
    )

    # El resultado de la operación.
    resultado = models.TextField(
        help_text="El resultado de la ejecución del comando (éxito, error, etc.)."
    )

    # Timestamp de la ejecución.
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora en que se procesó el comando."
    )

    def __str__(self):
        return f"Comando de {self.usuario} a las {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Registro de Auditoría SADI"
        verbose_name_plural = "Registros de Auditoría SADI"
        ordering = ['-timestamp']
