import os
import re

def identify_stub_type(path, context):
    path = path.lower()
    if 'adapter' in path or 'gateway' in path or 'interop' in path:
        return 'Integración Externa'
    if 'agent' in path or 'sarita_agents' in path or 'mision' in context or 'tarea' in context:
        return 'IA'
    if 'notification' in path or 'email' in path or 'sms' in path or 'push' in path:
        return 'Integración Interna'
    if 'analytics' in path or 'report' in path or 'pipeline' in path or 'indicator' in path:
        return 'Integración Interna'
    return 'Lógica de Negocio'

def get_priority(path, stub_type):
    path = path.lower()
    if 'payment' in path or 'wallet' in path or 'ledger' in path or 'transaction' in path:
        return 'P1 - Pagos/Finanzas'
    if 'reservation' in path or 'booking' in path or 'availability' in path:
        return 'P2 - Reservas'
    if 'auth' in path or 'jwt' in path or 'identity' in path:
        return 'P4 - Auth'
    if 'invoice' in path or 'tax' in path or 'receipt' in path:
        return 'P5 - Facturación'
    if 'notification' in path or 'email' in path:
        return 'P6 - Notificaciones'
    if 'analytics' in path or 'report' in path:
        return 'P7 - Analítica'
    if stub_type == 'IA':
        return 'P8 - IA'
    return 'P3 - Wallet/General'

def generate_inventory():
    inventory = []
    # backend dirs to scan
    scan_dirs = ['backend/application', 'backend/apps', 'backend/infrastructure', 'backend/api']

    for scan_dir in scan_dirs:
        for root, dirs, files in os.walk(scan_dir):
            if 'tests' in root or 'migrations' in root:
                continue
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    path = os.path.join(root, file)
                    with open(path, 'r', errors='ignore') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if re.match(r'^\s*pass\s*$', line):
                                # Find function name above
                                func_name = "Unknown"
                                for j in range(i - 1, -1, -1):
                                    m = re.match(r'^\s*def\s+(\w+)\(', lines[j])
                                    if m:
                                        func_name = m.group(1)
                                        break

                                stub_type = identify_stub_type(path, line)
                                priority = get_priority(path, stub_type)

                                inventory.append({
                                    'Archivo': path,
                                    'Función': func_name,
                                    'Tipo de Stub': stub_type,
                                    'Prioridad': priority
                                })
    return inventory

inventory = generate_inventory()

# Ensure docs dir exists
os.makedirs('docs', exist_ok=True)

with open('docs/stub_inventory.md', 'w') as f:
    f.write("# STUB INVENTORY: SARITA BACKEND\n\n")
    f.write("| Archivo | Función | Tipo de Stub | Prioridad |\n")
    f.write("| :--- | :--- | :--- | :--- |\n")
    # Sort by priority
    for item in sorted(inventory, key=lambda x: x['Prioridad']):
        f.write(f"| {item['Archivo']} | {item['Función']} | {item['Tipo de Stub']} | {item['Prioridad']} |\n")

print(f"Inventory generated with {len(inventory)} stubs.")
