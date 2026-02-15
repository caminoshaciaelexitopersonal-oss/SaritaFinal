# reality_test_4_1.py
import os
import django
import uuid

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.sarita_agents.orchestrator import sarita_orchestrator
from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada, MicroTarea

def run_test():
    print("🚀 INICIANDO PRUEBA DE REALIDAD FASE 4.1 - JERARQUÍA COMPLETA")

    directive = {
        "domain": "prestadores",
        "mission": {"type": "EXECUTE_OPERATIONAL_FLOW"}, # Fallback a lo que maneje el Coronel o tipo específico
        "parameters": {
            "reserva_id": str(uuid.uuid4()),
            "vuelo": "AV2401",
            "destino": "Puerto Gaitán"
        }
    }

    # Forzar que el Coronel elija CapitanAgenciaViajes si es posible,
    # o simplemente llamarlo directamente para la prueba si el enrutamiento es genérico.

    from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.coronel import PrestadoresCoronel
    coronel = PrestadoresCoronel(general=sarita_orchestrator)

    # Creamos la misión manualmente para tener control del ID
    mision = sarita_orchestrator.start_mission(directive)
    print(f"✅ Misión creada: {mision.id}")

    # Ejecutamos vía Coronel
    print("--- Delegando a Coronel ---")
    mision.estado = 'EN_PROGRESO'
    mision.save()

    # Simulamos el enrutamiento del Coronel al Capitan de Agencia
    from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.capitanes.gestion_operativa.capitan_agencia_viajes import CapitanAgenciaViajes
    capitan = CapitanAgenciaViajes(coronel=coronel)

    print(f"--- Capitán {capitan.__class__.__name__} planificando ---")
    plan = capitan.plan(mision)

    print(f"--- Capitán delegando a Teniente ---")
    # Usamos el modo EAGER si está configurado para que se ejecute síncronamente en el test
    capitan.delegate(plan)

    # Verificaciones
    plan.refresh_from_db()
    print(f"📊 Estado del Plan: {plan.estado}")

    tareas = TareaDelegada.objects.filter(plan_tactico=plan)
    print(f"📋 Tareas creadas: {tareas.count()}")

    for tarea in tareas:
        print(f"  - Tarea: {tarea.descripcion_tarea} | Estado: {tarea.estado}")
        # En la Fase 4.1, el Teniente debió crear MicroTareas
        micros = MicroTarea.objects.filter(tarea_padre=tarea)
        print(f"    🔍 MicroTareas (Soldados): {micros.count()}")
        for m in micros:
            print(f"      [Soldado {m.soldado_asignado}] -> {m.estado}")

    if tareas.count() > 0 and MicroTarea.objects.filter(tarea_padre__plan_tactico=plan).count() == 5:
        print("\n🏆 CERTIFICACIÓN ALCANZADA: Jerarquía 4.1 operativa al 100%.")
    else:
        print("\n❌ FALLO EN LA CADENA: No se detectaron los 5 soldados reglamentarios.")

if __name__ == "__main__":
    run_test()
