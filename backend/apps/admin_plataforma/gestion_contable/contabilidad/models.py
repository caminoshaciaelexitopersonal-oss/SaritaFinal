import uuid
from django.db import models
from django.conf import settings
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class PlanDeCuentas(TenantAwareModel):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"[ADMIN] Plan: {self.nombre}"

    class Meta:
        verbose_name = "Plan de Cuentas (Admin)"
        app_label = 'admin_contabilidad'

class Cuenta(TenantAwareModel):
    class TipoCuenta(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        PASIVO = 'PASIVO', 'Pasivo'
        PATRIMONIO = 'PATRIMONIO', 'Patrimonio'
        INGRESOS = 'INGRESOS', 'Ingresos'
        GASTOS = 'GASTOS', 'Gastos'
        COSTOS = 'COSTOS', 'Costos'

    plan_de_cuentas = models.ForeignKey(PlanDeCuentas, on_delete=models.CASCADE, related_name='admin_cuentas')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='admin_children')
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TipoCuenta.choices)
    saldo_inicial = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        app_label = 'admin_contabilidad'
        unique_together = ('plan_de_cuentas', 'codigo')

class PeriodoContable(TenantAwareModel):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cerrado = models.BooleanField(default=False)

    class Meta:
        app_label = 'admin_contabilidad'

class AsientoContable(TenantAwareModel):
    periodo = models.ForeignKey(PeriodoContable, on_delete=models.PROTECT, related_name='admin_asientos')
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='admin_asientos_creados')

    class Meta:
        app_label = 'admin_contabilidad'

class Transaccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE, related_name='admin_transacciones')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, related_name='admin_transacciones')
    debito = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    credito = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        app_label = 'admin_contabilidad'
