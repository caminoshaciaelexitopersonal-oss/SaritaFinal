import os
import re

def get_detailed_models():
    model_data = []
    # Include both apps and core_erp specific subdirs
    search_dirs = ['backend/apps/core_erp']
    for search_dir in search_dirs:
        for root, dirs, files in os.walk(search_dir):
            for file in files:
                if file.endswith('.py'):
                    # Module name relative to apps
                    module_name = root.split('apps/')[-1]
                    path = os.path.join(root, file)
                    with open(path, 'r', errors='ignore') as f:
                        content = f.read()
                        # Match class Name(models.Model) or class Name(AnyOther)
                        # but we filter by body content for fields
                        classes = re.split(r"class (\w+)\((.*?)\):", content)
                        for i in range(1, len(classes), 3):
                            class_name = classes[i]
                            body = classes[i+2] if i+2 < len(classes) else ""
                            if 'models.' in body:
                                fks = re.findall(r"(\w+)\s*=\s*models\.ForeignKey\(['\"]?(\w+)['\"]?", body)
                                fks_str = ", ".join([f"{f[0]}->{f[1]}" for f in fks])
                                model_data.append({
                                    'module': module_name,
                                    'model': class_name,
                                    'relations': fks_str
                                })
    return model_data

models = get_detailed_models()
print("| Módulo | Modelo | Relaciones (FK) |")
print("| :--- | :--- | :--- |")
for m in sorted(models, key=lambda x: (x['module'], x['model'])):
    print(f"| {m['module']} | {m['model']} | {m['relations']} |")
