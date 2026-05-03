import os
import sys
import subprocess
import glob
import hashlib

def calculate_checksum(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

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

    phases = [
        ['00_init', '01_core'],
        ['02_identity', '03_governance', '04_agents', '06_turismo'],
        ['07_prestadores', '08_directorio_turistico', '09_eventos_prestadores', '10_roles_empresariales', '11_compliance', '12_reputacion', '13_capacidad_operativa'], # VÍA 2
        ['05_erp_comercial', '10_wallet', '11_delivery', '12_auditoria', '13_ai_memory', '14_integraciones'],
        ['15_event_sourcing', '16_wallet_ledger', '17_payments', '18_ai_memory', '19_kyc', '21_tax', '22_reconciliation', '23_archival_legal', '24_partitioning', '25_backup_recovery', '26_transaction_engine', '27_concurrency', '28_retry_queue', '29_webhooks', '31_scheduler'],
        ['32_schema_versioning', '33_event_consistency', '34_retry_intelligence', '35_webhook_security', '36_trace_propagation', '37_ai_governance', '38_scheduler_advanced', '39_watchdog_recovery'],
        ['41_cross_domain_consistency', '42_rls_enforcement', '43_webhook_replay_protection', '44_scheduler_cluster', '45_ai_hierarchy', '46_event_archival', '47_forensic_mode', '48_system_validation'],
        ['20_relaciones_globales', '30_triggers', '40_rls', '50_indices', '70_seed', '80_testing']
    ]

    print("--- Iniciando Despliegue FASE V2-BUSINESS (Núcleo Económico) ---")

    global_checksum = hashlib.sha256()
    for phase in phases:
        for folder in phase:
            path = os.path.join('sarita_db', folder)
            if not os.path.exists(path): continue
            sql_files = sorted(glob.glob(os.path.join(path, '*.sql')))
            for sql_file in sql_files:
                run_sql_file(sql_file, db_url)
                global_checksum.update(calculate_checksum(sql_file).encode())

    final_checksum = global_checksum.hexdigest()
    print(f"Registrando versión v10.3_business_core (Checksum: {final_checksum[:10]})")
    subprocess.run(['psql', db_url, '-c', f"SELECT core.apply_schema_version('v10.3_business_core', '{final_checksum}')"], check=True)

    print("--- DESPLIEGUE FINALIZADO EXITOSAMENTE ---")

if __name__ == "__main__":
    deploy()
