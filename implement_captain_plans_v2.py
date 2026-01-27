import os
import re

def implement_plan_logic_v2(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    class_match = re.search(r"class\s+([A-Za-z0-9_]+)\(CapitanTemplate\):", content)
    if not class_match:
        print(f"  - ADVERTENCIA: No se encontró el patrón de clase en {filepath}. Saltando.")
        return
    class_name = class_match.group(1)

    teniente_key = class_name.replace("Capitan", "")
    teniente_key = re.sub(r'(?<!^)(?=[A-Z])', '_', teniente_key).lower().lstrip('_')

    # Plantilla con indentación corregida
    new_plan_logic = f"""    def plan(self):
        \"\"\"
        El corazón del Capitán. Aquí es donde defines el plan táctáctico.
        Debes crear un PlanTáctico y luego delegar Tareas a los Tenientes.
        \"\"\"
        self.logger.info(f"CAPITÁN {class_name}: Planificando la misión.")

        # 1. Crear el Plan Táctico
        plan_tactico = self.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para {class_name}",
            descripcion=f"Este plan detalla los pasos para cumplir el objetivo: {{self.objective}}"
        )

        # 2. Definir y Delegar Tarea Única
        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="{teniente_key}",
            descripcion=f"Ejecutar la tarea principal para {class_name}.",
            parametros_especificos=self.parametros
        )

        # 3. Lanzar la Ejecución del Plan
        self.lanzar_ejecucion_plan()

        self.logger.info(f"CAPITÁN {class_name}: Planificación completada y tarea delegada a '{teniente_key}'.")
"""

    plan_pattern = re.compile(r"def plan\(self\):.*?(?=(def\s|class\s|\Z))", re.DOTALL)
    # Asegurarse de que el patrón de reemplazo no deje indentación extraña
    if plan_pattern.search(content):
        new_content = plan_pattern.sub(new_plan_logic.replace("    ", "", 1), content) # Quitar un nivel de indentación
    else:
        # Si no hay método plan, añadirlo al final de la clase (aproximación)
        new_content = content.strip() + "\\n\\n" + new_plan_logic

    # Limpieza final de posibles artefactos de indentación del init
    new_content = re.sub(r"    \n    def __init__", "    def __init__", new_content)

    with open(filepath, 'w') as f:
        f.write(new_content)

def main():
    domains_to_implement = ["administrador_general", "clientes_turistas"]
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles/"

    print("Iniciando implementación de la lógica de plan (V2)...")
    for domain in domains_to_implement:
        capitanes_dir = os.path.join(base_dir, domain, "capitanes")
        if os.path.isdir(capitanes_dir):
            print(f"--- Implementando para el dominio: {domain} (V2) ---")
            for filename in os.listdir(capitanes_dir):
                if filename.startswith("capitan_") and filename.endswith(".py"):
                    filepath = os.path.join(capitanes_dir, filename)
                    print(f"  - Implementando plan en: {filepath} (V2)")
                    implement_plan_logic_v2(filepath)

    print("Implementación de planes (V2) completada.")

if __name__ == "__main__":
    main()
