from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio

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


class GuiaTuristico(models.Model):
    prestador = models.OneToOneField(PrestadorServicio, on_delete=models.CASCADE, primary_key=True, related_name='guia_profile')
    idiomas = models.CharField(max_length=200, help_text=_("Idiomas que domina, separados por coma"))
    especialidades = models.TextField(blank=True, help_text=_("Áreas de especialización, ej: Ecoturismo, Historia, Aventura"))
    rutas_asignadas = models.ManyToManyField('api.RutaTuristica', blank=True, related_name='guias_asignados')

    def __str__(self):
        return f"Perfil de Guía para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Perfil de Guía Turístico"
        verbose_name_plural = "Perfiles de Guías Turísticos"


class VehiculoTuristico(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    class Tipo(models.TextChoices):
        BUS = 'BUS', _('Autobús')
        BUSETA = 'BUSETA', _('Buseta')
        VAN = 'VAN', _('Van de Turismo')
        AUTOMOVIL = 'AUTOMOVIL', _('Automóvil Particular')
        CHIVA = 'CHIVA', _('Chiva Turística')
        LANCHA = 'LANCHA', _('Lancha Fluvial')

    tipo_vehiculo = models.CharField(max_length=50, choices=Tipo.choices)
    capacidad = models.PositiveIntegerField()
    documentacion_al_dia = models.BooleanField(default=True, help_text=_("Indica si el SOAT, tecnomecánica, y otros permisos están vigentes."))
    foto = models.ImageField(upload_to='vehiculos/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa}) - {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Vehículo Turístico"
        verbose_name_plural = "Vehículos Turísticos"


class PaqueteTuristico(models.Model):
    prestador_agencia = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='paquetes_ofrecidos', help_text=_("La agencia de viajes que crea y vende el paquete."))
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    # Simple fields for now, can be expanded to ManyToMany later if needed
    servicios_incluidos = models.TextField(help_text=_("Descripción de los servicios incluidos (ej. Alojamiento, Transporte, Guía)."))

    atractivos = models.ManyToManyField('api.AtractivoTuristico', blank=True, related_name='paquetes')

    precio_por_persona = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.PositiveIntegerField(default=1)

    es_publico = models.BooleanField(default=False, help_text=_("Marcar para que el paquete sea visible al público."))

    def __str__(self):
        return f"{self.nombre} - {self.prestador_agencia.nombre_negocio}"

    class Meta:
        verbose_name = "Paquete Turístico"
        verbose_name_plural = "Paquetes Turísticos"