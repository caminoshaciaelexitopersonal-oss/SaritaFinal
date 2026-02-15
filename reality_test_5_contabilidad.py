# reality_test_5_contabilidad.py
import os
import django
import uuid
import time

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.sarita_agents.orchestrator import sarita_orchestrator
from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada, MicroTarea

def run_reality_test_contabilidad():
    print("🚀 INICIANDO PRUEBA DE REALIDAD FASE 5 — GESTIÓN CONTABLE")

    # 1. Directiva Maestra de Contabilidad
    directive = {
        "domain": "contabilidad",
        "mission": {"type": "FULL_ACCOUNTING_CYCLE"},
        "parameters": {
            "monto_ingreso": 500000,
            "monto_gasto": 150000,
            "periodo": "2024-05",
            "asiento_id": "AS-9988"
        }
    }

    print("--- General SARITA iniciando misión contable ---")
    mision = sarita_orchestrator.start_mission(directive)
    sarita_orchestrator.execute_mission(mision.id)

    # Verificación de la cadena de mando
    mision.refresh_from_db()
    print(f"✅ Misión {mision.id} | Estado: {mision.estado}")

    plan = PlanTáctico.objects.get(mision=mision)
    print(f"✅ Plan Táctico creado por: {plan.capitan_responsable}")

    tarea = TareaDelegada.objects.get(plan_tactico=plan)
    print(f"✅ Tarea supervisada por Teniente: {tarea.teniente_asignado}")

    # Verificación del Nivel 6 (Soldados)
    micro_tareas = MicroTarea.objects.filter(tarea_padre=tarea)
    print(f"🔍 MicroTareas ejecutadas por Soldados: {micro_tareas.count()}")

    expected_soldiers = [
        "SoldadoRegistroIngreso",
        "SoldadoRegistroGasto",
        "SoldadoConciliacionWallet",
        "SoldadoVerificacionFiscal",
        "SoldadoCierreParcial"
    ]

    for m in micro_tareas:
        print(f"      [Soldado {m.soldado_asignado}] -> {m.estado}")

    actual_soldiers = list(micro_tareas.values_list('soldado_asignado', flat=True))

    if len(micro_tareas) == 5 and all(s in actual_soldiers for s in expected_soldiers):
        print("\n🏆 CERTIFICACIÓN FASE 5.1/5.2 ALCANZADA: Jerarquía Contable Operativa.")
    else:
        print("\n❌ FALLO EN LA CADENA CONTABLE: Soldados incompletos.")

if __name__ == "__main__":
    run_reality_test_contabilidad()
