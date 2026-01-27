# backend/apps/sarita_agents/tasks.py
import logging
from celery import shared_task
from backend.models import TareaDelegada
from backend.agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador
from backend.agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador

# --- Mapeo de Tenientes ---
# Este registro centralizado permite instanciar al teniente correcto a partir de un string.
TENIENTE_MAP = {
    'validacion': TenienteValidacionPrestador,
    'persistencia': TenientePersistenciaPrestador,
}

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    autoretry_for=(Exception,), # Reintentar en cualquier excepción.
    retry_kwargs={'max_retries': 3, 'countdown': 5} # Reintentar hasta 3 veces, con 5s de espera.
)
def ejecutar_tarea_teniente(self, tarea_id: str):
    """
    Tarea de Celery para ejecutar la lógica de un Teniente de forma asíncrona.
    """
    try:
        tarea = TareaDelegada.objects.get(id=tarea_id)

        # Actualizar estado para reflejar que está siendo procesada por un worker.
        tarea.estado = 'EN_PROGRESO'
        tarea.save()

        teniente_class = TENIENTE_MAP.get(tarea.teniente_asignado)
        if not teniente_class:
            raise ValueError(f"No se encontró la clase de Teniente para '{tarea.teniente_asignado}'.")

        # Instanciar y ejecutar
        teniente = teniente_class()
        teniente.execute_task(tarea)

    except TareaDelegada.DoesNotExist:
        # Si la tarea no existe, no podemos hacer nada. No reintentar.
        logger.error(f"CRITICAL: Tarea con ID {tarea_id} no encontrada. No se puede ejecutar.")
        return
    except Exception as e:
        # Si ocurre un error inesperado, Celery lo capturará y gestionará el reintento.
        logger.warning(f"Error en la ejecución de la tarea {tarea_id}. Reintentando si es posible. Error: {e}")
        raise self.retry(exc=e)

@shared_task(bind=True)
def ejecutar_mision_completa(self, mision_id: str):
    """
    Tarea de Celery para ejecutar una misión completa a través del orquestador.
    Esto permite que la API responda inmediatamente.
    """
    from backend.orchestrator import sarita_orchestrator

    try:
        sarita_orchestrator.execute_mission(mision_id)
    except Exception as e:
        logger.error(f"Error al ejecutar la misión completa {mision_id}: {e}", exc_info=True)
        # Opcional: Marcar la misión como fallida aquí si el orquestador no lo hizo.

@shared_task
def consolidar_plan_tactico(resultados, plan_id: str):
    """
    Se ejecuta cuando todas las tareas de un plan han terminado.
    Consolida los resultados y reporta hacia arriba.
    """
    from backend.models import PlanTáctico

    plan = PlanTáctico.objects.get(id=plan_id)

    # Simple lógica para determinar el estado final del plan
    if all(res['status'] == 'SUCCESS' for res in resultados):
        plan.estado = 'COMPLETADO'
    else:
        plan.estado = 'COMPLETADO_PARCIALMENTE' # o 'FALLIDO'
    plan.save()

    # Simula el método report() del Capitán
    reporte_capitan = {
        "captain": plan.capitan_responsable,
        "status": plan.estado,
        "details": resultados
    }

    # El Coronel empaquetaría esto, aquí lo simulamos
    reporte_final = {
        "status": "FORWARDED",
        "captain_report": reporte_capitan,
        "report_from": f"Coronel ({plan.mision.dominio})"
    }

    finalizar_mision.delay(plan.mision.id, reporte_final)

@shared_task
def finalizar_mision(mision_id: str, reporte_final: dict):
    """
    Último paso. Guarda el reporte final y marca la misión como completada.
    """
    from backend.models import Mision
    from django.utils import timezone

    mision = Mision.objects.get(id=mision_id)
    mision.resultado_final = reporte_final

    # Determinar el estado final basado en el reporte
    if reporte_final.get('captain_report', {}).get('status') == 'COMPLETADO':
        mision.estado = 'COMPLETADA'
    else:
        mision.estado = 'COMPLETADA_PARCIALMENTE'

    mision.timestamp_fin = timezone.now()
    mision.save()
