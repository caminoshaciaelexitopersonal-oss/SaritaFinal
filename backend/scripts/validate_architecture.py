import os
import sys
import re

def check_prohibited_imports():
    """
    Escanea el código fuente buscando importaciones prohibidas entre dominios:
    - admin_plataforma no puede importar de mi_negocio
    - mi_negocio no puede importar de admin_plataforma
    """
    base_path = 'backend/apps'
    violations = []

    rules = [
        {
            'path': 'admin_plataforma',
            'prohibited': 'apps.prestadores.mi_negocio',
            'message': 'Admin Plataforma intentó importar desde Mi Negocio (Tenant).'
        },
        {
            'path': 'prestadores/mi_negocio',
            'prohibited': 'apps.admin_plataforma',
            'message': 'Mi Negocio (Tenant) intentó importar desde Admin Plataforma.'
        }
    ]

    for rule in rules:
        target_dir = os.path.join(base_path, rule['path'])
        if not os.path.exists(target_dir):
            continue

        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if rule['prohibited'] in content:
                            violations.append(f"{file_path}: {rule['message']}")

    if violations:
        print("\n❌ VIOLACIONES DE ARQUITECTURA DETECTADAS:")
        for v in violations:
            print(f"  - {v}")
        return False

    print("\n✅ Arquitectura de dominios validada exitosamente.")
    return True

if __name__ == "__main__":
    success = check_prohibited_imports()
    if not success:
        sys.exit(1)
