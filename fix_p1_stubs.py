import os
import re

def replace_in_file(filepath, search_pattern, replacement):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(search_pattern, replacement, content, flags=re.MULTILINE|re.DOTALL)
    with open(filepath, 'w') as f:
        f.write(new_content)

# 1. Implement InventoryEngine.validate_stock_availability
inventory_logic = """    @staticmethod
    def validate_stock_availability(product, warehouse, requested_quantity):
        # Implementación real: busca el balance actual en el almacén
        from .models import InventoryMovement
        from django.db.models import Sum

        balance = InventoryMovement.objects.filter(
            product=product,
            warehouse=warehouse
        ).aggregate(
            total=Sum('quantity')
        )['total'] or 0

        return balance >= requested_quantity"""

replace_in_file('backend/apps/core_erp/inventory_engine.py',
                r'    @staticmethod\s+def validate_stock_availability\(product, warehouse, requested_quantity\):\s+#.*?\s+pass',
                inventory_logic)

# 2. Implement check_period_status in accounting_engine.py
accounting_logic = """    @staticmethod
    def check_period_status(date, tenant):
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
                r'    @staticmethod\s+def check_period_status\(date, tenant\):\s+#.*?\s+pass',
                accounting_logic)

print("Priority 1 stubs implemented.")
