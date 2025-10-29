from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil

User = get_user_model()

class Empleado(models.Model):
    TIPO_DOCUMENTO_CHOICES = [('CC', _('Cédula de Ciudadanía')), ('CE', _('Cédula de Extranjería')), ('PA', _('Pasaporte'))]
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="empleados")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)
    activo = models.BooleanField(default=True)
    def __str__(self): return f"{self.nombre} {self.apellido}"

class ConceptoNomina(models.Model):
    TIPO_CONCEPTO_CHOICES = [('ingreso', _('Ingreso')), ('deduccion', _('Deducción'))]
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CONCEPTO_CHOICES)
    es_fijo = models.BooleanField(default=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    def __str__(self): return f"[{self.codigo}] {self.descripcion}"

class Nomina(models.Model):
    ESTADO_CHOICES = [('borrador', _('Borrador')), ('procesada', _('Procesada')), ('pagada', _('Pagada'))]
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="nominas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador')
    total_ingresos = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_deducciones = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    neto_a_pagar = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    def __str__(self): return f"Nómina de {self.perfil.nombre_comercial} ({self.fecha_inicio} - {self.fecha_fin})"

class DetalleNomina(models.Model):
    nomina = models.ForeignKey(Nomina, on_delete=models.CASCADE, related_name="detalles")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="detalles_nomina")
    concepto = models.ForeignKey(ConceptoNomina, on_delete=models.PROTECT)
    valor_calculado = models.DecimalField(max_digits=12, decimal_places=2)
    class Meta: unique_together = ('nomina', 'empleado', 'concepto')
