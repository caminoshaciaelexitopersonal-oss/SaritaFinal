import os
import django
import sys
from unittest.mock import MagicMock

# Configurar el entorno de Django
sys.path.append('/workspace/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.decision_intelligence.services.strategic_analysis import StrategicAnalysisService
from apps.decision_intelligence.models import StrategyProposal, DecisionMatrix
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

def test_decision_sovereignty_flow():
    print("--- Iniciando prueba de Soberanía Decisora (Fase 5) ---")

    # 1. Preparar Matrix (Bloquear alto riesgo)
    DecisionMatrix.objects.update_or_create(
        risk_level=StrategyProposal.RiskLevel.HIGH,
        defaults={'requires_approval': True, 'description': 'Solo soberano'}
    )

    # 2. Ejecutar análisis IA (Simulado)
    print("\n[PASO 1] IA analizando el sistema...")
    service = StrategicAnalysisService()
    # Mockear para que siempre use el mock interpret si no hay key
    service.semantic_engine.llm = None
    proposals = service.run_full_audit()

    print(f"Propuestas generadas: {len(proposals)}")
    for p in proposals:
        print(f" - [{p.domain}] Confianza: {p.nivel_confianza} | Riesgo: {p.nivel_riesgo}")

    # 3. Seleccionar propuesta normativa (Alto Riesgo)
    normative = StrategyProposal.objects.filter(domain=StrategyProposal.Domain.NORMATIVO).first()
    print(f"\n[PASO 2] Propuesta seleccionada: {normative.domain} (Riesgo: {normative.nivel_riesgo})")

    # 4. Intentar ejecutar sin aprobación
    print("[PASO 3] Intentando ejecutar propuesta PENDIENTE...")
    admin = CustomUser.objects.filter(is_superuser=True).first()
    kernel = GovernanceKernel(user=admin)
    try:
        kernel.execute_strategic_proposal(str(normative.id))
        print("❌ ERROR: Debió fallar por no estar aprobada.")
    except ValueError as e:
        print(f"✅ ÉXITO: Bloqueado correctamente (Estado no aprobado): {e}")

    # 5. Aprobar propuesta
    print("\n[PASO 4] Aprobando propuesta...")
    normative.status = StrategyProposal.Status.APPROVED
    normative.save()

    # 6. Intentar ejecutar con usuario regular (si existiera, pero usamos SuperAdmin para el kernel)
    # El test de kernel ya valida que si requiere aprobación y no es superuser falla.

    # 7. Ejecución Soberana
    print("[PASO 5] Ejecución soberana definitiva...")
    try:
        result = kernel.execute_strategic_proposal(str(normative.id))
        print(f"✅ ÉXITO: Propuesta ejecutada: {result['status']}")

        # Verificar estado final
        normative.refresh_from_db()
        print(f"Estado final en BD: {normative.status}")

        if normative.status == StrategyProposal.Status.EXECUTED:
            print("\n✅ PRUEBA INTEGRAL EXITOSA: IA propone, Humano aprueba, Sistema ejecuta.")
        else:
            print("\n❌ PRUEBA FALLIDA: El estado no cambió correctamente.")

    except Exception as e:
        print(f"❌ ERROR durante ejecución: {e}")

if __name__ == "__main__":
    test_decision_sovereignty_flow()
