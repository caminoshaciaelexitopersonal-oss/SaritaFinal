# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/models/restaurantes.py
from django.db import models
from ...modulos_genericos.models.base import Perfil

class CategoriaMenu(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='menu_categorias')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class ProductoMenu(models.Model):
    categoria = models.ForeignKey(CategoriaMenu, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='productos_menu/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Mesa(models.Model):
    UBICACION_CHOICES = [
        ('salon', 'Salón Principal'),
        ('terraza', 'Terraza / Exterior'),
        ('barra', 'Barra'),
        ('privado', 'Salón Privado'),
    ]

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mesas')
    numero = models.CharField(max_length=10, help_text="Número o nombre de la mesa (ej. 'Mesa 5', 'Ventanal')")
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=50, choices=UBICACION_CHOICES, default='salon')
    disponible = models.BooleanField(default=True)

    class Meta:
        unique_together = ('perfil', 'numero')

    def __str__(self):
        return f"Mesa {self.numero} ({self.capacidad} personas) - {self.get_ubicacion_display()}"

class ReservaMesa(models.Model):
    ESTADO_CHOICES = [
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
        ('no_show', 'No Asistió'),
    ]

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='reservas')
    nombre_cliente = models.CharField(max_length=255)
    telefono_cliente = models.CharField(max_length=20, blank=True, null=True)
    fecha_hora = models.DateTimeField()
    numero_personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='confirmada')
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva para {self.nombre_cliente} en Mesa {self.mesa.numero} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"
