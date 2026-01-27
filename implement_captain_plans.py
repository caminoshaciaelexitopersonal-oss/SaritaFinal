import os
import re

def implement_plan_logic(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extraer el nombre de la clase
    class_match = re.search(r"class\s+([A-Za-z0-9_]+)\(CapitanTemplate\):", content)
    if not class_match:
        print(f"  - ADVERTENCIA: No se encontró el patrón de clase en {filepath}. Saltando.")
        return
    class_name = class_match.group(1)

    # Derivar el nombre del teniente a partir del nombre del capitán
    # e.g., CapitanAuditoriaGlobal -> auditoria_global
    teniente_key = class_name.replace("Capitan", "")
    teniente_key = re.sub(r'(?<!^)(?=[A-Z])', '_', teniente_key).lower().lstrip('_')

    # Nueva lógica para el método plan()
    new_plan_logic = f"""    def plan(self):
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

        # 2. Definir y Delegar Tarea Única
        # Cada capitán delega a su teniente correspondiente.
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

    # Reemplazar el método plan() existente
    plan_pattern = re.compile(r"def plan\(self\):.*?(?=(def\s|class\s|\Z))", re.DOTALL)
    new_content = plan_pattern.sub(new_plan_logic, content)

    with open(filepath, 'w') as f:
        f.write(new_content)

def main():
    domains_to_implement = ["administrador_general", "clientes_turistas"]
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles/"

    print("Iniciando implementación de la lógica de plan en los Capitanes...")
    for domain in domains_to_implement:
        capitanes_dir = os.path.join(base_dir, domain, "capitanes")
        if os.path.isdir(capitanes_dir):
            print(f"--- Implementando para el dominio: {domain} ---")
            for filename in os.listdir(capitanes_dir):
                if filename.startswith("capitan_") and filename.endswith(".py"):
                    filepath = os.path.join(capitanes_dir, filename)
                    print(f"  - Implementando plan en: {filepath}")
                    implement_plan_logic(filepath)

    print("Implementación de planes completada.")

if __name__ == "__main__":
    main()
