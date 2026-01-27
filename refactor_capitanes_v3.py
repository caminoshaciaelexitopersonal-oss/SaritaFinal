import os
import re

def refactor_captain_file_v3(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        # Extraer el nombre de la clase y el docstring. Patrón mejorado.
        class_match = re.search(
            r"class\s+([A-Za-z0-9_]+)\s*(\(.*\))?:\s*\"\"\"(.*?)\"\"\"",
            content,
            re.DOTALL
        )

        if not class_match:
            # Si el patrón principal falla, intenta uno más simple para clases sin herencia
            class_match = re.search(
                r"class\s+([A-Za-z0-9_]+)\s*:\s*\"\"\"(.*?)\"\"\"",
                content,
                re.DOTALL
            )
            if not class_match:
                 print(f"  - ADVERTENCIA: No se pudo encontrar el patrón de clase en {filepath}. Saltando.")
                 return

        class_name = class_match.group(1)
        docstring = class_match.group(3).strip().replace('"', '\\"') # Escapar comillas

        # Plantilla de nuevo contenido
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
        Debes crear un PlanTáctico y luego delegar Tareas a los Tenientes.
        \"\"\"
        self.logger.info(f"CAPITÁN {class_name}: Planificando la misión.")

        # 1. Crear el Plan Táctico
        plan_tactico = self.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para {class_name}",
            descripcion=f"Este plan detalla los pasos para cumplir el objetivo: {{self.objective}}"
        )

        # 2. Definir y Delegar Tareas (EJEMPLO - DEBE SER IMPLEMENTADO)
        # self.delegar_tarea(plan_tactico=plan_tactico, nombre_teniente="...", descripcion="...", parametros_especificos={{...}})

        # 3. Lanzar la Ejecución del Plan
        self.lanzar_ejecucion_plan()

        self.logger.info(f"CAPITÁN {class_name}: Planificación completada y tareas delegadas.")
"""

        with open(filepath, 'w') as f:
            f.write(new_template)

    except Exception as e:
        print(f"  - ERROR: Fallo al procesar {filepath}: {e}")

def main():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles/"
    print("Iniciando refactorización de Capitanes (V3)...")
    # Excluir archivos que ya deberían estar bien.
    exclude_files = ['onboarding_prestador_capitan.py', 'dummy_capitan.py']

    for coronel in os.listdir(base_dir):
        capitanes_dir = os.path.join(base_dir, coronel, "capitanes")
        if os.path.isdir(capitanes_dir):
            for root, _, files in os.walk(capitanes_dir):
                for filename in files:
                    if filename.startswith("capitan_") and filename.endswith(".py") and filename not in exclude_files:
                        filepath = os.path.join(root, filename)
                        print(f"  - Refactorizando (V3): {filepath}")
                        refactor_captain_file_v3(filepath)
    print("Refactorización (V3) completada.")

if __name__ == "__main__":
    main()
