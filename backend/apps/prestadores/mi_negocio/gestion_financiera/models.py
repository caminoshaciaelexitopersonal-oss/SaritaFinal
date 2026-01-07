from django.db import models
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import ChartOfAccount
from ..gestion_contable.empresa.models import Tercero

class CuentaBancaria(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='cuentas_bancarias')
    banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=50, unique=True)
    tipo_cuenta = models.CharField(max_length=50)
    saldo_inicial = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    saldo_actual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    cuenta_contable = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, related_name='cuenta_bancaria_asociada', null=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.banco} - {self.numero_cuenta}"

class OrdenPago(models.Model):
    class EstadoPago(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        PAGADA = 'PAGADA', 'Pagada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='ordenes_pago')
    cuenta_bancaria_origen = models.ForeignKey(CuentaBancaria, on_delete=models.PROTECT, related_name='pagos_realizados')
    beneficiario_empleado = models.ForeignKey(
        'nomina.Empleado',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='pagos_recibidos'
    )
    beneficiario_tercero = models.ForeignKey(
        'empresa.Tercero',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='pagos_recibidos'
    )
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    concepto = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=EstadoPago.choices, default=EstadoPago.PENDIENTE)
    referencia_pago = models.CharField(max_length=100, blank=True)

    def __str__(self):
        beneficiario = self.beneficiario_empleado or self.beneficiario_tercero
        return f"Pago a {beneficiario} por {self.monto} - {self.estado}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(beneficiario_empleado__isnull=False, beneficiario_tercero__isnull=True) |
                    models.Q(beneficiario_empleado__isnull=True, beneficiario_tercero__isnull=False)
                ),
                name='un_solo_beneficiario_por_pago'
            )
        ]
