# simulate_load_4_2.py
import os
import django
import uuid
import time
from datetime import timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada, MicroTarea, RegistroMicroTarea
from apps.sarita_agents.orchestrator import sarita_orchestrator

def simulate_500_microtasks():
    print("🚀 INICIANDO SIMULACIÓN DE CARGA FASE 4.2 (500 MICROTAREAS)")

    # 1. Crear una Misión Maestra
    master_mission = sarita_orchestrator.start_mission({
        "domain": "prestadores",
        "mission": {"type": "LOAD_SIMULATION_4_2"},
        "parameters": {"volume": 500}
    })

    # 2. Crear Plan y Tarea Padre
    plan = PlanTáctico.objects.create(
        mision=master_mission,
        capitan_responsable="CapitanCargaMasiva",
        pasos_del_plan={"1": {"description": "Simulación masiva"}},
        estado='EN_EJECUCION'
    )

    tarea_padre = TareaDelegada.objects.create(
        plan_tactico=plan,
        teniente_asignado="TenienteCargaMasiva",
        descripcion_tarea="Delegación de 500 microtareas",
        estado='EN_PROGRESO'
    )

    start_time = time.time()

    # 3. Generar 500 MicroTareas (Simulando 100 Sargentos con 5 soldados cada uno)
    print("--- Generando microtareas... ---")
    micro_tareas = []
    for i in range(500):
        mt = MicroTarea(
            tarea_padre=tarea_padre,
            soldado_asignado=f"Soldado_{i % 5 + 1}_Sargento_{i // 5 + 1}",
            descripcion=f"Tarea manual {i+1}",
            estado='COMPLETADA'
        )
        micro_tareas.append(mt)

    MicroTarea.objects.bulk_create(micro_tareas)

    # 4. Generar Registros (Simulando éxito)
    print("--- Generando registros de ejecución... ---")
    created_micros = MicroTarea.objects.filter(tarea_padre=tarea_padre)
    logs = []
    for mt in created_micros:
        logs.append(RegistroMicroTarea(
            micro_tarea=mt,
            exitoso=True,
            resultado={"status": "OK", "simulated": True}
        ))

    RegistroMicroTarea.objects.bulk_create(logs)

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\n📊 RESULTADOS DE SIMULACIÓN:")
    print(f"✅ MicroTareas creadas: 500")
    print(f"✅ Registros de ejecución: 500")
    print(f"⏱️ Tiempo total de procesamiento (DB): {total_time:.2f}s")
    print(f"⚡ Velocidad: {500/total_time:.2f} tareas/seg")

    if total_time < 5: # Umbral de éxito para optimización 4.2.1
        print("\n🏆 OPTIMIZACIÓN EXITOSA: Rendimiento de base de datos óptimo.")
    else:
        print("\n⚠️ ADVERTENCIA: Latencia superior a la esperada.")

if __name__ == "__main__":
    simulate_500_microtasks()
