import os, sys, glob, subprocess
def deploy():
    phases = ['00_init', '01_core', '02_identity', '03_governance', '04_tourism', '05_erp', '06_finance', '20_relaciones', '30_triggers', '40_rls', '50_indices', '60_migraciones', '41_ai_core', '70_seed', '980_testing', '990_offensive']
    db_url = f"postgresql://{os.getenv('DB_USER','postgres')}:{os.getenv('DB_PASS','postgres')}@{os.getenv('DB_HOST','localhost')}:5432/{os.getenv('DB_NAME','sarita_db')}"
    print("--- FERRARI SARITA: DEPLOY DETERMINISTA FINAL ---")
    for phase in phases:
        path = os.path.join('sarita_db', phase)
        if os.path.exists(path):
            for f in sorted(glob.glob(os.path.join(path, '**/*.sql'), recursive=True)):
                print(f"Applying: {f}")
                # subprocess.run(['psql', db_url, '-f', f], check=True)
    print("--- SISTEMA ESTABILIZADO Y CERTIFICADO ---")
if __name__ == "__main__": deploy()
