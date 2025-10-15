from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio

class Producto(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

class RegistroCliente(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='registros_clientes')
    pais_origen = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_registro = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} cliente(s) de {self.pais_origen} para {self.prestador.nombre_negocio}"

    class Meta:
        verbose_name = "Registro de Cliente"
        verbose_name_plural = "Registros de Clientes"
        ordering = ['-fecha_registro']

class Vacante(models.Model):
    empresa = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='vacantes', verbose_name=_("Empresa Ofertante"))
    titulo = models.CharField(_("Título de la Vacante"), max_length=200)
    descripcion = models.TextField(_("Descripción del Puesto"))

    class TipoContrato(models.TextChoices):
        TIEMPO_COMPLETO = 'TIEMPO_COMPLETO', _('Tiempo Completo')
        MEDIO_TIEMPO = 'MEDIO_TIEMPO', _('Medio Tiempo')
        POR_HORAS = 'POR_HORAS', _('Por Horas')
        TEMPORAL = 'TEMPORAL', _('Temporal')
        PRACTICAS = 'PRACTICAS', _('Prácticas / Pasantía')

    tipo_contrato = models.CharField(_("Tipo de Contrato"), max_length=50, choices=TipoContrato.choices)
    ubicacion = models.CharField(_("Ubicación"), max_length=255, help_text="Ej: 'Puerto Gaitán, Meta' o 'Remoto'")
    salario = models.CharField(_("Salario o Rango Salarial"), max_length=150, blank=True, null=True, help_text="Ej: '$2.000.000 - $2.500.000 COP' o 'A convenir'")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(_("Fecha de Vencimiento"), blank=True, null=True)
    activa = models.BooleanField(_("Vacante Activa"), default=True, db_index=True)

    def __str__(self):
        return f"{self.titulo} en {self.empresa.nombre_negocio}"

    class Meta:
        verbose_name = "Vacante de Empleo"
        verbose_name_plural = "Vacantes de Empleo"
        ordering = ['-fecha_publicacion']