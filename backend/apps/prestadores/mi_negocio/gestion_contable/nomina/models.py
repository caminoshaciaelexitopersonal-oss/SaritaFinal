from django.db import models
from backend.apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Empleado(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='empleados')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    class Meta: app_label = 'nomina'

class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='contratos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=18, decimal_places=2)
    cargo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    class Meta: app_label = 'nomina'

class ConceptoNomina(models.Model):
    class TipoConcepto(models.TextChoices):
        DEVENGADO = 'DEVENGADO', 'Devengado'
        DEDUCCION = 'DEDUCCION', 'Deducción'
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TipoConcepto.choices)
    class Meta: app_label = 'nomina'

class Planilla(models.Model):
    class EstadoPlanilla(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        LIQUIDADA = 'LIQUIDADA', 'Liquidada'
        CONTABILIZADA = 'CONTABILIZADA', 'Contabilizada'
        PAGADA = 'PAGADA', 'Pagada'
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='planillas')
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    total_devengado = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_deduccion = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_neto = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=20, choices=EstadoPlanilla.choices, default=EstadoPlanilla.BORRADOR)
    class Meta: app_label = 'nomina'

class DetalleLiquidacion(models.Model):
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='detalles_liquidacion')
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='liquidaciones')
    salario_base = models.DecimalField(max_digits=18, decimal_places=2)
    dias_trabajados = models.IntegerField()
    valor_prima = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_cesantias = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_intereses_cesantias = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_vacaciones = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_aporte_ccf = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_aporte_icbf = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    valor_aporte_sena = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    class Meta: app_label = 'nomina'

class NovedadNomina(models.Model):
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='novedades')
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    concepto = models.ForeignKey(ConceptoNomina, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=18, decimal_places=2)
    descripcion = models.TextField(blank=True)
    class Meta: app_label = 'nomina'
