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
        ['00_init', '01_core', '38_clientes', '39_productos_servicios'],
        ['02_identity', '03_governance', '04_agents', '06_turismo', '07_prestadores', '08_directorio_turistico', '09_eventos_prestadores', '10_roles_empresariales', '11_compliance', '12_reputacion', '13_capacidad_operativa', '37_artesanos/01_identidad', '37_artesanos/02_geolocalizacion', '37_artesanos/03_catalogo', '37_artesanos/04_inventario_produccion', '37_artesanos/05_clasificacion', '37_artesanos/06_directorio', '37_artesanos/07_eventos'],
        ['50_wpc_funnel'],
        ['38_clientes_turistas/01_perfil', '38_clientes_turistas/02_geolocalizacion', '38_clientes_turistas/03_comportamiento', '38_clientes_turistas/04_historial', '38_clientes_turistas/05_interacciones', '38_clientes_turistas/06_feed_personalizado', '38_clientes_turistas/07_citas'], # VÍA 3
        ['30_mi_negocio', '31_gestion_comercial/01_crm', '31_gestion_comercial/02_ventas', '31_gestion_comercial/03_marketing', '31_gestion_comercial/04_fidelizacion', '31_gestion_comercial/05_contenido_multimedia', '31_gestion_comercial/06_social_media', '31_gestion_comercial/07_automatizacion_comercial', '31_gestion_comercial/08_ia_conversacional'],
        ['32_gestion_operativa/01_core_operativo', '32_gestion_operativa/02_tareas_operativas', '32_gestion_operativa/03_ordenes_servicio', '32_gestion_operativa/04_recursos', '32_gestion_operativa/05_agenda_programacion', '32_gestion_operativa/06_incidentes', '32_gestion_operativa/07_checklist_control', '32_gestion_operativa/08_logistica', '32_gestion_operativa/09_capacidad_ocupacion', '32_gestion_operativa/10_geolocalizacion'],
        ['33_operativa_especializada/01_hoteles', '33_operativa_especializada/02_restaurantes', '33_operativa_especializada/03_bares_discotecas', '33_operativa_especializada/04_agencias_viaje', '33_operativa_especializada/05_agencias_operativas', '33_operativa_especializada/06_guias_turisticos', '33_operativa_especializada/07_asociaciones_guias', '33_operativa_especializada/08_transporte_turistico'],
        ['34_gestion_archivistica/01_estructura_documental', '34_gestion_archivistica/02_expedientes', '34_gestion_archivistica/03_documentos', '34_gestion_archivistica/04_versionado', '34_gestion_archivistica/05_metadatos', '34_gestion_archivistica/06_clasificacion', '34_gestion_archivistica/07_ciclo_vida', '34_gestion_archivistica/08_accesos_seguridad', '34_gestion_archivistica/09_firma_electronica', '34_gestion_archivistica/10_notarizacion', '34_gestion_archivistica/11_ocr_extraccion', '34_gestion_archivistica/12_trazabilidad', '34_gestion_archivistica/13_retencion_disposicion', '34_gestion_archivistica/14_exportacion_auditoria'],
        ['35_gestion_contable/01_catalogos', '35_gestion_contable/02_configuracion', '35_gestion_contable/03_movimientos', '35_gestion_contable/04_periodos', '35_gestion_contable/05_impuestos', '35_gestion_contable/06_conciliacion', '35_gestion_contable/07_analitica', '35_gestion_contable/08_auditoria'],
        ['36_gestion_financiera/01_tesoreria', '36_gestion_financiera/02_presupuestos', '36_gestion_financiera/03_flujo_caja', '36_gestion_financiera/04_financiamiento', '36_gestion_financiera/05_inversiones', '36_gestion_financiera/06_gastos', '36_gestion_financiera/07_indicadores', '36_gestion_financiera/08_consolidacion'],
        ['37_analitica_financiera', '40_facturacion', '41_costos'],
        ['10_wallet', '11_delivery', '12_auditoria', '13_ai_memory', '14_integraciones'],
        ['15_event_sourcing', '16_wallet_ledger', '17_payments', '19_kyc', '21_tax', '22_reconciliation', '23_archival_legal', '24_partitioning', '25_backup_recovery', '26_transaction_engine', '27_concurrency', '28_retry_queue', '29_webhooks', '31_scheduler'],
        ['932_schema_versioning', '933_event_consistency', '934_retry_intelligence', '935_webhook_security', '936_trace_propagation', '937_ai_governance', '938_scheduler_advanced', '939_watchdog_recovery'],
        ['941_cross_domain_consistency', '942_rls_enforcement', '943_webhook_replay_protection', '944_scheduler_cluster', '945_ai_hierarchy', '946_event_archival', '947_forensic_mode', '948_system_validation'],
        ['20_relaciones_globales', '930_triggers', '940_rls', '950_indices', '970_seed', '980_testing']
    ]

    print("--- Iniciando Despliegue MOTOR DE EXPERIENCIA TURISTA (Fase 10.12) ---")

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
    print(f"Registrando versión v10.12_tourist_experience (Checksum: {final_checksum[:10]})")
    subprocess.run(['psql', db_url, '-c', f"SELECT core.apply_schema_version('v10.12_tourist_experience', '{final_checksum}')"], check=True)

    print("--- DESPLIEGUE TURISMO V3 COMPLETADO ---")

if __name__ == "__main__":
    deploy()
