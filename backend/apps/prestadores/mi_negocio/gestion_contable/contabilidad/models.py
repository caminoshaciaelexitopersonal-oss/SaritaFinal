# backend/apps/prestadores/mi_negocio/gestion_contable/models.py
import uuid
from django.db import models
from django.conf import settings
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.core_erp.base.base_models import (
    BaseAccount, BaseJournalEntry, BaseAccountingTransaction, BaseFiscalPeriod
)

class PlanDeCuentas(TenantAwareModel):
    """
    El catálogo de cuentas contables para un prestador (inquilino).
    Cada prestador tendrá su propio plan de cuentas.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Plan de Cuentas: {self.name} para {self.provider.name_comercial}"

    class Meta:
        verbose_name = "Plan de Cuentas"
        verbose_name_plural = "Planes de Cuentas"
        unique_together = ('provider', 'name')


class Cuenta(BaseAccount, TenantAwareModel):
    """
    Una cuenta contable específica dentro de un Plan de Cuentas.
    Las cuentas están anidadas para crear una jerarquía (ej. Activos -> Activos Corrientes -> Caja).
    """
    plan_de_cuentas = models.ForeignKey(PlanDeCuentas, on_delete=models.CASCADE, related_name='cuentas')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    descripcion = models.TextField(blank=True)
    saldo_inicial = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Cuentas Contables"
        unique_together = ('plan_de_cuentas', 'code')
        ordering = ['code']


class PeriodoContable(BaseFiscalPeriod, TenantAwareModel):
    """
    Define un período fiscal (ej. Enero 2024) para registrar transacciones.
    """
    def __str__(self):
        return f"{self.period_start} - {self.period_end}"

    class Meta:
        verbose_name = "Período Contable"
        verbose_name_plural = "Períodos Contables"
        unique_together = ('provider', 'period_start', 'period_end')


class AsientoContable(BaseJournalEntry, TenantAwareModel):
    """
    Un asiento en el libro diario. Es la unidad fundamental de registro contable.
    Agrupa un conjunto de transacciones de débito y crédito que deben balancearse.
    """
    periodo = models.ForeignKey(PeriodoContable, on_delete=models.PROTECT, related_name='asientos')
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Asiento #{self.id} del {self.date}"

    class Meta:
        verbose_name = "Asiento Contable"
        verbose_name_plural = "Asientos Contables"
        ordering = ['-date']


class Transaccion(BaseAccountingTransaction):
    """
    Una línea individual dentro de un Asiento Contable.
    Representa un movimiento de débito o crédito a una cuenta específica.
    """
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE, related_name='transactions')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, related_name='transactions')

    def __str__(self):
        return f"Transacción en {self.cuenta.name} por {'Débito' if self.debit > 0 else 'Crédito'} de {self.debit or self.credit}"

    class Meta:
        verbose_name = "Transacción Contable"
        verbose_name_plural = "Transacciones Contables"
