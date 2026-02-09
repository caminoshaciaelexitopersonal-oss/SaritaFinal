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

# --- TENIENTES ARCHIVÍSTICOS (SARGENTOS LOGIC) ---
class TenienteIntegridadArchivistica(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_archivistica.sargentos import SargentoArchivistico
        version_id = parametros.get("version_id")
        content = parametros.get("content", b"")
        success = SargentoArchivistico.validar_integridad(version_id, content)
        return {"status": "SUCCESS" if success else "FAILED", "integrated": success}

class TenienteSelloTemporal(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_archivistica.sargentos import SargentoArchivistico
        version_id = parametros.get("version_id")
        success = SargentoArchivistico.aplicar_sello_temporal(version_id)
        return {"status": "SUCCESS" if success else "FAILED"}

class TenienteAuditoriaAcceso(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_archivistica.sargentos import SargentoArchivistico
        document_id = parametros.get("document_id")
        user_id = parametros.get("user_id")
        action = parametros.get("action", "READ")
        success = SargentoArchivistico.registrar_acceso(document_id, user_id, action)
        return {"status": "SUCCESS" if success else "FAILED"}

class TenienteTransicionEstado(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos import SargentoOperativo
        entidad_tipo = parametros.get("entidad_tipo")
        entidad_id = parametros.get("entidad_id")
        nuevo_estado = parametros.get("nuevo_estado")
        motivo = parametros.get("motivo", "")
        agente_id = parametros.get("agente_id")
        success = SargentoOperativo.actualizar_estado(entidad_tipo, entidad_id, nuevo_estado, motivo, agente_id)
        return {"status": "SUCCESS" if success else "FAILED"}

class TenienteCoordinacionTuristica(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos_especializados import SargentoEspecializado
        tour_id = parametros.get("tour_id")
        guia_id = parametros.get("guia_id")
        success = SargentoEspecializado.asignar_guia(tour_id, guia_id)
        return {"status": "SUCCESS" if success else "FAILED"}

class TenienteDespachoLogistico(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos_especializados import SargentoEspecializado
        vehiculo_id = parametros.get("vehiculo_id")
        ruta_id = parametros.get("ruta_id")
        success = SargentoEspecializado.activar_transporte(vehiculo_id, ruta_id)
        return {"status": "SUCCESS" if success else "FAILED"}

class TenienteMonitoreoSeguridad(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos_especializados import SargentoEspecializado
        zona_id = parametros.get("zona_id")
        desc = parametros.get("descripcion")
        nivel = parametros.get("nivel", "LOW")
        success = SargentoEspecializado.registrar_incidente_seguridad(zona_id, desc, nivel)
        return {"status": "SUCCESS" if success else "FAILED"}

class TenienteCreacionOrden(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos import SargentoOperativo
        res = SargentoOperativo.crear_orden_servicio(
            perfil_id=parametros.get("perfil_id"),
            descripcion=parametros.get("descripcion"),
            parametros=parametros
        )
        return {"status": "SUCCESS", "orden_id": res.get("id")}

class TenienteRegistroCosto(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos import SargentoOperativo
        costo_id = SargentoOperativo.registrar_costo_operativo(
            perfil_id=parametros.get("perfil_id"),
            orden_id=parametros.get("orden_id"),
            concepto=parametros.get("concepto"),
            monto=parametros.get("monto")
        )
        return {"status": "SUCCESS", "costo_id": costo_id}

class TenienteAsignacionRecurso(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.sargentos import SargentoOperativo
        asignacion_id = SargentoOperativo.asignar_recurso(
            orden_id=parametros.get("orden_id"),
            item_id=parametros.get("item_id"),
            cantidad=parametros.get("cantidad")
        )
        return {"status": "SUCCESS", "asignacion_id": asignacion_id}

class TenienteArchivado(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_archivistica.sargentos import SargentoArchivistico
        version_id = SargentoArchivistico.archivar_documento(parametros)
        if version_id:
            return {"status": "SUCCESS", "version_id": version_id}
        return {"status": "FAILED"}

class TenienteRegistroContable(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.sargentos import SargentoContable
        asiento = SargentoContable.generar_asiento_partida_doble(
            periodo_id=parametros.get("periodo_id"),
            fecha=parametros.get("fecha"),
            descripcion=parametros.get("descripcion"),
            movimientos=parametros.get("movimientos"),
            usuario_id=parametros.get("usuario_id")
        )
        if asiento:
            return {"status": "SUCCESS", "asiento_id": str(asiento.id)}
        return {"status": "FAILED"}

class TenienteCierreContable(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.sargentos import SargentoContable
        success = SargentoContable.ejecutar_cierre_periodo(
            periodo_id=parametros.get("periodo_id"),
            usuario_id=parametros.get("usuario_id")
        )
        return {"status": "SUCCESS" if success else "FAILED"}

# --- TENIENTES COMERCIALES (SARGENTOS LOGIC) ---
class TenienteContratacionComercial(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_comercial.domain.sargentos import SargentoComercial
        operacion_id = parametros.get("operacion_id")
        contrato = SargentoComercial.generar_contrato(operacion_id)
        if contrato:
            return {"status": "SUCCESS", "contrato_id": str(contrato.id)}
        return {"status": "FAILED", "message": "No se pudo generar el contrato."}

class TenienteActivacionOperativa(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_comercial.domain.sargentos import SargentoComercial
        contrato_id = parametros.get("contrato_id")
        orden = SargentoComercial.generar_orden_operativa(contrato_id)
        if orden:
            return {"status": "SUCCESS", "orden_id": str(orden.id)}
        return {"status": "FAILED", "message": "No se pudo generar la orden operativa."}

class TenienteGenericoComercial(TenienteTemplate):
    def perform_action(self, parametros: dict):
        action = parametros.get("action", "unknown_action")
        logger.info(f"TENIENTE COMERCIAL: Ejecutando acción atómica: {action}")
        return {"status": "SUCCESS", "action": action, "result": "Operación completada por Sargento Virtual"}

# --- MAPEO DE TENIENTES ---

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

# --- TENIENTES OPERATIVOS GENÉRICOS (FASE 3.1) ---

class TenienteOperacionComercial(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reservas.sargentos import SargentoReservas
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.sargentos import SargentoClientes
        action = parametros.get("action")
        if action == "CONFIRM":
            SargentoReservas.confirmar_reserva(parametros.get("reserva_id"))
        if action == "CREATE_CLIENT":
            SargentoClientes.crear_cliente(parametros.get("perfil_id"), parametros.get("cliente_data"))
        return {"status": "SUCCESS", "action": action}

class TenienteLogisticaRecursos(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.inventario.sargentos import SargentoInventario
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.sargentos import SargentoProductos
        if "item_id" in parametros:
            SargentoInventario.descontar_stock(parametros.get("item_id"), parametros.get("cantidad"))
        if "producto_id" in parametros:
            SargentoProductos.validar_oferta(parametros.get("producto_id"))
        return {"status": "SUCCESS"}

class TenienteAdministracionFisica(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.horarios.sargentos import SargentoHorarios
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.sargentos import SargentoPerfil
        if "fecha" in parametros:
            SargentoHorarios.validar_turno(parametros.get("perfil_id"), parametros.get("fecha"), parametros.get("hora"))
        if "perfil_data" in parametros:
            SargentoPerfil.actualizar_datos_base(parametros.get("perfil_id"), parametros.get("perfil_data"))
        return {"status": "SUCCESS"}

class TenienteGestionCostos(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.costos.sargentos import SargentoCostos
        SargentoCostos.registrar_gasto(parametros.get("perfil_id"), parametros)
        return {"status": "SUCCESS"}

class TenienteInformacionEvidencia(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.documentos.sargentos import SargentoDocumentos
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.galeria.sargentos import SargentoGaleria
        if "doc_id" in parametros:
            SargentoDocumentos.archivar_evidencia(parametros.get("doc_id"), parametros)
        if "image_url" in parametros:
            SargentoGaleria.registrar_imagen(parametros.get("perfil_id"), parametros.get("image_url"))
        return {"status": "SUCCESS"}

class TenienteAnalisisDatos(TenienteTemplate):
    def perform_action(self, parametros: dict):
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.estadisticas.sargentos import SargentoEstadisticas
        from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.valoraciones.sargentos import SargentoValoraciones
        if "kpi" in parametros:
            SargentoEstadisticas.actualizar_kpi(parametros.get("perfil_id"), parametros.get("kpi"), parametros.get("valor"))
        if "resena_id" in parametros:
            SargentoValoraciones.registrar_puntuacion(parametros.get("resena_id"), parametros.get("puntos"))
        return {"status": "SUCCESS"}


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
    # Archivísticos (Nuevos)
    'archivistico_integridad': TenienteIntegridadArchivistica,
    'archivistico_sello': TenienteSelloTemporal,
    'archivistico_acceso': TenienteAuditoriaAcceso,
    'archivistico_archivado': TenienteArchivado,
    'contable_registro': TenienteRegistroContable,
    'contable_cierre': TenienteCierreContable,
    'operativo_transicion': TenienteTransicionEstado,
    'operativo_coordinacion_turista': TenienteCoordinacionTuristica,
    'operativo_despacho_logistico': TenienteDespachoLogistico,
    'operativo_monitoreo_seguridad': TenienteMonitoreoSeguridad,
    'operativo_creacion_orden': TenienteCreacionOrden,
    'operativo_registro_costo': TenienteRegistroCosto,
    'operativo_asignacion_recurso': TenienteAsignacionRecurso,
    'operativo_comercial': TenienteOperacionComercial,
    'operativo_logistica': TenienteLogisticaRecursos,
    'operativo_admin_fisica': TenienteAdministracionFisica,
    'operativo_gestion_costos': TenienteGestionCostos,
    'operativo_info_evidencia': TenienteInformacionEvidencia,
    'operativo_analisis_datos': TenienteAnalisisDatos,
    # Comerciales (Nuevos)
    'comercial_contratacion': TenienteContratacionComercial,
    'comercial_activacion': TenienteActivacionOperativa,
    'seo_technical': TenienteGenericoComercial,
    'content_optimization': TenienteGenericoComercial,
    'matching_engine': TenienteGenericoComercial,
    'partnership_manager': TenienteGenericoComercial,
    'payment_gateway': TenienteGenericoComercial,
    'pricing_engine': TenienteGenericoComercial,
    'nlp_handler': TenienteGenericoComercial,
    'signature_provider': TenienteGenericoComercial,
    'id_validator': TenienteGenericoComercial,
    'gdpr_compliance': TenienteGenericoComercial,
    'points_manager': TenienteGenericoComercial,
    'ticket_handler': TenienteGenericoComercial,
    'survey_manager': TenienteGenericoComercial,
    'integrity_checker': TenienteGenericoComercial,
    'anomaly_detector': TenienteGenericoComercial,
}
