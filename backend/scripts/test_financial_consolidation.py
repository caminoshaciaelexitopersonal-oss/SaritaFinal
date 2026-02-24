import os
import django
import uuid
from decimal import Decimal
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.core_erp.tenancy.models import Tenant
from apps.core_erp.accounting.models import Account, ChartOfAccounts, FiscalPeriod
from apps.core_erp.accounting.ledger_engine import LedgerEngine
from apps.core_erp.consolidation.models import HoldingEntity, HoldingMembership, IntercompanyAccountMapping
from apps.core_erp.consolidation.consolidation_engine import ConsolidationEngine
from apps.core_erp.consolidation.reports import ConsolidationReports

def test_consolidation():
    print("Starting Financial Consolidation Test...")

    # 1. Create Holding
    holding = HoldingEntity.objects.create(name="Sarita Holding", base_currency="COP")

    # 2. Create Tenants
    t1 = Tenant.objects.create(name="Subsidiary A", tax_id="SubA-" + str(uuid.uuid4())[:8], currency="COP")
    t2 = Tenant.objects.create(name="Subsidiary B", tax_id="SubB-" + str(uuid.uuid4())[:8], currency="USD")

    # 3. Setup Memberships
    HoldingMembership.objects.create(holding=holding, tenant=t1, ownership_percentage=100)
    HoldingMembership.objects.create(holding=holding, tenant=t2, ownership_percentage=80, consolidation_method='PROPORTIONAL')

    # 4. Setup Intercompany Mapping
    IntercompanyAccountMapping.objects.create(holding=holding, account_name_pattern="Intercompany")

    # 5. Add some data to T1
    coa1 = ChartOfAccounts.objects.create(tenant=t1, name="COA A")
    cutoff_date = timezone.now().date()
    FiscalPeriod.objects.get_or_create(
        tenant=t1,
        period_start=cutoff_date.replace(day=1),
        period_end=cutoff_date.replace(day=28),
        defaults={'status': 'open'}
    )

    # Accounts for T1
    Account.objects.get_or_create(tenant=t1, chart_of_accounts=coa1, code="110505", defaults={'name': "Caja A"})
    Account.objects.get_or_create(tenant=t1, chart_of_accounts=coa1, code="413501", defaults={'name': "Ventas A"})
    Account.objects.get_or_create(tenant=t1, chart_of_accounts=coa1, code="130510", defaults={'name': "Intercompany Receivable B"})

    LedgerEngine.post_event("MANUAL_ENTRY", {
        "tenant_id": str(t1.id),
        "reference": "OP1",
        "lines": [
            {"account": "110505", "debit": 100000, "credit": 0},
            {"account": "413501", "debit": 0, "credit": 100000}
        ]
    })

    LedgerEngine.post_event("MANUAL_ENTRY", {
        "tenant_id": str(t1.id),
        "reference": "IC1",
        "lines": [
            {"account": "130510", "debit": 50000, "credit": 0},
            {"account": "413501", "debit": 0, "credit": 50000}
        ]
    })

    # 6. Add some data to T2 (USD)
    coa2 = ChartOfAccounts.objects.create(tenant=t2, name="COA B")
    FiscalPeriod.objects.get_or_create(
        tenant=t2,
        period_start=cutoff_date.replace(day=1),
        period_end=cutoff_date.replace(day=28),
        defaults={'status': 'open'}
    )

    Account.objects.get_or_create(tenant=t2, chart_of_accounts=coa2, code="110505", defaults={'name': "Caja B"})
    Account.objects.get_or_create(tenant=t2, chart_of_accounts=coa2, code="413501", defaults={'name': "Ventas B"})
    Account.objects.get_or_create(tenant=t2, chart_of_accounts=coa2, code="233510", defaults={'name': "Intercompany Payable A"})

    LedgerEngine.post_event("MANUAL_ENTRY", {
        "tenant_id": str(t2.id),
        "reference": "OP2",
        "lines": [
            {"account": "110505", "debit": 10, "credit": 0},
            {"account": "413501", "debit": 0, "credit": 10}
        ]
    })

    # 7. Run Consolidation
    print("\nRunning Consolidation...")
    result = ConsolidationReports.get_consolidated_balance_sheet(str(holding.id), cutoff_date)

    print(f"Consolidated Assets: {result['assets']}")
    print(f"Consolidated Liabilities: {result['liabilities']}")
    print(f"Consolidated Equity: {result['equity']}")

    expected_assets = Decimal('132000')
    if result['assets'] == expected_assets:
        print(f"SUCCESS: Assets match expected {expected_assets}")
    else:
        print(f"FAILED: Expected {expected_assets}, got {result['assets']}")

    print("\nCONSOLIDATION TEST COMPLETED!")

if __name__ == "__main__":
    test_consolidation()
