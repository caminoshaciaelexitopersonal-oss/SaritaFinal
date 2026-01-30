# backend/apps/sarita_agents/tasks.py
# Archivo reconstruido manualmente para asegurar la integridad.
import logging
from celery import shared_task
from .models import TareaDelegada

# --- IMPORTS DE TENIENTES ---
# NOTA: Muchos tenientes son esqueletos con nombres de archivo inconsistentes.
# Se comentan los que impiden el arranque del sistema. Solo se dejan los funcionales.

# from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.teniente_auditoria_global import TenienteAuditoriaGlobal
# ... (otros del administrador_general)

from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador
from apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.tenienteauditoria_global import TenienteAuditoriaGlobal
from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.operativos.tenientes_persistencia import (
    AdminTenientePersistenciaComercial,
    AdminTenientePersistenciaContable,
    AdminTenientePersistenciaFinanciera,
    AdminTenientePersistenciaOperativa,
    AdminTenientePersistenciaArchivistica
)
from apps.sarita_agents.marketing.tenientes_marketing import (
    TenienteCalificacion, TenienteDolor, TenienteOferta, TenienteObjeciones, TenienteCierre
)
from apps.sarita_agents.agents.teniente_template import TenienteTemplate

# --- TENIENTES FINANCIEROS (Phase 4-F) ---
class TenienteCACCalculator(TenienteTemplate):
    def perform_action(self, parametros: dict):
        session_id = parametros.get("session_id")
        from apps.sarita_agents.finanzas.capitan_cac import CapitanCAC
        cap = CapitanCAC(coronel=None)
        cac = cap.calculate_cac(session_id)
        return {"cac": cac, "session_id": session_id}

class TenienteLTVCalculator(TenienteTemplate):
    def perform_action(self, parametros: dict):
        user_type = parametros.get("user_type", "prestador")
        plan_value = parametros.get("plan_value", 50.0)
        from apps.sarita_agents.finanzas.capitan_ltv import CapitanLTV
        cap = CapitanLTV(coronel=None)
        ltv = cap.estimate_ltv(user_type, plan_value)
        return {"ltv": ltv, "user_type": user_type}

class TenienteROICalculator(TenienteTemplate):
    def perform_action(self, parametros: dict):
        cac = parametros.get("cac", 1.0)
        ltv = parametros.get("ltv", 10.0)
        from apps.sarita_agents.finanzas.capitan_roi import CapitanROI
        cap = CapitanROI(coronel=None)
        roi = cap.evaluate_roi(cac, ltv)
        return {"roi": roi, "profitable": roi > 0}

# --- MAPEO DE TENIENTES ---
TENIENTE_MAP = {
    # Prestadores (Funcionales)
    'persistencia': TenientePersistenciaPrestador,
    'validacion': TenienteValidacionPrestador,
    # Administración General
    'auditoria_global': TenienteAuditoriaGlobal,
    # Operativos Super Admin (ERP Administrativo)
    'admin_persistencia_comercial': AdminTenientePersistenciaComercial,
    'admin_persistencia_contable': AdminTenientePersistenciaContable,
    'admin_persistencia_financiera': AdminTenientePersistenciaFinanciera,
    'admin_persistencia_operativa': AdminTenientePersistenciaOperativa,
    'admin_persistencia_archivistica': AdminTenientePersistenciaArchivistica,
    # Marketing & Ventas (Phase 4-M)
    'marketing_calificacion': TenienteCalificacion,
    'marketing_dolor': TenienteDolor,
    'marketing_oferta': TenienteOferta,
    'marketing_objeciones': TenienteObjeciones,
    'marketing_cierre': TenienteCierre,
    # Finanzas (Phase 4-F)
    'cac_calculator': TenienteCACCalculator,
    'ltv_calculator': TenienteLTVCalculator,
    'roi_calculator': TenienteROICalculator,
}

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 5}
)
def ejecutar_tarea_teniente(self, tarea_id: str):
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
        logger.error(f"CRITICAL: Tarea con ID {tarea_id} no encontrada.")
        return
    except Exception as e:
        logger.warning(f"Error en la ejecución de la tarea {tarea_id}. Reintentando. Error: {e}")
        raise self.retry(exc=e)

@shared_task(bind=True)
def ejecutar_mision_completa(self, mision_id: str):
    from .orchestrator import sarita_orchestrator
    try:
        sarita_orchestrator.execute_mission(mision_id)
    except Exception as e:
        logger.error(f"Error al ejecutar la misión completa {mision_id}: {e}", exc_info=True)

@shared_task
def consolidar_plan_tactico(resultados, plan_id: str):
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
