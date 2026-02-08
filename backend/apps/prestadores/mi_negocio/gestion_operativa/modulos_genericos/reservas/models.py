# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/reservas/models.py
import uuid
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class PoliticaCancelacion(models.Model):
    perfil_ref_id = models.UUIDField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Reserva(models.Model):
    id_publico = models.UUIDField(editable=False, unique=True, null=True)
    class EstadoReserva(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'
        COMPLETADA = 'COMPLETADA', 'Completada'

    perfil_ref_id = models.UUIDField()
    cliente_ref_id = models.UUIDField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=36)
    item_reservado = GenericForeignKey('content_type', 'object_id')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EstadoReserva.choices, default=EstadoReserva.PENDIENTE)
    notas = models.TextField(blank=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    deposito_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)
    documento_archivistico_ref_id = models.UUIDField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id_publico:
            self.id_publico = uuid.uuid4()
        super().save(*args, **kwargs)

class ReservaServicioAdicional(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='servicios_adicionales')
    servicio_ref_id = models.UUIDField()
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
