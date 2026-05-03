import os
import sys
import subprocess
import glob

def run_sql_file(filepath, db_url):
    print(f"Executing {filepath}...")
    try:
        # Asume psql está disponible.
        subprocess.run(['psql', db_url, '-f', filepath], check=True)
    except Exception as e:
        print(f"Error executing {filepath}: {e}")
        sys.exit(1)

def deploy():
    db_url = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/sarita_db')

    order = [
        '00_init',
        '01_core',
        '02_identity',
        '03_governance',
        '04_agents',
        '05_erp_comercial',
        '06_erp_operativo',
        '07_erp_contable',
        '08_erp_financiero',
        '09_erp_archivistico',
        '10_wallet',
        '11_delivery',
        '12_auditoria',
        '13_ai_memory',
        '14_integraciones',
        '20_relaciones_globales',
        '30_triggers',
        '40_rls',
        '50_indices',
        '70_seed'
    ]

    print("--- Inicia Despliegue de Base de Datos Institucional SARITA ---")

    for folder in order:
        path = os.path.join('sarita_db', folder)
        if not os.path.exists(path):
            continue

        # Ordenar archivos para asegurar que las definiciones de funciones precedan a su uso
        sql_files = sorted(glob.glob(os.path.join(path, '*.sql')))
        for sql_file in sql_files:
            run_sql_file(sql_file, db_url)

    print("--- Despliegue Completado Exitosamente ---")

if __name__ == "__main__":
    deploy()
