from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Empleado(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_empleados')
    nombre = models.CharField(max_length=200)
    documento = models.CharField(max_length=20, unique=True)

    class Meta:
        app_label = 'admin_nomina'

class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='admin_contratos')
    fecha_inicio = models.DateField()
    salario_base = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_nomina'

class ConceptoNomina(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)

    class Meta:
        app_label = 'admin_nomina'

class Planilla(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_planillas')
    mes = models.IntegerField()
    anio = models.IntegerField()

    class Meta:
        app_label = 'admin_nomina'

class NovedadNomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='admin_novedades')
    concepto = models.ForeignKey(ConceptoNomina, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_nomina'

class DetalleLiquidacion(models.Model):
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='admin_detalles')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    total_devengado = models.DecimalField(max_digits=18, decimal_places=2)
    total_deducciones = models.DecimalField(max_digits=18, decimal_places=2)
    neto_pagar = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_nomina'
