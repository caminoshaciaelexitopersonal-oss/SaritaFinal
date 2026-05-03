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

    phases = [
        ['00_init', '01_core'],
        ['02_identity', '03_governance', '04_agents'],
        ['05_erp_comercial', '06_erp_operativo', '07_erp_contable', '08_erp_financiero', '09_erp_archivistico'],
        ['10_wallet', '11_delivery', '12_auditoria', '13_ai_memory', '14_integraciones'],
        ['15_event_sourcing', '16_wallet_ledger', '17_payments', '18_ai_memory', '19_kyc', '21_tax', '22_reconciliation', '23_archival_legal', '24_partitioning', '25_backup_recovery', '26_transaction_engine', '27_concurrency', '28_retry_queue', '29_webhooks', '31_scheduler'],
        ['20_relaciones_globales', '30_triggers', '40_rls', '50_indices', '70_seed', '80_testing']
    ]

    print("--- Iniciando Despliegue de HARDENING FASE 10 (Operatividad Crítica) ---")

    for phase in phases:
        for folder in phase:
            path = os.path.join('sarita_db', folder)
            if not os.path.exists(path): continue

            sql_files = sorted(glob.glob(os.path.join(path, '*.sql')))
            for sql_file in sql_files:
                run_sql_file(sql_file, db_url)

    print("--- DESPLIEGUE FINALIZADO CON ÉXITO ---")

if __name__ == "__main__":
    deploy()
