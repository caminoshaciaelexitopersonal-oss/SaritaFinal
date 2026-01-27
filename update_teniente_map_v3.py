import os
import re

def update_teniente_map_v3():
    base_dir = "backend/apps/sarita_agents/agents/general/sarita/coroneles"
    tasks_filepath = "backend/apps/sarita_agents/tasks.py"

    tenientes = {} # {key: (import_path, class_name)}

    print("Escaneando para encontrar todos los Tenientes...")
    for coronel in os.listdir(base_dir):
        tenientes_dir = os.path.join(base_dir, coronel, "tenientes")
        if os.path.isdir(tenientes_dir):
            for filename in os.listdir(tenientes_dir):
                if filename.startswith("teniente_") and filename.endswith(".py"):
                    filepath = os.path.join(tenientes_dir, filename)
                    with open(filepath, 'r') as f:
                        content = f.read()

                    class_match = re.search(r"class\s+([A-Za-z0-9_]+)\(TenienteTemplate\):", content)
                    if class_match:
                        class_name = class_match.group(1)
                        # Usar imports absolutos desde la raíz de la app Django
                        module_path = f"apps.sarita_agents.agents.general.sarita.coroneles.{coronel}.tenientes.{filename[:-3]}"
                        map_key = filename.replace("teniente_", "").replace(".py", "")

                        tenientes[map_key] = (module_path, class_name)
                        print(f"  - Encontrado: {class_name} (clave: {map_key})")

    # --- Plantilla Completa del Archivo ---
    file_template = """# backend/apps/sarita_agents/tasks.py
# ESTE ARCHIVO ES AUTO-GENERADO. NO EDITAR MANUALMENTE LAS SECCIONES DE IMPORTS Y MAPEO.
import logging
from celery import shared_task
from .models import TareaDelegada

# --- IMPORTS DE TENIENTES (GENERADO AUTOMÁTICAMENTE) ---
{imports_block}

# --- MAPEO DE TENIENTES (GENERADO AUTOMÁTICAMENTE) ---
TENIENTE_MAP = {{
{map_block}
}}

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={{'max_retries': 3, 'countdown': 5}}
)
def ejecutar_tarea_teniente(self, tarea_id: str):
    \"\"\"
    Tarea de Celery para ejecutar la lógica de un Teniente de forma asíncrona.
    \"\"\"
    try:
        tarea = TareaDelegada.objects.get(id=tarea_id)
        tarea.estado = 'EN_PROGRESO'
        tarea.save()

        teniente_class = TENIENTE_MAP.get(tarea.teniente_asignado)
        if not teniente_class:
            raise ValueError(f"No se encontró la clase de Teniente para '{{tarea.teniente_asignado}}'.")

        teniente = teniente_class()
        teniente.execute_task(tarea)

    except TareaDelegada.DoesNotExist:
        logger.error(f"CRITICAL: Tarea con ID {{tarea_id}} no encontrada. No se puede ejecutar.")
        return
    except Exception as e:
        logger.warning(f"Error en la ejecución de la tarea {{tarea_id}}. Reintentando si es posible. Error: {{e}}")
        raise self.retry(exc=e)

@shared_task(bind=True)
def ejecutar_mision_completa(self, mision_id: str):
    \"\"\"
    Tarea de Celery para ejecutar una misión completa a través del orquestador.
    \"\"\"
    from .orchestrator import sarita_orchestrator
    try:
        sarita_orchestrator.execute_mission(mision_id)
    except Exception as e:
        logger.error(f"Error al ejecutar la misión completa {{mision_id}}: {{e}}", exc_info=True)

@shared_task
def consolidar_plan_tactico(resultados, plan_id: str):
    \"\"\"
    Se ejecuta cuando todas las tareas de un plan han terminado.
    \"\"\"
    from .models import PlanTáctico
    plan = PlanTáctico.objects.get(id=plan_id)

    if all(res['status'] == 'SUCCESS' for res in resultados):
        plan.estado = 'COMPLETADO'
    else:
        plan.estado = 'COMPLETADO_PARCIALMENTE'
    plan.save()

    reporte_capitan = {{"captain": plan.capitan_responsable, "status": plan.estado, "details": resultados}}
    reporte_final = {{"status": "FORWARDED", "captain_report": reporte_capitan, "report_from": f"Coronel ({{plan.mision.dominio}})"}}
    finalizar_mision.delay(plan.mision.id, reporte_final)

@shared_task
def finalizar_mision(mision_id: str, reporte_final: dict):
    \"\"\"
    Último paso. Guarda el reporte final y marca la misión como completada.
    \"\"\"
    from .models import Mision
    from django.utils import timezone
    mision = Mision.objects.get(id=mision_id)
    mision.resultado_final = reporte_final

    if reporte_final.get('captain_report', {{}}).get('status') == 'COMPLETADO':
        mision.estado = 'COMPLETADA'
    else:
        mision.estado = 'COMPLETADA_PARCIALMENTE'
    mision.timestamp_fin = timezone.now()
    mision.save()
"""

    # Generar el bloque de imports
    imports_list = [
        "from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador",
        "from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador"
    ]
    for key in sorted(tenientes.keys()):
        module_path, class_name = tenientes[key]
        imports_list.append(f"from {module_path} import {class_name}")
    imports_block = "\\n".join(imports_list)

    # Generar el bloque del mapa
    map_list = [
        "    'validacion': TenienteValidacionPrestador,",
        "    'persistencia': TenientePersistenciaPrestador,"
    ]
    for key in sorted(tenientes.keys()):
        _, class_name = tenientes[key]
        map_list.append(f"    '{key}': {class_name},")
    map_block = "\\n".join(map_list)

    # Poblar la plantilla
    final_content = file_template.format(imports_block=imports_block, map_block=map_block)

    # Escribir el nuevo contenido
    with open(tasks_filepath, 'w') as f:
        f.write(final_content)
    print(f"Archivo {tasks_filepath} reconstruido con éxito.")

if __name__ == "__main__":
    update_teniente_map_v3()
