from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil

# Obtener el modelo de usuario personalizado
User = get_user_model()

class Empleado(models.Model):
    """
    Modelo para gestionar los empleados de un prestador de servicios.
    """
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', _('Cédula de Ciudadanía')),
        ('CE', _('Cédula de Extranjería')),
        ('PA', _('Pasaporte')),
    ]

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name="empleados",
        verbose_name=_("Perfil del Prestador")
    )
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    apellido = models.CharField(max_length=100, verbose_name=_("Apellido"))
    tipo_documento = models.CharField(
        max_length=2,
        choices=TIPO_DOCUMENTO_CHOICES,
        verbose_name=_("Tipo de Documento")
    )
    numero_documento = models.CharField(max_length=20, unique=True, verbose_name=_("Número de Documento"))
    fecha_nacimiento = models.DateField(verbose_name=_("Fecha de Nacimiento"))
    fecha_contratacion = models.DateField(verbose_name=_("Fecha de Contratación"))
    salario_base = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Salario Base"))
    activo = models.BooleanField(default=True, verbose_name=_("Activo"))

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = _("Empleado")
        verbose_name_plural = _("Empleados")
        ordering = ['-activo', 'nombre', 'apellido']


class ConceptoNomina(models.Model):
    """
    Modelo para definir los conceptos de la nómina (ingresos, deducciones, etc.).
    """
    TIPO_CONCEPTO_CHOICES = [
        ('ingreso', _('Ingreso')),
        ('deduccion', _('Deducción')),
    ]

    codigo = models.CharField(max_length=10, unique=True, verbose_name=_("Código"))
    descripcion = models.CharField(max_length=255, verbose_name=_("Descripción"))
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CONCEPTO_CHOICES,
        verbose_name=_("Tipo de Concepto")
    )
    es_fijo = models.BooleanField(
        default=True,
        verbose_name=_("¿Es un valor fijo?"),
        help_text=_("Marcar si este concepto es un valor fijo o un porcentaje.")
    )
    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_("Valor/Porcentaje"),
        help_text=_("Valor fijo o porcentaje (ej. 0.04 para 4%).")
    )

    def __str__(self):
        return f"[{self.codigo}] {self.descripcion}"

    class Meta:
        verbose_name = _("Concepto de Nómina")
        verbose_name_plural = _("Conceptos de Nómina")


class Nomina(models.Model):
    """
    Modelo que representa una corrida de nómina para un período específico.
    """
    ESTADO_CHOICES = [
        ('borrador', _('Borrador')),
        ('procesada', _('Procesada')),
        ('pagada', _('Pagada')),
    ]

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name="nominas",
        verbose_name=_("Perfil del Prestador")
    )
    fecha_inicio = models.DateField(verbose_name=_("Fecha de Inicio"))
    fecha_fin = models.DateField(verbose_name=_("Fecha de Fin"))
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de Creación"))
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='borrador',
        verbose_name=_("Estado")
    )
    total_ingresos = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name=_("Total Ingresos"))
    total_deducciones = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name=_("Total Deducciones"))
    neto_a_pagar = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name=_("Neto a Pagar"))

    def __str__(self):
        return f"Nómina de {self.perfil.nombre_comercial} ({self.fecha_inicio} - {self.fecha_fin})"

    class Meta:
        verbose_name = _("Nómina")
        verbose_name_plural = _("Nóminas")
        ordering = ['-fecha_inicio']


class DetalleNomina(models.Model):
    """
    Almacena el valor de cada concepto para un empleado en una corrida de nómina.
    """
    nomina = models.ForeignKey(
        Nomina,
        on_delete=models.CASCADE,
        related_name="detalles",
        verbose_name=_("Nómina")
    )
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name="detalles_nomina",
        verbose_name=_("Empleado")
    )
    concepto = models.ForeignKey(
        ConceptoNomina,
        on_delete=models.PROTECT,
        verbose_name=_("Concepto")
    )
    valor_calculado = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Valor Calculado")
    )

    def __str__(self):
        return f"{self.empleado} - {self.concepto}: {self.valor_calculado}"

    class Meta:
        verbose_name = _("Detalle de Nómina")
        verbose_name_plural = _("Detalles de Nómina")
        unique_together = ('nomina', 'empleado', 'concepto')
