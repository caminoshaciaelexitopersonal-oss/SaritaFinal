# scripts/migrarSoldadosN6OroV2.py
# Simulación de script de migración masiva automatizada

import os
import re
import json

def migrate_soldiers():
    base_dir = "backend/apps/sarita_agents/agents"
    report = {
        "total_scanned": 0,
        "migrated": [],
        "errors": []
    }

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and file != "soldado_n6_oro_v2.py" and file != "soldado_template.py":
                report["total_scanned"] += 1
                filepath = os.path.join(root, file)

                with open(filepath, 'r') as f:
                    content = f.read()

                # Regex para detectar clases que heredan de SoldierTemplate
                if "SoldierTemplate" in content:
                    # 1. Cambiar importación
                    new_content = content.replace(
                        "from apps.sarita_agents.agents.soldado_template import SoldierTemplate",
                        "from apps.sarita_agents.agents.soldado_n6_oro_v2 import SoldadoN6OroV2"
                    )

                    # 2. Cambiar herencia de clases
                    new_content = re.sub(r'class (.*)\(SoldierTemplate\):', r'class \1(SoldadoN6OroV2):', new_content)

                    # 3. Insertar placeholders obligatorios
                    # Intentamos inferir dominio por la ruta
                    domain = root.split("/")[-2] if len(root.split("/")) > 2 else "unknown"
                    placeholders = f'\n    domain = "{domain}"\n    aggregate_root = "Placeholder"\n    required_permissions = ["{domain}.execute"]\n'

                    new_content = re.sub(r'(class .*\(SoldadoN6OroV2\):)', r'\1' + placeholders, new_content)

                    with open(filepath, 'w') as f:
                        f.write(new_content)

                    report["migrated"].append(file)

    with open("reporte_migracion_soldados.json", "w") as f:
        json.dump(report, f, indent=4)

    print(f"MIGRACIÓN COMPLETADA: {len(report['migrated'])} soldados procesados.")

if __name__ == "__main__":
    migrate_soldiers()
