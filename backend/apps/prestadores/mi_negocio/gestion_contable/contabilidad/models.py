# backend/apps/prestadores/mi_negocio/gestion_contable/models.py
import uuid
from django.db import models
from django.conf import settings
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel

class PlanDeCuentas(TenantAwareModel):
    """
    El catálogo de cuentas contables para un prestador (inquilino).
    Cada prestador tendrá su propio plan de cuentas.
    """
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"Plan de Cuentas: {self.nombre} para {self.provider.nombre_comercial}"

    class Meta:
        verbose_name = "Plan de Cuentas"
        verbose_name_plural = "Planes de Cuentas"
        unique_together = ('provider', 'nombre')


class Cuenta(TenantAwareModel):
    """
    Una cuenta contable específica dentro de un Plan de Cuentas.
    Las cuentas están anidadas para crear una jerarquía (ej. Activos -> Activos Corrientes -> Caja).
    """
    class TipoCuenta(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        PASIVO = 'PASIVO', 'Pasivo'
        PATRIMONIO = 'PATRIMONIO', 'Patrimonio'
        INGRESOS = 'INGRESOS', 'Ingresos'
        GASTOS = 'GASTOS', 'Gastos'
        COSTOS = 'COSTOS', 'Costos'

    plan_de_cuentas = models.ForeignKey(PlanDeCuentas, on_delete=models.CASCADE, related_name='cuentas')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TipoCuenta.choices)
    descripcion = models.TextField(blank=True)
    saldo_inicial = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Cuentas Contables"
        unique_together = ('plan_de_cuentas', 'codigo')
        ordering = ['codigo']


class PeriodoContable(TenantAwareModel):
    """
    Define un período fiscal (ej. Enero 2024) para registrar transacciones.
    """
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cerrado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Período Contable"
        verbose_name_plural = "Períodos Contables"
        unique_together = ('provider', 'fecha_inicio', 'fecha_fin')


class AsientoContable(TenantAwareModel):
    """
    Un asiento en el libro diario. Es la unidad fundamental de registro contable.
    Agrupa un conjunto de transacciones de débito y crédito que deben balancearse.
    """
    periodo = models.ForeignKey(PeriodoContable, on_delete=models.PROTECT, related_name='asientos')
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Asiento #{self.id} del {self.fecha}"

    class Meta:
        verbose_name = "Asiento Contable"
        verbose_name_plural = "Asientos Contables"
        ordering = ['-fecha']


class Transaccion(models.Model):
    """
    Una línea individual dentro de un Asiento Contable.
    Representa un movimiento de débito o crédito a una cuenta específica.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE, related_name='transacciones')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, related_name='transacciones')
    debito = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, help_text="Monto que entra o aumenta (Debe).")
    credito = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, help_text="Monto que sale o disminuye (Haber).")
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Transacción en {self.cuenta.nombre} por {'Débito' if self.debito > 0 else 'Crédito'} de {self.debito or self.credito}"

    class Meta:
        verbose_name = "Transacción Contable"
        verbose_name_plural = "Transacciones Contables"
