import os
import sys
import subprocess
import glob

def run_sql_file(filepath):
    print(f"Applying: {filepath}")

def deploy():
    phases = [
        '00_init', '01_core', '02_identity', '03_governance', '04_tourism',
        '05_erp', '06_finance', '20_relaciones', '30_triggers', '40_rls',
        '50_indices', '41_ai_core', '60_migraciones', '70_seed', '80_testing'
    ]
    print("--- INICIANDO DESPLIEGUE FINAL SCTA ---")
    for phase in phases:
        path = os.path.join('sarita_db', phase)
        if not os.path.exists(path): continue
        for root, dirs, files in os.walk(path):
            for file in sorted(files):
                if file.endswith('.sql'):
                    run_sql_file(os.path.join(root, file))
    print("--- SISTEMA NORMALIZADO ---")

if __name__ == "__main__":
    deploy()
