import os
import re

def refactor_captain_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Añadir el import necesario
    # Asegurarse de no añadirlo si ya existe
    if "from apps.sarita_agents.agents.capitan_template import CapitanTemplate" not in content:
        content = "from apps.sarita_agents.agents.capitan_template import CapitanTemplate\n" + content

    # Modificar la declaración de la clase para que herede de CapitanTemplate
    # Expresión regular para encontrar "class NombreClase:" o "class NombreClase("
    content = re.sub(r"class\s+([A-Za-z0-9_]+)\s*:", r"class \1(CapitanTemplate):", content, count=1)

    # Reemplazar el método __init__
    init_pattern = re.compile(r"def __init__\(self,.*?\):.*?(?=(def\s|class\s|\Z))", re.DOTALL)
    new_init = """    def __init__(self, mision_id: str):
        super().__init__(mision_id)
        # El logger ya está disponible como self.logger en CapitanTemplate
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Inicializado para Misión ID {self.mision_id}.")
"""
    content = init_pattern.sub(new_init, content)


    # Reemplazar el método plan()
    plan_pattern = re.compile(r"def plan\(self.*?\):.*?(?=(def\s|class\s|\Z))", re.DOTALL)
    new_plan = """    def plan(self):
        # Implementar la lógica de planificación real aquí.
        # Este método debe crear un PlanTáctico y TareasDelegadas.
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificando misión.")
        # Lógica de ejemplo:
        # self.crear_plan_tactico(...)
        pass
"""
    content = plan_pattern.sub(new_plan, content)

    # Reemplazar el método delegate() - a menudo llamado dentro de plan en la nueva arq.
    delegate_pattern = re.compile(r"def delegate\(self.*?\):.*?(?=(def\s|class\s|\Z))", re.DOTALL)
    new_delegate = """    # El método delegate() ahora es parte de la lógica de crear_plan_tactico
    # en la nueva arquitectura. Este método puede ser eliminado o adaptado.
"""
    content = delegate_pattern.sub(new_delegate, content)


    # Reemplazar el método report()
    report_pattern = re.compile(r"def report\(self.*?\):.*?(?=(def\s|class\s|\Z))", re.DOTALL)
    new_report = """    def report(self):
        # La lógica de reporte ahora es manejada por el Coronel
        # a través de la consolidación de los Planes Tácticos.
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Reporte no es necesario aquí.")
        pass
"""
    content = report_pattern.sub(new_report, content)

    with open(filepath, 'w') as f:
        f.write(content)

def main():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles/"
    print("Iniciando refactorización de Capitanes...")
    for coronel in os.listdir(base_dir):
        capitanes_dir = os.path.join(base_dir, coronel, "capitanes")
        if os.path.isdir(capitanes_dir):
            for root, _, files in os.walk(capitanes_dir):
                for filename in files:
                    if filename.startswith("capitan_") and filename.endswith(".py"):
                        filepath = os.path.join(root, filename)
                        print(f"  - Refactorizando: {filepath}")
                        refactor_captain_file(filepath)
    print("Refactorización completada.")

if __name__ == "__main__":
    main()
