import os
import re

def check_stubs():
    stubs = []
    # We check only the priority ones we targeted
    files_to_check = [
        'backend/apps/core_erp/inventory_engine.py',
        'backend/apps/core_erp/accounting_engine.py',
        'backend/apps/core_erp/audit_engine.py',
        'backend/apps/prestadores/mi_negocio/operativa_turistica/operadores_directos/agencias/services.py',
        'backend/apps/core_erp/contracts/financial_contract.py',
        'backend/apps/global_holding/application/tax_optimization_service.py'
    ]

    for path in files_to_check:
        with open(path, 'r') as f:
            content = f.read()
            # Look for pass that is NOT inside an abstract method
            # For simplicity, we just look for any pass
            if 'pass' in content:
                 print(f"STUB STILL PRESENT IN: {path}")
            else:
                 print(f"STUB RESOLVED IN: {path}")

check_stubs()
