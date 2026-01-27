import os
import re

def update_teniente_map_v2():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles"
    tasks_filepath = "backend/apps/sarita_agents/tasks.py"

    tenientes = {} # {key: (import_path, class_name)}

    print("Escaneando para encontrar todos los Tenientes...")
    for coronel in os.listdir(base_dir):
        tenientes_dir = os.path.join(base_dir, coronel, "tenientes")
        if os.path.isdir(tenientes_dir):
            for filename in os.listdir(tenientes_dir):
                if filename.startswith("teniente_") and filename.endswith(".py"):

                    filepath = os.path.join(tenientes_dir, filename)
                    with open(filepath, 'r') as f:
                        content = f.read()

                    class_match = re.search(r"class\s+([A-Za-z0-9_]+)\(TenienteTemplate\):", content)
                    if class_match:
                        class_name = class_match.group(1)
                        module_path = f"apps.sarita_agents.agents.general.sarita.coroneles.{coronel}.tenientes.{filename[:-3]}"
                        map_key = filename.replace("teniente_", "").replace(".py", "")

                        tenientes[map_key] = (module_path, class_name)
                        print(f"  - Encontrado: {class_name} (clave: {map_key})")

    # Leer el contenido original de tasks.py
    with open(tasks_filepath, 'r') as f:
        original_content = f.read()

    # Generar los nuevos imports
    imports_str = "# --- IMPORTS DE TENIENTES (GENERADO AUTOMÁTICAMENTE) ---\n"
    # Añadir los tenientes preexistentes manualmente para asegurar que no se pierden
    imports_str += "from .agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador\n"
    imports_str += "from .agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador\n"
    for key in sorted(tenientes.keys()):
        module_path, class_name = tenientes[key]
        imports_str += f"from {module_path} import {class_name}\n"

    # Generar el nuevo TENIENTE_MAP
    map_str = "# --- MAPEO DE TENIENTES (GENERADO AUTOMÁTICAMENTE) ---\nTENIENTE_MAP = {\n"
    # Añadir los tenientes preexistentes
    map_str += "    'validacion': TenienteValidacionPrestador,\n"
    map_str += "    'persistencia': TenientePersistenciaPrestador,\n"
    for key in sorted(tenientes.keys()):
        _, class_name = tenientes[key]
        map_str += f"    '{key}': {class_name},\n"
    map_str += "}\n"

    # Reemplazar las secciones antiguas en el archivo
    # Usaremos patrones que abarquen desde el inicio del marcador hasta el final del bloque

    # Reemplazar imports
    content_with_new_imports = re.sub(
        r"# backend/apps/sarita_agents/tasks.py.*?from \.models import TareaDelegada",
        f"# backend/apps/sarita_agents/tasks.py\nimport logging\nfrom celery import shared_task\nfrom .models import TareaDelegada",
        original_content,
        flags=re.DOTALL
    )

    content_with_new_imports = content_with_new_imports.replace(
        "from .agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador\nfrom .agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador",
        imports_str
    )

    # Reemplazar el mapa
    final_content = re.sub(
        r"# --- Mapeo de Tenientes ---.*?TENIENTE_MAP = \{.*?\n\}",
        map_str,
        content_with_new_imports,
        flags=re.DOTALL
    )

    with open(tasks_filepath, 'w') as f:
        f.write(final_content)
    print(f"Archivo {tasks_filepath} actualizado con éxito.")

if __name__ == "__main__":
    update_teniente_map_v2()
