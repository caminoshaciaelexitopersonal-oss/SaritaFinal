# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/models/transporte.py
from django.db import models
from ...modulos_genericos.models.base import Perfil
from django.conf import settings

class Vehiculo(models.Model):
    TIPO_VEHICULO_CHOICES = [
        ('automovil', 'Automóvil'),
        ('camioneta', 'Camioneta / SUV'),
        ('van', 'Van / Microbús'),
        ('bus', 'Autobús'),
        ('chiva', 'Chiva / Bus Escalera'),
        ('otro', 'Otro'),
    ]

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    capacidad_pasajeros = models.PositiveIntegerField()
    tipo_vehiculo = models.CharField(max_length=50, choices=TIPO_VEHICULO_CHOICES)
    foto = models.ImageField(upload_to='vehiculos_transporte/', blank=True, null=True)
    soat_vigente = models.BooleanField(default=True, help_text="¿El SOAT está vigente?")
    tecnomecanica_vigente = models.BooleanField(default=True, help_text="¿La revisión tecnomecánica está vigente?")

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['marca', 'modelo']

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

class Conductor(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='conductores')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        help_text="Opcional: vincular a una cuenta de usuario del sistema."
    )
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='conductores/', blank=True, null=True)
    licencia_conduccion = models.CharField(max_length=50, help_text="Número de la licencia")
    vencimiento_licencia = models.DateField()

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"
