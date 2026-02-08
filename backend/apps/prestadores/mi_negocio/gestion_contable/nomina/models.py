from django.db import models
import uuid
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Empleado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='empleados')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    framework_legal = models.CharField(max_length=50, default='CO') # ej: CO, MX, ES

    class Meta: app_label = 'nomina'

class Contrato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='contratos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=18, decimal_places=2)
    cargo = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=50, default='TERMINO_INDEFINIDO')
    activo = models.BooleanField(default=True)
    evidencia_archivistica_ref_id = models.UUIDField(null=True, blank=True)

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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='planillas')
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    total_devengado = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_deduccion = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_neto = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=20, choices=EstadoPlanilla.choices, default=EstadoPlanilla.BORRADOR)

    asiento_contable_ref_id = models.UUIDField(null=True, blank=True)
    orden_pago_ref_id = models.UUIDField(null=True, blank=True)
    evidencia_archivistica_ref_id = models.UUIDField(null=True, blank=True)

    class Meta: app_label = 'nomina'

class DetalleLiquidacion(models.Model):
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='detalles_liquidacion')
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='liquidaciones')
    salario_base = models.DecimalField(max_digits=18, decimal_places=2)
    dias_trabajados = models.IntegerField()
    total_devengado = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_deduccion = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    total_neto = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
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

class IncapacidadLaboral(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    incidente_sst_ref_id = models.UUIDField(null=True, blank=True) # Link to SG-SST
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_incapacidad = models.CharField(max_length=100) # Común, Laboral
    diagnostico = models.TextField()
    estado = models.CharField(max_length=20, default='PENDIENTE')
    class Meta: app_label = 'nomina'

class Ausencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50) # Permiso, Licencia no remunerada, etc.
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    justificada = models.BooleanField(default=False)
    class Meta: app_label = 'nomina'

class ProvisionNomina(models.Model):
    """
    Causación mensual de prestaciones sociales.
    """
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    periodo_mes = models.IntegerField()
    periodo_anio = models.IntegerField()
    tipo_prestacion = models.CharField(max_length=50) # Prima, Cesantías, etc.
    monto_total = models.DecimalField(max_digits=18, decimal_places=2)
    asiento_contable_ref_id = models.UUIDField(null=True, blank=True)
    class Meta: app_label = 'nomina'
