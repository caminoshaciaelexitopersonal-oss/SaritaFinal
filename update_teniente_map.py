import os
import re

def update_teniente_map():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles"
    tasks_filepath = "backend/apps/sarita_agents/tasks.py"

    imports_to_add = []
    map_entries_to_add = []

    print("Escaneando para encontrar nuevos Tenientes...")
    for coronel in os.listdir(base_dir):
        tenientes_dir = os.path.join(base_dir, coronel, "tenientes")
        if os.path.isdir(tenientes_dir):
            for filename in os.listdir(tenientes_dir):
                if filename.startswith("teniente_") and filename.endswith(".py"):

                    # 1. Construir la ruta de importación
                    module_path = f".agents.general.sarita.coroneles.{coronel}.tenientes.{filename[:-3]}"

                    # 2. Extraer el nombre de la clase
                    with open(os.path.join(tenientes_dir, filename), 'r') as f:
                        content = f.read()
                        class_match = re.search(r"class\s+([A-Za-z0-9_]+)\(TenienteTemplate\):", content)
                        if class_match:
                            class_name = class_match.group(1)

                            # 3. Generar la clave del mapa (e.g., 'auditoria_global')
                            map_key = filename.replace("teniente_", "").replace(".py", "")

                            imports_to_add.append(f"from {module_path} import {class_name}")
                            map_entries_to_add.append(f"    '{map_key}': {class_name},")
                            print(f"  - Encontrado: {class_name} (clave: {map_key})")

    # Leer el contenido de tasks.py
    with open(tasks_filepath, 'r') as f:
        tasks_content = f.read()

    # Insertar los imports
    # Busca el comentario de marcador para saber dónde insertar.
    imports_marker = "# --- Mapeo de Tenientes ---"
    if imports_marker in tasks_content:
        # Eliminar duplicados y ordenar
        imports_to_add = sorted(list(set(imports_to_add)))
        imports_str = "\\n".join(imports_to_add)
        # Usamos sed para la sustitución para manejar los saltos de línea
        os.system(f"sed -i '/{imports_marker}/a{imports_str}' {tasks_filepath}")
        print(f"Imports de Tenientes añadidos a {tasks_filepath}")

    # Insertar las entradas del mapa
    map_marker = "TENIENTE_MAP = {"
    if map_marker in tasks_content:
        # Recargamos el contenido por si sed lo ha modificado
        with open(tasks_filepath, 'r') as f:
            tasks_content_updated = f.read()

        map_entries_str = "\n".join(sorted(map_entries_to_add))
        new_content = tasks_content_updated.replace(map_marker, f"{map_marker}\n{map_entries_str}")

        with open(tasks_filepath, 'w') as f:
            f.write(new_content)
        print(f"Entradas de TENIENTE_MAP añadidas a {tasks_filepath}")

if __name__ == "__main__":
    update_teniente_map()
