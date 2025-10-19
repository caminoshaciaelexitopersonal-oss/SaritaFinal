from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.prestadores.mi_negocio.modelos.clientes import Cliente


class Hotel(models.Model):
    prestador = models.OneToOneField(PrestadorServicio, on_delete=models.CASCADE, primary_key=True, related_name='hotel_profile')
    categoria_estrellas = models.PositiveIntegerField(default=3, help_text=_("Número de estrellas del hotel"))
    reporte_ocupacion_nacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")
    reporte_ocupacion_internacional = models.PositiveIntegerField(default=0, help_text="Exclusivo para hoteles")

    def __str__(self):
        return f"Perfil de Hotel para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Perfil de Hotel"
        verbose_name_plural = "Perfiles de Hotel"

class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='habitaciones')
    nombre_o_numero = models.CharField(max_length=100)

    class Tipo(models.TextChoices):
        INDIVIDUAL = 'INDIVIDUAL', _('Individual')
        DOBLE = 'DOBLE', _('Doble')
        SUITE = 'SUITE', _('Suite')
        FAMILIAR = 'FAMILIAR', _('Familiar')

    tipo_habitacion = models.CharField(max_length=50, choices=Tipo.choices)
    capacidad = models.PositiveIntegerField(default=1)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_o_numero} ({self.hotel.prestador.nombre_negocio})"

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"

class Tarifa(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='tarifas')
    nombre = models.CharField(max_length=150, help_text="Ej: 'Tarifa Fin de Semana', 'Temporada Alta'")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    recurso = GenericForeignKey('content_type', 'object_id')
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.nombre} (${self.precio}) para {self.recurso}"

class Disponibilidad(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='disponibilidades')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    recurso = GenericForeignKey('content_type', 'object_id')
    fecha = models.DateField()
    cupos_totales = models.PositiveIntegerField(default=1)
    cupos_ocupados = models.PositiveIntegerField(default=0)

    @property
    def cupos_disponibles(self):
        return self.cupos_totales - self.cupos_ocupados

    def __str__(self):
        return f"{self.cupos_disponibles} cupos para {self.recurso} el {self.fecha}"

    class Meta:
        unique_together = ('content_type', 'object_id', 'fecha')

class Reserva(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='reservas')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, help_text="Cliente del CRM asociado a la reserva.")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    recurso_reservado = GenericForeignKey('content_type', 'object_id')
    fecha_inicio_reserva = models.DateTimeField()
    fecha_fin_reserva = models.DateTimeField(null=True, blank=True)
    numero_personas = models.PositiveIntegerField(default=1)

    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', _('Pendiente')
        CONFIRMADA = 'CONFIRMADA', _('Confirmada')
        CANCELADA = 'CANCELADA', _('Cancelada')
        COMPLETADA = 'COMPLETADA', _('Completada')

    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    monto_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    notas_reserva = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva para {self.cliente.nombre if self.cliente else 'N/A'} del {self.fecha_inicio_reserva.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['-fecha_inicio_reserva']