from django.db import models
from api.models import PrestadorServicio

class Cliente(models.Model):
    """Modelo para un cliente real (CRM)."""
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='clientes_crm')
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    notas = models.TextField(blank=True, null=True, help_text="Notas internas sobre el cliente.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente: {self.nombre} - {self.prestador.nombre_negocio}"

    class Meta:
        db_table = 'empresa_cliente'
        verbose_name = "Cliente (CRM)"
        verbose_name_plural = "Clientes (CRM)"
        unique_together = ('prestador', 'email')
        ordering = ['nombre']