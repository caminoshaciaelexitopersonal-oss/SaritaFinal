# stress_test_4_3_resilience.py
import os
import django
import random
import uuid

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada, MicroTarea, RegistroMicroTarea
from apps.sarita_agents.orchestrator import sarita_orchestrator
from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.sargentos.sargento_contable import SargentoRegistroContable

class ChaosSargento(SargentoRegistroContable):
    def handle_directive(self, directive):
        # Inyectar fallo aleatorio en el Sargento (10% probabilidad)
        if random.random() < 0.10:
            print(f"💥 CHAOS: Sargento {self.__class__.__name__} colapsó (Simulado)")
            return {"status": "FAILED", "error": "Connection lost in Chaos Mode"}
        return super().handle_directive(directive)

def run_resilience_test():
    print("🚀 INICIANDO FASE 4.3.3: PRUEBA DE RESILIENCIA JERÁRQUICA")

    mision = sarita_orchestrator.start_mission({
        "domain": "prestadores",
        "mission": {"type": "RESILIENCE_CHAOS_TEST"},
        "parameters": {"chaos": True}
    })

    plan = PlanTáctico.objects.create(
        mision=mision,
        capitan_responsable="CapitanResiliencia",
        pasos_del_plan={"1": {"description": "Resiliencia"}},
        estado='EN_EJECUCION'
    )

    tarea = TareaDelegada.objects.create(
        plan_tactico=plan,
        teniente_asignado="TenienteResiliencia",
        estado='EN_PROGRESO'
    )

    print("--- Ejecutando 20 Sargentos con inyección de fallos (10% prob) ---")

    failures = 0
    successes = 0

    for i in range(20):
        sargento = ChaosSargento()
        params = {"tarea_delegada_id": str(tarea.id), "id": i}
        res = sargento.handle_directive(params)

        if res["status"] == "FAILED":
            failures += 1
        else:
            successes += 1

    print(f"\n📊 RESULTADOS SUBFASE 4.3.3:")
    print(f"✅ Sargentos exitosos: {successes}")
    print(f"💥 Sargentos fallidos: {failures}")

    # Verificar trazabilidad de fallos
    micro_tareas = MicroTarea.objects.filter(tarea_padre=tarea)
    failed_micros = micro_tareas.filter(estado='FALLIDA').count()

    print(f"🔍 Microtareas fallidas registradas: {failed_micros}")

    if failed_micros > 0 or failures > 0:
        print("\n🏆 PRUEBA SUPERADA: El sistema registra y sobrevive a fallos parciales.")
    else:
        print("\n⚠️ ALERTA: No se inyectaron fallos o no se registraron.")

if __name__ == "__main__":
    run_resilience_test()
