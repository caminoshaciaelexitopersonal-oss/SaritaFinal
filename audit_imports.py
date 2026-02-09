import os
import re

base_path = 'backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial'
levels = {
    'soldados': 4,
    'sargentos': 3,
    'tenientes': 2,
    'capitanes': 1
}

patterns = {
    'capitanes': [r'from \.*tenientes', r'from \.*sargentos', r'from \.*soldados'],
    'tenientes': [r'from \.*sargentos', r'from \.*soldados'],
    'sargentos': [r'from \.*soldados'],
    'soldados': []
}

# Subordinated can't import superiors
forbidden = {
    'soldados': ['Sargento', 'Teniente', 'Capitan'],
    'sargentos': ['Teniente', 'Capitan'],
    'tenientes': ['Capitan']
}

errors = []

for folder, level in levels.items():
    path = os.path.join(base_path, folder)
    if not os.path.exists(path): continue

    for filename in os.listdir(path):
        if not filename.endswith('.py') or filename == '__init__.py': continue

        file_path = os.path.join(path, filename)
        with open(file_path, 'r') as f:
            content = f.read()

        # Check forbidden keywords (superiors)
        for super_role in forbidden.get(folder, []):
            # Check if it's imported (simple check)
            if re.search(fr'from .* import .*{super_role}', content) or re.search(fr'import .*{super_role}', content):
                 # Ignore base templates
                 if 'comercial_base_templates' not in content:
                    errors.append(f"VIOLACIÓN DE IMPORTACIÓN: {file_path} intenta importar un superior ({super_role})")

if not errors:
    print("AUDITORÍA DE IMPORTACIONES EXITOSA: No se detectaron importaciones ascendentes.")
else:
    print("ERRORES DE CODIFICACIÓN DETECTADOS:")
    for err in errors:
        print(f"- {err}")
