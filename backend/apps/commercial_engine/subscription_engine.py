import logging
from datetime import date, timedelta
from .models import SaaSPlan, SaaSSubscription
from apps.core_erp.billing_engine import BillingEngine
from apps.admin_plataforma.gestion_comercial.domain.models import FacturaVenta, OperacionComercial

logger = logging.getLogger(__name__)

class SubscriptionEngine:
    """
    Gestiona el ciclo de vida de las suscripciones SaaS.
    """

    @staticmethod
    def create_subscription(lead, plan):
        subscription = SaaSSubscription.objects.create(
            tenant_id=lead.company_name.lower().replace(" ", "_"),
            plan=plan,
            next_billing_date=date.today() + timedelta(days=30)
        )

        # Generar Factura Inicial Automática
        SubscriptionEngine._generate_initial_invoice(subscription)

        return subscription

    @staticmethod
    def _generate_initial_invoice(subscription):
        # Crear Operación Comercial (Adapter a admin_comercial)
        operacion = OperacionComercial.objects.create(
            perfil_ref_id=subscription.id, # Placeholder
            cliente_ref_id=subscription.id, # Placeholder
            total=subscription.plan.monthly_price,
            estado=OperacionComercial.Estado.CONFIRMADA
        )

        invoice = FacturaVenta.objects.create(
            operacion=operacion,
            number=f"SaaS-{subscription.tenant_id.upper()}-001",
            issue_date=date.today(),
            total_amount=subscription.plan.monthly_price,
            status='DRAFT'
        )

        # Validar y Emitir vía Core ERP
        BillingEngine.issue_invoice(invoice)

        # Impacto Contable (Debe ser automático en SaaS Real)
        SubscriptionEngine._create_accounting_impact(invoice)

        return invoice

    @staticmethod
    def _create_accounting_impact(invoice):
        from apps.core_erp.accounting_engine import AccountingEngine
        from apps.admin_plataforma.gestion_contable.contabilidad.models import (
            AdminJournalEntry, AdminAccountingTransaction, AdminAccount, AdminFiscalPeriod
        )

        # 1. Obtener/Crear Periodo
        period_name = invoice.issue_date.strftime("%Y-%m")
        period, _ = AdminFiscalPeriod.objects.get_or_create(
            name=period_name,
            defaults={'start_date': invoice.issue_date.replace(day=1), 'end_date': invoice.issue_date}
        )

        # 2. Crear Asiento
        entry = AdminJournalEntry.objects.create(
            period=period,
            date=invoice.issue_date,
            description=f"Facturación Automática SaaS - {invoice.number}",
            reference=invoice.number
        )

        # 3. Transacciones (CxC vs Ingresos)
        # Placeholder para códigos de cuenta reales
        acct_receivable, _ = AdminAccount.objects.get_or_create(code="130505", defaults={"name": "Clientes SaaS", "account_type": "ASSET"})
        acct_revenue, _ = AdminAccount.objects.get_or_create(code="413501", defaults={"name": "Ingresos SaaS", "account_type": "REVENUE"})

        AdminAccountingTransaction.objects.create(journal_entry=entry, account=acct_receivable, debit=invoice.total_amount, credit=0)
        AdminAccountingTransaction.objects.create(journal_entry=entry, account=acct_revenue, debit=0, credit=invoice.total_amount)

        # 4. Postear vía Engine
        AccountingEngine.post_entry(entry)
