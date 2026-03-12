import os
import sys

def check_parity():
    critical_modules = [
        "dashboard-admin",
        "dashboard-prestador",
        "descubre-turismo",
        "usuarios",
        "reportes",
        "reservas",
        "POS",
        "ERP"
    ]

    platforms = {
        "Web": "interfaz/src/app",
        "Mobile": "apps/mobile/src/screens",
        "Desktop": "apps/desktop/renderer/src"
    }

    # Standardized mapping for path searching
    module_paths = {
        "dashboard-admin": ["dashboard/admin", "admin", "dashboard/panel-admin"],
        "dashboard-prestador": ["dashboard/prestador", "business", "dashboard/tablero-prestador"],
        "descubre-turismo": ["descubre", "explore", "pages/descubre"],
        "usuarios": ["dashboard/usuarios", "profile", "dashboard/users"],
        "reportes": ["dashboard/reportes", "reports", "dashboard/reports"],
        "reservas": ["dashboard/reservas", "booking", "dashboard/operations/BookingsCalendar.tsx"],
        "POS": ["dashboard/pos", "pos", "dashboard/commercial/POSInterface.tsx"],
        "ERP": ["dashboard/erp", "business/BusinessAccountingScreen.tsx", "dashboard/MiNegocio.tsx"]
    }

    results = {}

    print("=== SARITA MODULE PARITY AUDIT ===")
    for module in critical_modules:
        results[module] = {}
        for platform, base_path in platforms.items():
            found = False
            for path_alias in module_paths.get(module, []):
                full_path = os.path.join(base_path, path_alias)
                # Check for either directory or exact file
                if os.path.exists(full_path):
                    found = True
                    break
            results[module][platform] = "✓" if found else "✖"

    # Print Matrix
    header = f"{'Módulo':<20} | {'Web':<10} | {'Mobile':<10} | {'Desktop':<10}"
    print(header)
    print("-" * len(header))

    for module, platforms_status in results.items():
        row = f"{module:<20} | {platforms_status['Web']:<10} | {platforms_status['Mobile']:<10} | {platforms_status['Desktop']:<10}"
        print(row)

    # Validation
    gaps = 0
    for module in results:
        for platform in results[module]:
            if results[module][platform] == "✖":
                gaps += 1

    if gaps == 0:
        print("\n✅ SUCCESS: Structural Parity Achieved.")
    else:
        print(f"\n⚠️ WARNING: Detected {gaps} functional gaps.")

if __name__ == "__main__":
    check_parity()
