# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/agencias_de_viajes/models.py
from django.db import models
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from django.conf import settings
# Importamos el modelo canonico para evitar duplicidad
from ..operadores_turisticos.models import PaqueteTuristico

class ReservaPaquete(models.Model):
    """
    Representa una reserva de un paquete turístico por parte de un cliente.
    """
    ESTADO_RESERVA_CHOICES = [
        ('pendiente', 'Pendiente de Confirmación'),
        ('confirmada', 'Confirmada'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE, related_name='reservas')
    # Podría enlazarse con el modelo Cliente si existe y es relevante.
    # cliente = models.ForeignKey('gestion_comercial.Cliente', on_delete=models.SET_NULL, null=True, blank=True)
    nombre_cliente_temporal = models.CharField(max_length=150, help_text="Nombre del cliente que hace la reserva")
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=20, blank=True)

    fecha_inicio = models.DateField()
    numero_de_personas = models.PositiveIntegerField(default=1)
    costo_total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=15, choices=ESTADO_RESERVA_CHOICES, default='pendiente')
    notas_especiales = models.TextField(blank=True, help_text="Requerimientos o notas especiales del cliente.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Calcula el costo total al guardar la reserva si no se ha especificado
        if not self.costo_total:
            # El precio viene del 'producto' base asociado al paquete
            self.costo_total = self.paquete.producto.base_price * self.numero_de_personas
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva de {self.paquete.producto.nombre} para {self.nombre_cliente_temporal} el {self.fecha_inicio}"
