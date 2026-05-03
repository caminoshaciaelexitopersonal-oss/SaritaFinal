import os
import sys
import subprocess
import glob

def run_sql_file(filepath, db_url):
    print(f"Executing {filepath}...")
    try:
        subprocess.run(['psql', db_url, '-f', filepath], check=True)
    except Exception as e:
        print(f"Error executing {filepath}: {e}")
        sys.exit(1)

def deploy():
    db_host = os.getenv('DB_HOST', 'localhost')
    db_name = os.getenv('DB_NAME', 'sarita_db')
    db_user = os.getenv('DB_USER', 'postgres')
    db_pass = os.getenv('DB_PASS', 'postgres')
    db_url = f"postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}"

    admin_url = f"postgresql://{db_user}:{db_pass}@{db_host}:5432/postgres"
    print(f"Verificando existencia de base de datos {db_name}...")
    try:
        result = subprocess.run(['psql', admin_url, '-tAc', f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"], capture_output=True, text=True)
        if result.stdout.strip() != '1':
            print(f"Creando base de datos {db_name}...")
            subprocess.run(['psql', admin_url, '-c', f"CREATE DATABASE {db_name}"], check=True)
    except Exception as e:
        print(f"Error al verificar/crear DB: {e}")

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
        '15_event_sourcing',
        '16_wallet_ledger',
        '17_payments',
        '18_ai_memory',
        '19_kyc',
        '21_tax',
        '22_reconciliation',
        '23_archival_legal',
        '24_partitioning',
        '25_backup_recovery',
        '20_relaciones_globales',
        '30_triggers',
        '40_rls',
        '50_indices',
        '70_seed'
    ]

    print("--- Inicia Despliegue de Infraestructura de Datos Soberana SARITA (Fase 10) ---")

    for folder in order:
        path = os.path.join('sarita_db', folder)
        if not os.path.exists(path):
            continue

        sql_files = sorted(glob.glob(os.path.join(path, '*.sql')))
        for sql_file in sql_files:
            run_sql_file(sql_file, db_url)

    print("--- Despliegue Completado con Éxito (Nivel World Class) ---")

if __name__ == "__main__":
    deploy()
