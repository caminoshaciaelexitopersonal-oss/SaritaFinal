import os

def fix_imports(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()

                # Replace canonical paths with local admin paths
                new_content = content.replace('apps.prestadores.mi_negocio', 'apps.admin_plataforma')

                # Fix some specific cases if needed
                # e.g. some files might still point to api.models for ProviderProfile
                # new_content = new_content.replace('from api.models import ProviderProfile', 'from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile')

                if new_content != content:
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    print(f"Fixed imports in {filepath}")

if __name__ == "__main__":
    fix_imports('backend/apps/admin_plataforma')
