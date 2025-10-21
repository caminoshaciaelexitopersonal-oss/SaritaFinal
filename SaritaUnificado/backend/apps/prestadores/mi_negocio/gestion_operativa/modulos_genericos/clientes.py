from django.db import models
from django.utils.translation import gettext_lazy as _
from .perfil import Perfil

class Cliente(models.Model):
    """
    Modelo para gestionar los clientes (CRM) de un prestador de servicios.
    """
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(_("Nombre del Cliente"), max_length=255)
    email = models.EmailField(_("Correo Electrónico"), max_length=255, unique=True, blank=True, null=True)
    telefono = models.CharField(_("Teléfono"), max_length=50, blank=True)
    notas = models.TextField(_("Notas Internas"), blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - Cliente de {self.perfil.nombre_comercial}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']
