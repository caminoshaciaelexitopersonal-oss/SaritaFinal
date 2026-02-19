import logging
import uuid
import hashlib
from datetime import date
from decimal import Decimal
from django.db import models
from ..models import Subscription
from ..models import BillingCycle
from ..models import UsageMetric
from ..models import PricingRule
from apps.core_erp.billing.billing_engine import BillingEngine as CoreBillingEngine
from apps.core_erp.accounting.accounting_engine import AccountingEngine
from apps.admin_plataforma.gestion_comercial.domain.models import FacturaVenta, OperacionComercial
from apps.admin_plataforma.gestion_contable.contabilidad.models import AdminJournalEntry, AdminAccountingTransaction, AdminAccount, AdminFiscalPeriod

logger = logging.getLogger(__name__)

def uuid_from_string(s):
    return uuid.UUID(hashlib.md5(s.encode()).hexdigest())

class BillingEngine:
    """
    Motor de facturación comercial SaaS.
    Traduce suscripciones en facturas ERP y asientos contables.
    """

    @staticmethod
    def calculate_overage(subscription: Subscription, cycle_start: date, cycle_end: date):
        """Calcula cargos adicionales por exceso de uso."""
        overage_total = Decimal('0.00')
        details = []

        metrics = UsageMetric.objects.filter(
            tenant_id=subscription.tenant_id,
            period_start__gte=cycle_start,
            period_end__lte=cycle_end
        )

        plan = subscription.plan
        rules = PricingRule.objects.filter(plan=plan, is_active=True).first()

        if not rules:
            return overage_total, details

        # Exceso de Almacenamiento
        storage_usage = metrics.filter(metric_type='STORAGE').aggregate(max_qty=models.Max('quantity'))['max_qty'] or 0
        if storage_usage > plan.storage_limit_gb:
            excess = Decimal(str(storage_usage - plan.storage_limit_gb))
            cost = excess * rules.extra_gb_price
            if cost > 0:
                overage_total += cost
                details.append(f"Exceso Almacenamiento: {excess} GB x {rules.extra_gb_price} = {cost}")

        return overage_total, details

    @staticmethod
    def generate_invoice(subscription: Subscription):
        """
        Genera automáticamente la factura para el periodo actual.
        """
        plan = subscription.plan
        base_amount = plan.monthly_price if subscription.billing_cycle == Subscription.BillingCycle.MONTHLY else plan.yearly_price

        cycle_start = date.today().replace(day=1)
        cycle_end = date.today()

        overage_amount, overage_details = BillingEngine.calculate_overage(subscription, cycle_start, cycle_end)
        total_amount = base_amount + overage_amount

        cycle = BillingCycle.objects.create(
            subscription=subscription,
            cycle_start=cycle_start,
            cycle_end=cycle_end,
            amount_calculated=total_amount,
            status=BillingCycle.Status.PENDING,
            total_usage={"overage_details": overage_details}
        )

        tenant_uuid = uuid_from_string(subscription.tenant_id)

        operacion = OperacionComercial.objects.create(
            perfil_ref_id=tenant_uuid,
            total=total_amount,
            estado=OperacionComercial.Estado.CONFIRMADA,
            tipo_operacion=OperacionComercial.TipoOperacion.VENTA
        )

        invoice = FacturaVenta.objects.create(
            operacion=operacion,
            perfil_ref_id=tenant_uuid,
            number=f"SaaS-{subscription.id.hex[:6].upper()}",
            issue_date=date.today(),
            due_date=date.today(),
            total_amount=total_amount,
            status="DRAFT"
        )

        CoreBillingEngine.validate_invoice(invoice)
        invoice.status = "ISSUED"
        invoice.save()

        cycle.invoice_id = invoice.id
        cycle.status = BillingCycle.Status.INVOICED
        cycle.save()

        BillingEngine._create_accounting_impact(invoice)

        logger.info(f"Factura generada para tenant {subscription.tenant_id} por {total_amount}")
        return invoice

    @staticmethod
    def _create_accounting_impact(invoice):
        """Dispara el asiento contable balanceado via Core AccountingEngine."""

        # 1. Obtener Periodo Contable
        period_name = invoice.issue_date.strftime("%Y-%m")
        periodo = AdminFiscalPeriod.objects.filter(name=period_name).first()
        if not periodo:
            periodo = AdminFiscalPeriod.objects.create(
                name=period_name,
                start_date=invoice.issue_date.replace(day=1),
                end_date=invoice.issue_date,
                tenant_id="SARITA_HOLDING"
            )

        # 2. Crear Asiento
        asiento = AdminJournalEntry.objects.create(
            period=periodo,
            date=invoice.issue_date,
            description=f"Facturación SaaS {invoice.number}",
            reference=str(invoice.id),
            is_posted=False,
            tenant_id="SARITA_HOLDING"
        )

        # 3. Crear Transacciones (CxC y Ventas)
        cuenta_ingresos = AdminAccount.objects.filter(code="413501").first()
        cuenta_clientes = AdminAccount.objects.filter(code="130505").first()

        if cuenta_ingresos and cuenta_clientes:
            AdminAccountingTransaction.objects.create(
                journal_entry=asiento,
                account=cuenta_clientes,
                debit=invoice.total_amount,
                credit=0,
                description="CxC suscripción"
            )
            AdminAccountingTransaction.objects.create(
                journal_entry=asiento,
                account=cuenta_ingresos,
                debit=0,
                credit=invoice.total_amount,
                description="Ingresos por suscripciones"
            )

            # 4. Validar y Postear via Engine
            AccountingEngine.post_entry(asiento)
        else:
            logger.error("No se encontraron las cuentas contables 413501 o 130505. El asiento quedó en borrador.")
