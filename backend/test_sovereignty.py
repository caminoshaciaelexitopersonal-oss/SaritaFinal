import os
import django
import sys

# Configurar el entorno de Django
sys.path.append('/workspace/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel, AuthorityLevel
from apps.admin_plataforma.models import Plan, GovernanceAuditLog, GovernancePolicy

def test_sovereignty_and_policies():
    print("--- Iniciando prueba de Soberanía y Políticas ---")

    # 1. Obtener admin
    admin_user = CustomUser.objects.filter(is_superuser=True).first()
    kernel = GovernanceKernel(user=admin_user)

    # Limpiar planes previos de prueba
    Plan.objects.filter(nombre__startswith="Plan Bajo Bloqueo").delete()

    # Limpiar políticas previas para la prueba
    # Usamos una forma compatible con SQLite
    for p in GovernancePolicy.objects.all():
        if "PLATFORM_CREATE_PLAN" in p.affected_intentions:
            p.delete()

    # 2. Definir parámetros
    params = {
        "nombre": "Plan Bajo Bloqueo",
        "precio": 50.00,
        "frecuencia": "ANUAL",
        "descripcion": "No debería crearse"
    }

    # 3. CREAR BLOQUEO SOBERANO
    print("\n[PASO 1] Creando bloqueo soberano para 'PLATFORM_CREATE_PLAN'...")
    kernel.intervene_block_intention(
        intention_name="PLATFORM_CREATE_PLAN",
        reason="Mantenimiento de emergencia del sistema de suscripciones."
    )

    # 4. INTENTAR EJECUTAR
    print("\n[PASO 2] Intentando ejecutar intención bajo bloqueo...")
    try:
        kernel.resolve_and_execute("PLATFORM_CREATE_PLAN", params)
        print("❌ ERROR: La operación debió ser bloqueada.")
    except PermissionError as e:
        print(f"✅ ÉXITO: Operación bloqueada correctamente: {e}")
    except Exception as e:
        print(f"❌ ERROR INESPERADO: {type(e).__name__}: {e}")

    # 5. AUTORIZACIÓN CRÍTICA (OVERRIDE)
    print("\n[PASO 3] Intentando autorización soberana manual (OVERRIDE)...")
    try:
        result = kernel.intervene_authorize_critical("PLATFORM_CREATE_PLAN", params)
        print(f"✅ ÉXITO: El SuperAdmin forzó la ejecución: {result['status']}")

        # Verificar auditoría específica
        audit = GovernanceAuditLog.objects.filter(intencion="PLATFORM_CREATE_PLAN", success=True).first()
        if audit and audit.es_intervencion_soberana:
            print(f"✅ AUDITORÍA OK: Registrada como intervención soberana.")
        else:
            print("❌ ERROR DE AUDITORÍA: No se marcó como soberana.")

    except Exception as e:
        print(f"❌ ERROR durante override: {e}")

    # 6. LIMPIEZA
    GovernancePolicy.objects.all().delete()
    print("\n--- Prueba de Soberanía Finalizada ---")

if __name__ == "__main__":
    test_sovereignty_and_policies()
