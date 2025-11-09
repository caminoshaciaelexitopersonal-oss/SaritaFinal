from django.db import models
from django.conf import settings
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Empleado(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='empleados')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='contratos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=18, decimal_places=2)
    cargo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Contrato de {self.empleado} - {self.cargo}"

class ConceptoNomina(models.Model):
    class TipoConcepto(models.TextChoices):
        DEVENGADO = 'DEVENGADO', 'Devengado'
        DEDUCCION = 'DEDUCCION', 'Deducción'

    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TipoConcepto.choices)

    def __str__(self):
        return self.descripcion

class Planilla(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='planillas')
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    total_devengado = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_deduccion = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_neto = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Planilla {self.periodo_inicio} a {self.periodo_fin}"

class NovedadNomina(models.Model):
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='novedades')
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    concepto = models.ForeignKey(ConceptoNomina, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=18, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.concepto} - {self.empleado}: {self.valor}"
