import logging
from decimal import Decimal
from apps.core_erp.event_bus import EventBus
from .models import AdminJournalEntry, AdminAccountingTransaction, AdminChartOfAccounts

logger = logging.getLogger(__name__)

def handle_financial_impact_request(payload):
    """
    Listener for FINANCIAL_IMPACT_REQUESTED events.
    Translates DTO-like payload into Ledger entries.
    """
    tenant_id = payload.get('tenant_id')
    event_type = payload.get('event_type')
    impacts = payload.get('impacts', [])

    logger.info(f"Processing financial impact for {event_type} (Tenant: {tenant_id})")

    try:
        journal_entry = AdminJournalEntry.objects.create(
            tenant_id=tenant_id,
            date=payload.get('date'),
            description=payload.get('description'),
            reference=payload.get('reference'),
        )

        for impact in impacts:
            account_code = impact.get('account_code')
            try:
                account = AdminChartOfAccounts.objects.get(tenant_id=tenant_id, code=account_code)
                AdminAccountingTransaction.objects.create(
                    entry=journal_entry,
                    account=account,
                    debit=Decimal(impact.get('debit', '0.00')),
                    credit=Decimal(impact.get('credit', '0.00')),
                    description=payload.get('description')
                )
            except AdminChartOfAccounts.DoesNotExist:
                logger.error(f"Account {account_code} not found for tenant {tenant_id}")
                # In a real system, this might trigger an alert or a suspense account entry

        logger.info(f"Journal Entry {journal_entry.id} created successfully via EventBus")

    except Exception as e:
        logger.error(f"Failed to process financial impact: {e}")
        raise

# Register the listener
EventBus.subscribe("FINANCIAL_IMPACT_REQUESTED", handle_financial_impact_request)
