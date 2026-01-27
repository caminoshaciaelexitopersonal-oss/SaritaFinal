# backend/apps/sarita_agents/tasks.py
# ESTE ARCHIVO ES AUTO-GENERADO. NO EDITAR MANUALMENTE LAS SECCIONES DE IMPORTS Y MAPEO.
import logging
from celery import shared_task
from .models import TareaDelegada

# --- IMPORTS DE TENIENTES (GENERADO AUTOMÁTICAMENTE) ---
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.teniente_auditoria_global import TenienteAuditoriaGlobal
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.teniente_configuracion_sistema import TenienteConfiguracionSistema
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.teniente_gobernanza_agentes import TenienteGobernanzaAgentes
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.teniente_monitoreo_plataforma import TenienteMonitoreoPlataforma
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.teniente_seguridad_accesos import TenienteSeguridadAccesos
from apps.sarita_agents.agents.general.sarita.coroneles.clientes_turistas.tenientes.teniente_busqueda_servicios import TenienteBusquedaServicios
from apps.sarita_agents.agents.general.sarita.coroneles.clientes_turistas.tenientes.teniente_contexto_viaje import TenienteContextoViaje
from apps.sarita_agents.agents.general.sarita.coroneles.clientes_turistas.tenientes.teniente_experiencia_turista import TenienteExperienciaTurista
from apps.sarita_agents.agents.general.sarita.coroneles.clientes_turistas.tenientes.teniente_gestion_perfil import TenienteGestionPerfil
from apps.sarita_agents.agents.general.sarita.coroneles.clientes_turistas.tenientes.teniente_pqrs import TenientePqrs
from apps.sarita_agents.agents.general.sarita.coroneles.clientes_turistas.tenientes.teniente_reservas_turista import TenienteReservasTurista
from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador
from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador


# --- MAPEO DE TENIENTES (GENERADO AUTOMÁTICAMENTE) ---
TENIENTE_MAP = {
    'auditoria_global': TenienteAuditoriaGlobal,
    'configuracion_sistema': TenienteConfiguracionSistema,
    'gobernanza_agentes': TenienteGobernanzaAgentes,
    'monitoreo_plataforma': TenienteMonitoreoPlataforma,
    'seguridad_accesos': TenienteSeguridadAccesos,
    'busqueda_servicios': TenienteBusquedaServicios,
    'contexto_viaje': TenienteContextoViaje,
    'experiencia_turista': TenienteExperienciaTurista,
    'gestion_perfil': TenienteGestionPerfil,
    'pqrs': TenientePqrs,
    'reservas_turista': TenienteReservasTurista,
    'persistencia': TenientePersistenciaPrestador,
    'validacion': TenienteValidacionPrestador,
}

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 5}
)
def ejecutar_tarea_teniente(self, tarea_id: str):
    """
    Tarea de Celery para ejecutar la lógica de un Teniente de forma asíncrona.
    """
    try:
        tarea = TareaDelegada.objects.get(id=tarea_id)
        tarea.estado = 'EN_PROGRESO'
        tarea.save()

        teniente_class = TENIENTE_MAP.get(tarea.teniente_asignado)
        if not teniente_class:
            raise ValueError(f"No se encontró la clase de Teniente para '{tarea.teniente_asignado}'.")

        teniente = teniente_class()
        teniente.execute_task(tarea)

    except TareaDelegada.DoesNotExist:
        logger.error(f"CRITICAL: Tarea con ID {tarea_id} no encontrada. No se puede ejecutar.")
        return
    except Exception as e:
        logger.warning(f"Error en la ejecución de la tarea {tarea_id}. Reintentando si es posible. Error: {e}")
        raise self.retry(exc=e)

@shared_task(bind=True)
def ejecutar_mision_completa(self, mision_id: str):
    """
    Tarea de Celery para ejecutar una misión completa a través del orquestador.
    """
    from .orchestrator import sarita_orchestrator
    try:
        sarita_orchestrator.execute_mission(mision_id)
    except Exception as e:
        logger.error(f"Error al ejecutar la misión completa {mision_id}: {e}", exc_info=True)

@shared_task
def consolidar_plan_tactico(resultados, plan_id: str):
    """
    Se ejecuta cuando todas las tareas de un plan han terminado.
    """
    from .models import PlanTáctico
    plan = PlanTáctico.objects.get(id=plan_id)

    if all(res['status'] == 'SUCCESS' for res in resultados):
        plan.estado = 'COMPLETADO'
    else:
        plan.estado = 'COMPLETADO_PARCIALMENTE'
    plan.save()

    reporte_capitan = {"captain": plan.capitan_responsable, "status": plan.estado, "details": resultados}
    reporte_final = {"status": "FORWARDED", "captain_report": reporte_capitan, "report_from": f"Coronel ({plan.mision.dominio})"}
    finalizar_mision.delay(plan.mision.id, reporte_final)

@shared_task
def finalizar_mision(mision_id: str, reporte_final: dict):
    """
    Último paso. Guarda el reporte final y marca la misión como completada.
    """
    from .models import Mision
    from django.utils import timezone
    mision = Mision.objects.get(id=mision_id)
    mision.resultado_final = reporte_final

    if reporte_final.get('captain_report', {}).get('status') == 'COMPLETADO':
        mision.estado = 'COMPLETADA'
    else:
        mision.estado = 'COMPLETADA_PARCIALMENTE'
    mision.timestamp_fin = timezone.now()
    mision.save()
