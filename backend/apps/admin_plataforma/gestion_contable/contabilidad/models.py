import uuid
from django.db import models
from django.conf import settings
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.core_erp.base.base_models import (
    BaseAccount, BaseJournalEntry, BaseAccountingTransaction, BaseFiscalPeriod
)

class PlanDeCuentas(TenantAwareModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"[ADMIN] Plan: {self.name}"

    class Meta:
        verbose_name = "Plan de Cuentas (Admin)"
        app_label = 'admin_contabilidad'

class Cuenta(BaseAccount, TenantAwareModel):
    plan_de_cuentas = models.ForeignKey(PlanDeCuentas, on_delete=models.CASCADE, related_name='admin_cuentas')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='admin_children')
    saldo_inicial = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    class Meta:
        app_label = 'admin_contabilidad'
        unique_together = ('plan_de_cuentas', 'code')

class PeriodoContable(BaseFiscalPeriod, TenantAwareModel):
    class Meta:
        app_label = 'admin_contabilidad'

class AsientoContable(BaseJournalEntry, TenantAwareModel):
    periodo = models.ForeignKey(PeriodoContable, on_delete=models.PROTECT, related_name='admin_asientos')
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='admin_asientos_creados')

    class Meta:
        app_label = 'admin_contabilidad'

class Transaccion(BaseAccountingTransaction):
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE, related_name='transactions')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, related_name='transactions')

    class Meta:
        app_label = 'admin_contabilidad'
