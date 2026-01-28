from django.db import models
from django.conf import settings
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class PoliticaCancelacion(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='politicas_cancelacion')
    nombre = models.CharField(max_length=100, help_text="Ej: Estricta, Flexible, No reembolsable")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    class EstadoReserva(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'
        COMPLETADA = 'COMPLETADA', 'Completada'

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='reservas')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='reservas')

    # Para vincular a un objeto específico (Habitación, Mesa, Tour, etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item_reservado = GenericForeignKey('content_type', 'object_id')

    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    estado = models.CharField(max_length=20, choices=EstadoReserva.choices, default=EstadoReserva.PENDIENTE)
    notas = models.TextField(blank=True)

    # Información financiera
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    deposito_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva #{self.id} para {self.cliente.nombre}"

class ReservaServicioAdicional(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='servicios_adicionales')
    servicio = models.ForeignKey('prestadores.Product', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio en el momento de la reserva")

    def __str__(self):
        return f"{self.cantidad} x {self.servicio.nombre} para Reserva #{self.reserva.id}"
