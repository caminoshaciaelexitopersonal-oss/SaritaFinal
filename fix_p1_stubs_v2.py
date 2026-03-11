import os
import re

def replace_in_file(filepath, search_pattern, replacement):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(search_pattern, replacement, content, flags=re.MULTILINE|re.DOTALL)
    with open(filepath, 'w') as f:
        f.write(new_content)

# 1. Implement check_period_status in accounting_engine.py
accounting_logic = """    @staticmethod
    def check_period_status(date, tenant):
        \"\"\"
        Verifica si el periodo para la fecha dada está abierto.
        \"\"\"
        from .accounting.models import FiscalPeriod
        period = FiscalPeriod.objects.filter(
            tenant=tenant,
            start_date__lte=date,
            end_date__gte=date
        ).first()

        if not period:
            return False, "No fiscal period found for date"
        return period.is_open, "Period closed" if not period.is_open else "OK\""""

replace_in_file('backend/apps/core_erp/accounting_engine.py',
                r'    @staticmethod\s+def check_period_status\(date, company\):\s+.*?pass',
                accounting_logic)

# 2. Implement create_intercompany_entry in accounting_engine.py
intercompany_logic = """    @staticmethod
    def create_intercompany_entry(origin_tenant, destination_tenant, amount, currency, concept):
        \"\"\"
        Genera asientos espejo para transacciones entre empresas del holding.
        \"\"\"
        from .accounting.models import JournalEntry, Account, FiscalPeriod
        from django.utils import timezone

        # 1. Validar periodos abiertos en ambos tenants
        now = timezone.now().date()
        if not AccountingEngine.check_period_status(now, origin_tenant)[0]:
            raise ValidationError(f"Periodo cerrado en origen {origin_tenant}")
        if not AccountingEngine.check_period_status(now, destination_tenant)[0]:
            raise ValidationError(f"Periodo cerrado en destino {destination_tenant}")

        # 2. Crear Asiento en Origen
        entry_origin = JournalEntry.objects.create(
            tenant=origin_tenant,
            date=now,
            description=f"INTERCOMPANY: {concept} to {destination_tenant}",
            period=FiscalPeriod.objects.filter(tenant=origin_tenant, is_open=True).first()
        )

        # 3. Crear Asiento en Destino
        entry_dest = JournalEntry.objects.create(
            tenant=destination_tenant,
            date=now,
            description=f"INTERCOMPANY: {concept} from {origin_tenant}",
            period=FiscalPeriod.objects.filter(tenant=destination_tenant, is_open=True).first()
        )

        logger.info(f"Intercompany entries created: {entry_origin.id} and {entry_dest.id}")
        return entry_origin, entry_dest"""

replace_in_file('backend/apps/core_erp/accounting_engine.py',
                r'    @staticmethod\s+def create_intercompany_entry\(origin_entity_id, destination_entity_id, amount, currency, concept\):\s+.*?pass',
                intercompany_logic)

print("Priority 1 stubs implemented v2.")
