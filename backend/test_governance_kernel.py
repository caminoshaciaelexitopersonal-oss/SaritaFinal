import os
import django
import sys

# Configurar el entorno de Django
sys.path.append('/workspace/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
from apps.admin_plataforma.models import Plan, GovernanceAuditLog

def test_kernel_flow():
    print("--- Iniciando prueba del GovernanceKernel ---")

    # 1. Obtener o crear un usuario administrador
    admin_user = CustomUser.objects.filter(is_superuser=True).first()
    if not admin_user:
        admin_user = CustomUser.objects.create_superuser(
            username='admin_test',
            email='admin@sarita.com',
            password='password123'
        )

    # 2. Instanciar el Kernel
    kernel = GovernanceKernel(user=admin_user)

    # 3. Definir parámetros para crear un plan
    params = {
        "nombre": "Plan de Prueba Kernel",
        "precio": 99.99,
        "frecuencia": "MENSUAL",
        "descripcion": "Creado desde el núcleo de gobernanza"
    }

    # 4. Ejecutar la intención
    print(f"Ejecutando intención 'PLATFORM_CREATE_PLAN'...")
    try:
        result = kernel.resolve_and_execute("PLATFORM_CREATE_PLAN", params)
        print(f"Resultado: {result}")

        # 5. Verificar persistencia
        plan_exists = Plan.objects.filter(nombre="Plan de Prueba Kernel").exists()
        print(f"¿Plan creado en BD?: {plan_exists}")

        # 6. Verificar auditoría
        audit_exists = GovernanceAuditLog.objects.filter(intencion="PLATFORM_CREATE_PLAN").exists()
        print(f"¿Auditoría registrada?: {audit_exists}")

        if plan_exists and audit_exists:
            print("\n✅ PRUEBA EXITOSA: El kernel resolvió y ejecutó la intención correctamente.")
        else:
            print("\n❌ PRUEBA FALLIDA: Falta persistencia o auditoría.")

    except Exception as e:
        print(f"\n❌ ERROR durante la ejecución: {e}")

if __name__ == "__main__":
    test_kernel_flow()
