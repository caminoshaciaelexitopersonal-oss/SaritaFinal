from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from api.models import PrestadorServicio, CustomUser

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


class ReservaTuristica(models.Model):
    class EstadoReserva(models.TextChoices):
        PENDIENTE = 'PENDIENTE', _('Pendiente')
        CONFIRMADA = 'CONFIRMADA', _('Confirmada')
        CANCELADA = 'CANCELADA', _('Cancelada')
        COMPLETADA = 'COMPLETADA', _('Completada')

    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='reservas_turismo')
    usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservas_realizadas')
    fecha_inicio_reserva = models.DateTimeField(default=timezone.now)
    fecha_fin_reserva = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EstadoReserva.choices, default=EstadoReserva.PENDIENTE)
    monto_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    notas_adicionales = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva de {self.usuario.username if self.usuario else 'N/A'} para {self.prestador.nombre_negocio} - {self.estado}"

    class Meta:
        verbose_name = "Reserva Turística"
        verbose_name_plural = "Reservas Turísticas"
        ordering = ['-fecha_inicio_reserva']


class GuiaTuristico(models.Model):
    prestador = models.OneToOneField(PrestadorServicio, on_delete=models.CASCADE, primary_key=True, related_name='perfil_guia')
    idiomas = models.CharField(max_length=255, help_text=_("Idiomas que domina, separados por coma"))
    especialidades = models.CharField(max_length=255, help_text=_("Áreas de especialidad, ej: Avistamiento de aves, Historia"))
    experiencia_anos = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Perfil de Guía para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Perfil de Guía Turístico"
        verbose_name_plural = "Perfiles de Guía Turístico"


class VehiculoTuristico(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()

    class TipoVehiculo(models.TextChoices):
        BUS = 'BUS', _('Bus')
        BUSETA = 'BUSETA', _('Buseta')
        VAN = 'VAN', _('Van')
        AUTOMOVIL = 'AUTOMOVIL', _('Automóvil')
        CAMPERO = 'CAMPERO', _('Campero')
        LANCHA = 'LANCHA', _('Lancha')

    tipo = models.CharField(max_length=20, choices=TipoVehiculo.choices)
    documentacion_al_dia = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa}) - {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Vehículo Turístico"
        verbose_name_plural = "Vehículos Turísticos"


class PaqueteTuristico(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='paquetes_turisticos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio_validez = models.DateField()
    fecha_fin_validez = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Paquete Turístico"
        verbose_name_plural = "Paquetes Turísticos"