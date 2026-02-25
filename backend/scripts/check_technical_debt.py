import os
import re

def get_metrics():
    """
    Calcula métricas estructurales básicas del sistema.
    """
    base_path = 'backend/apps'
    metrics = {
        'total_models': 0,
        'total_endpoints': 0,
        'cross_domain_imports': 0,
        'apps_count': 0
    }

    for root, dirs, files in os.walk(base_path):
        if 'migrations' in root or '__pycache__' in root:
            continue

        for file in files:
            file_path = os.path.join(root, file)

            # Contar Modelos
            if file == 'models.py':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    metrics['total_models'] += len(re.findall(r'class\s+\w+\(models\.Model\)', content))
                    metrics['total_models'] += len(re.findall(r'class\s+\w+\(BaseErpModel\)', content))
                    metrics['total_models'] += len(re.findall(r'class\s+\w+\(TenantAwareModel\)', content))

            # Contar Endpoints (en urls.py)
            if file == 'urls.py':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    metrics['total_endpoints'] += len(re.findall(r'path\(', content))

    print("\n📊 MÉTRICAS DE DEUDA TÉCNICA (SISTEMA INMUNOLÓGICO):")
    print(f"  - Total Modelos: {metrics['total_models']}")
    print(f"  - Total Endpoints (aprox): {metrics['total_endpoints']}")

    return metrics

if __name__ == "__main__":
    get_metrics()
