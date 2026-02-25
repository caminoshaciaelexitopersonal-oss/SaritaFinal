import os
import django
import uuid
import threading
from decimal import Decimal
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.core_erp.tenancy.models import Tenant
from apps.core_erp.accounting.ledger_engine import LedgerEngine
from apps.core_erp.event_bus import EventBus
from apps.core_erp.accounting.models import Account, ChartOfAccounts, FiscalPeriod

def simulate_reservation(tenant_id, reference):
    """
    Simula una reserva y su impacto contable.
    """
    try:
        payload = {
            "tenant_id": str(tenant_id),
            "total_amount": 1000,
            "commission_rate": 0.10,
            "reference": reference
        }
        LedgerEngine.post_event("ReservationConfirmed", payload)
        return True
    except Exception as e:
        print(f"Error in simulation: {e}")
        return False

def run_concurrency_test():
    print("\n--- INICIANDO PRUEBA DE CONCURRENCIA MASIVA ---")

    # 1. Setup Tenant
    tenant = Tenant.objects.create(name="Chaos Tenant", tax_id="CHAOS-001", currency="COP")
    coa = ChartOfAccounts.objects.create(tenant=tenant, name="COA Chaos")
    cutoff_date = timezone.now().date()
    FiscalPeriod.objects.create(tenant=tenant, period_start=cutoff_date.replace(day=1), period_end=cutoff_date.replace(day=28), status='open')

    # Accounts needed by ReservationConfirmed rule
    Account.objects.create(tenant=tenant, chart_of_accounts=coa, code="130505", name="AR")
    Account.objects.create(tenant=tenant, chart_of_accounts=coa, code="413501", name="Revenue")
    Account.objects.create(tenant=tenant, chart_of_accounts=coa, code="233505", name="Payable")

    # 2. Launch Threads
    threads = []
    num_reservations = 20
    for i in range(num_reservations):
        t = threading.Thread(target=simulate_reservation, args=(tenant.id, f"RES-{i}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # 3. Validation
    from apps.core_erp.accounting.models import JournalEntry
    entries_count = JournalEntry.objects.filter(tenant_id=tenant.id).count()
    print(f"  - Reservas intentadas: {num_reservations}")
    print(f"  - Asientos generados: {entries_count}")

    if entries_count == num_reservations:
        print("✅ Prueba de concurrencia EXITOSA.")
    else:
        print("❌ Prueba de concurrencia FALLIDA (posible pérdida de datos o deadlock).")

if __name__ == "__main__":
    run_concurrency_test()
