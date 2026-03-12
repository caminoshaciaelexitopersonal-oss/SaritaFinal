import os
import django
from decimal import Decimal

# Setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puerto_gaitan_turismo.settings")
django.setup()

from apps.sarita_agents.orchestrator import sarita_orchestrator
from apps.core_erp.tenancy.models import Tenant
from apps.core_erp.accounting.models import FiscalPeriod, Account, ChartOfAccounts
from django.utils import timezone

def verify_n6_hardening():
    print("SARITA EOS: Iniciando Certificación de Endurecimiento N6...")

    # 1. Setup Test Data (Tenant & Period)
    tenant, _ = Tenant.objects.get_or_create(
        tax_id="N6-TEST-999",
        defaults={"name": "N6 Hardening Test Corp", "currency": "COP"}
    )

    chart, _ = ChartOfAccounts.objects.get_or_create(
        tenant=tenant,
        name="Standard Chart"
    )

    # Create critical accounts
    Account.plain_objects.get_or_create(
        chart_of_accounts=chart, code="110505",
        defaults={"name": "Caja General", "type": "ASSET", "tenant": tenant}
    )
    Account.plain_objects.get_or_create(
        chart_of_accounts=chart, code="413501",
        defaults={"name": "Ingresos Operativos", "type": "REVENUE", "tenant": tenant}
    )

    period, _ = FiscalPeriod.plain_objects.get_or_create(
        tenant=tenant,
        period_start=timezone.now().date().replace(day=1),
        period_end=timezone.now().date().replace(day=28),
        defaults={"status": "open"}
    )

    # 2. Test Accounting N6 (Registro de Ingreso)
    print("\n--- TEST: SoldadoRegistroIngreso (Contable) ---")
    directive = {
        "domain": "contabilidad",
        "action": "ERP_CREATE_VOUCHER", # Mapped to CapitanContable
        "parameters": {
            "tenant_id": str(tenant.id),
            "fecha": str(timezone.now().date()),
            "descripcion": "Venta de prueba N6 Hardening",
            "monto_ingreso": 500000,
            "movimientos": [
                {"account_code": "110505", "debit": 500000, "credit": 0},
                {"account_code": "413501", "debit": 0, "credit": 500000}
            ],
            "usuario_id": None
        }
    }

    result = sarita_orchestrator.handle_directive(directive)
    print(f"Resultado Directiva: {result.get('status')}")

    if result.get('status') == "SUCCESS":
        print("✅ INTEGRACIÓN N6 -> SARGENTO -> LEDGER: EXITOSA")
    else:
        print(f"❌ FALLO: {result.get('error')}")

    # 3. Verificar Persistencia Real
    from apps.core_erp.accounting.models import JournalEntry
    entry = JournalEntry.objects.filter(tenant_id=tenant.id, is_posted=True).first()
    if entry and entry.system_hash:
        print(f"✅ PERSISTENCIA Y HASH: VERIFICADOS (ID: {entry.id}, Hash: {entry.system_hash[:16]})")
    else:
        print("❌ FALLO: No se encontró asiento posteado o falta hash.")

    # 4. Test Inventory N6
    print("\n--- TEST: SoldadoAjusteStock (Inventarios) ---")
    from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.inventario.models import InventoryItem

    item, _ = InventoryItem.objects.get_or_create(
        tenant_id=tenant.id,
        nombre_item="Producto Test N6",
        defaults={"cantidad": 100, "precio_unitario": 5000, "punto_reorden": 10}
    )

    directive_inv = {
        "domain": "prestadores",
        "mission": {"type": "ADJUST_INVENTORY"},
        "parameters": {
            "item_id": str(item.id),
            "cantidad": -5,
            "motivo": "Venta de prueba",
            "user_id": None,
            "tenant_id": str(tenant.id)
        }
    }

    result_inv = sarita_orchestrator.handle_directive(directive_inv)
    item.refresh_from_db()

    if item.cantidad == 95:
        print("✅ ENDURECIMIENTO INVENTARIO: EXITOSO (Stock: 95)")
    else:
        print(f"❌ FALLO INVENTARIO: Stock esperado 95, obtenido {item.cantidad}")

if __name__ == "__main__":
    try:
        verify_n6_hardening()
    except Exception as e:
        print(f"Error durante la certificación: {e}")
        import traceback
        traceback.print_exc()
