# stress_test_4_3_load.py
import os
import django
import time
import uuid
import threading
from concurrent.futures import ThreadPoolExecutor

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada, MicroTarea
from apps.sarita_agents.orchestrator import sarita_orchestrator
from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.sargentos.sargento_contable import SargentoRegistroContable

def simulate_sargento_execution(sargento_id, tarea_padre_id, params):
    sargento = SargentoRegistroContable()
    directive = params.copy()
    directive["tarea_delegada_id"] = str(tarea_padre_id)
    return sargento.handle_directive(directive)

def run_stress_test_load():
    print("🚀 INICIANDO FASE 4.3.1: SIMULACIÓN DE CARGA OPERATIVA MASIVA")

    # 1. Crear Misión Maestra
    mision = sarita_orchestrator.start_mission({
        "domain": "prestadores",
        "mission": {"type": "STRESS_TEST_4_3"},
        "parameters": {"total_microtasks": 1000}
    })

    plan = PlanTáctico.objects.create(
        mision=mision,
        capitan_responsable="CapitanStressTest",
        pasos_del_plan={"1": {"description": "Carga masiva"}},
        estado='EN_EJECUCION'
    )

    # Crear 50 TareasDelegadas (una para cada Sargento)
    tareas_padre = []
    for i in range(50):
        t = TareaDelegada.objects.create(
            plan_tactico=plan,
            teniente_asignado=f"TenienteStress_{i+1}",
            descripcion_tarea=f"Supervisión bloque {i+1}",
            estado='EN_PROGRESO'
        )
        tareas_padre.append(t)

    print(f"✅ Misión, Plan y 50 Tareas de Supervisión creadas.")

    start_time = time.time()

    # Ejecutar 50 Sargentos en paralelo, cada uno con 5 soldados (250 soldados totales)
    # Para llegar a 1,000 microtareas, cada Sargento debería procesar 4 rondas o simplemente
    # escalamos los Sargentos. El requerimiento dice 50 Sargentos / 250 Soldados.
    # 50 sargentos * 5 soldados = 250 soldados.
    # Si queremos 1,000 microtareas, podemos hacer 4 rondas de ejecución.

    print("--- Ejecutando Sargentos y Soldados en paralelo ---")

    all_results = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for round_num in range(4):
            for i, tarea in enumerate(tareas_padre):
                params = {
                    "comprobante_id": str(uuid.uuid4()),
                    "asiento_id": f"ST-{round_num}-{i}",
                    "operacion_id": str(uuid.uuid4()),
                    "tx_id": f"TX-{round_num}-{i}",
                    "round": round_num
                }
                futures.append(executor.submit(simulate_sargento_execution, i, tarea.id, params))

        for future in futures:
            all_results.append(future.result())

    end_time = time.time()
    total_duration = end_time - start_time

    # Verificaciones finales
    total_microtareas = MicroTarea.objects.filter(tarea_padre__plan_tactico=plan).count()
    orphan_misisons = Mision.objects.filter(estado='PENDIENTE').count() # Simplificado

    print(f"\n📊 RESULTADOS SUBFASE 4.3.1:")
    print(f"⏱️ Tiempo total: {total_duration:.2f}s")
    print(f"✅ Microtareas registradas: {total_microtareas}")
    print(f"⚡ Rendimiento: {total_microtareas/total_duration:.2f} tareas/seg")
    print(f"🔍 Misiones huérfanas detectadas: {orphan_misisons}")

    if total_microtareas == 1000 and total_duration < 30:
        print("\n🏆 PRUEBA SUPERADA: Estabilidad jerárquica confirmada bajo carga masiva.")
    else:
        print("\n⚠️ ALERTA: Rendimiento inferior al umbral o pérdida de datos.")

if __name__ == "__main__":
    run_stress_test_load()
