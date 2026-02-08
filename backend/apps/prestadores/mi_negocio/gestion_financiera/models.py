# backend/apps/prestadores/mi_negocio/gestion_financiera/models.py
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
# from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import ChartOfAccount
from .statements_models import *

class TesoreriaCentral(TenantAwareModel):
    """
    Entidad de gobierno central para la custodia de fondos.
    """
    saldo_total_custodia = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    reservas_totales = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    liquidez_disponible = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    ultima_conciliacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Tesorería Central"
        verbose_name_plural = "Tesorerías Centrales"

class CuentaBancaria(models.Model):
    perfil_ref_id = models.UUIDField()
    banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=50, unique=True)
    tipo_cuenta = models.CharField(max_length=50)
    saldo_inicial = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    saldo_actual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    cuenta_contable_ref_id = models.UUIDField(null=True)
    activa = models.BooleanField(default=True)

class OrdenPago(models.Model):
    class EstadoPago(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        PAGADA = 'PAGADA', 'Pagada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    perfil_ref_id = models.UUIDField()
    cuenta_bancaria_ref_id = models.UUIDField()

    # Patrón de beneficiario genérico explícito según la Directriz 14.4
    beneficiario_id = models.UUIDField(null=True, help_text="ID del beneficiario (Cliente, Proveedor, Empleado, etc.)")
    tipo_beneficiario = models.CharField(max_length=100, null=True, help_text="Tipo de beneficiario para resolución por servicio.")

    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    concepto = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=EstadoPago.choices, default=EstadoPago.PENDIENTE)
    referencia_pago = models.CharField(max_length=100, blank=True)

    documento_archivistico_ref_id = models.UUIDField(null=True, blank=True)
