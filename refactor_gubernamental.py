import os
import re

def refactor_captain_file_v3(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        class_match = re.search(
            r"class\s+([A-Za-z0-9_]+)\s*(\(.*\))?:\s*\"\"\"(.*?)\"\"\"",
            content,
            re.DOTALL
        )
        if not class_match:
            class_match = re.search(
                r"class\s+([A-Za-z0-9_]+)\s*:\s*\"\"\"(.*?)\"\"\"",
                content,
                re.DOTALL
            )
            if not class_match:
                 print(f"  - ADVERTENCIA: No se pudo encontrar el patrón de clase en {filepath}. Saltando.")
                 return

        class_name = class_match.group(1)
        docstring = class_match.group(2).strip().replace('"', '\\"') if len(class_match.groups()) > 1 else ""


        new_template = f"""from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class {class_name}(CapitanTemplate):
    \"\"\"
    {docstring}
    \"\"\"

    def __init__(self, mision_id: str, objective: str, parametros: Dict[str, Any]):
        super().__init__(mision_id=mision_id, objective=objective, parametros=parametros)
        self.logger.info(f"CAPITÁN {class_name}: Inicializado para Misión ID {{self.mision_id}}.")

    def plan(self):
        \"\"\"
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        \"\"\"
        self.logger.info(f"CAPITÁN {class_name}: Planificando la misión.")
        plan_tactico = self.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para {class_name}",
            descripcion=f"Este plan detalla los pasos para cumplir el objetivo: {{self.objective}}"
        )
        self.lanzar_ejecucion_plan()
        self.logger.info(f"CAPITÁN {class_name}: Planificación completada.")
"""

        with open(filepath, 'w') as f:
            f.write(new_template)

    except Exception as e:
        print(f"  - ERROR: Fallo al procesar {filepath}: {e}")

def main():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles/gubernamental/"
    print("Iniciando refactorización de Capitanes de Gubernamental...")

    for root, _, files in os.walk(base_dir):
        for filename in files:
            if filename.startswith("capitan_") and filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                print(f"  - Refactorizando: {filepath}")
                refactor_captain_file_v3(filepath)

    print("Refactorización de Gubernamental completada.")

if __name__ == "__main__":
    main()
