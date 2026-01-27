import os
import re

def refactor_captain_file_v2(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extraer el nombre de la clase y el docstring
    class_match = re.search(r"class\s+([A-Za-z0-9_]+)\s*:\s*\"\"\"(.*?)\"\"\"", content, re.DOTALL)
    if not class_match:
        print(f"  - ADVERTENCIA: No se pudo encontrar el patrón de clase en {filepath}. Saltando.")
        return

    class_name = class_match.group(1)
    docstring = class_match.group(2).strip()

    # Crear el nuevo contenido del archivo
    new_content = f'''from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class {class_name}(CapitanTemplate):
    """
    {docstring}
    """

    def __init__(self, mision_id: str, objective: str, parametros: Dict[str, Any]):
        super().__init__(mision_id=mision_id, objective=objective, parametros=parametros)
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Inicializado para Misión ID {{self.mision_id}}.")

    def plan(self):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        Debes crear un PlanTáctico y luego delegar Tareas a los Tenientes.
        """
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificando la misión.")

        # 1. Crear el Plan Táctico
        # El plan_tactico se crea una sola vez. El método se asegura de eso.
        plan_tactico = self.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para {self.__class__.__name__}",
            descripcion="Este plan detalla los pasos para cumplir el objetivo: {self.objective}"
        )

        # 2. Definir y Delegar Tareas
        # Aquí defines las tareas que los tenientes ejecutarán.
        # Ejemplo:
        # tarea_validacion = self.delegar_tarea(
        #     plan_tactico=plan_tactico,
        #     nombre_teniente="validacion", # Clave del TENIENTE_MAP en tasks.py
        #     descripcion="Validar los datos del nuevo prestador.",
        #     parametros_especificos={{"documento": self.parametros.get("documento_identidad")}}
        # )
        #
        # tarea_persistencia = self.delegar_tarea(
        #     plan_tactico=plan_tactico,
        #     nombre_teniente="persistencia",
        #     descripcion="Guardar el nuevo prestador en la base de datos.",
        #     parametros_especificos={{"datos_validados": f"output_of:{{tarea_validacion.id}}"}}
        # )

        # 3. Lanzar la Ejecución del Plan
        # Esto encolará las tareas en Celery.
        self.lanzar_ejecucion_plan()

        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tareas delegadas.")

'''
    with open(filepath, 'w') as f:
        f.write(new_content)

def main():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles/"
    print("Iniciando refactorización de Capitanes (V2)...")
    for coronel in os.listdir(base_dir):
        capitanes_dir = os.path.join(base_dir, coronel, "capitanes")
        if os.path.isdir(capitanes_dir):
            for root, _, files in os.walk(capitanes_dir):
                for filename in files:
                    # Aplicar solo a los capitanes movidos, no a los que ya existen
                    if filename.startswith("capitan_") and filename.endswith(".py"):
                        filepath = os.path.join(root, filename)
                        print(f"  - Refactorizando (V2): {filepath}")
                        refactor_captain_file_v2(filepath)
    print("Refactorización (V2) completada.")

if __name__ == "__main__":
    main()
