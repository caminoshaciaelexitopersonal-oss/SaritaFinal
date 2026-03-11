import os
import re

def map_models():
    models = {}
    for root, dirs, files in os.walk('backend/apps'):
        for file in files:
            if file == 'models.py' or (root.endswith('models') and file.endswith('.py')):
                # Use the path to identify the module
                parts = root.split('/')
                module = parts[2] if len(parts) > 2 else root
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                    classes = re.findall(r"class (\w+)\(.*?models\.Model\):", content)
                    if not classes:
                        classes = re.findall(r"class (\w+)\(models\.Model\):", content)
                    if classes:
                        if module not in models: models[module] = []
                        models[module].extend(classes)
    return models

mapping = map_models()
for mod, classes in sorted(mapping.items()):
    print(f"Module: {mod} -> Models: {', '.join(classes[:5])}{'...' if len(classes) > 5 else ''}")
