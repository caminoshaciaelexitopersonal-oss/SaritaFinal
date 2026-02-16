# stress_test_4_3_governance.py
import os
import django
import time
from concurrent.futures import ThreadPoolExecutor

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel, AuthorityLevel

def attempt_privilege_escalation(user):
    kernel = GovernanceKernel(user=user)
    try:
        # Intención de nivel SOVEREIGN
        kernel.resolve_and_execute("PLATFORM_TRANSFER_OWNERSHIP", {"new_owner": "hacker@malicious.com"})
        return "SUCCESS (FAIL: Escalation allowed!)"
    except PermissionError:
        return "REJECTED (PASS: Security intact)"
    except Exception as e:
        return f"ERROR: {str(e)}"

def run_governance_stress_test():
    print("🚀 INICIANDO FASE 4.3.4: VALIDACIÓN DE GOBERNANZA BAJO PRESIÓN")

    # 1. Crear un usuario de nivel OPERATIONAL
    User = CustomUser
    user, _ = User.objects.get_or_create(
        username="operative_user",
        email="op@sarita.com",
        role="TURISTA" # Nivel Operacional más bajo
    )

    print(f"--- Intentando 50 escalamientos de privilegios concurrentes ---")

    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(attempt_privilege_escalation, user) for _ in range(50)]
        for future in futures:
            results.append(future.result())

    rejected_count = results.count("REJECTED (PASS: Security intact)")
    success_count = results.count("SUCCESS (FAIL: Escalation allowed!)")

    print(f"\n📊 RESULTADOS SUBFASE 4.3.4:")
    print(f"✅ Intentos bloqueados: {rejected_count}")
    print(f"❌ Intentos exitosos: {success_count}")

    if success_count == 0 and rejected_count == 50:
        print("\n🏆 PRUEBA SUPERADA: El GovernanceKernel es inquebrantable bajo presión.")
    else:
        print("\n🚨 VULNERABILIDAD DETECTADA: El sistema permitió escalamiento bajo carga.")

if __name__ == "__main__":
    run_governance_stress_test()
