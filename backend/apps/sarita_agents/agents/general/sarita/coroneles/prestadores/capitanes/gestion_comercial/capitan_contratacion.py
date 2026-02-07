# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_comercial/capitan_contratacion.py
import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import Mision, PlanTáctico

logger = logging.getLogger(__name__)

class CapitanContratacion(CapitanTemplate):
    """
    Agente de Contratación: Orquesta el flujo de cierre de ventas y generación de contratos.
    """

    def plan(self, mision: Mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (Contratación): Planificando cierre de contrato para misión {mision.id}")

        operacion_id = mision.directiva_original.get("parameters", {}).get("operacion_id")

        pasos = {
            "paso_1_confirmacion": {
                "descripcion": "Confirmar la operación comercial y generar la factura.",
                "teniente": "confirmador_comercial",
                "parametros": {"operacion_id": operacion_id}
            },
            "paso_2_archivado": {
                "descripcion": "Asegurar que la factura y el contrato queden archivados con integridad.",
                "teniente": "admin_persistencia_archivistica",
                "parametros": {"source_model": "FacturaVenta", "source_id": operacion_id}
            }
        }

        return PlanTáctico.objects.create(
            mision=mision,
            capitan_responsable=self.__class__.__name__,
            pasos_del_plan=pasos,
            estado='PLANIFICADO'
        )

    def _get_tenientes(self) -> dict:
        from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.operativos.tenientes_persistencia import AdminTenientePersistenciaArchivistica

        # Necesito un teniente confirmador
        class TenienteConfirmadorComercial:
            def execute_task(self, tarea):
                from apps.prestadores.mi_negocio.gestion_comercial.services import FacturacionService
                from apps.prestadores.mi_negocio.gestion_comercial.domain.models import OperacionComercial
                op = OperacionComercial.objects.get(id=tarea.parametros['operacion_id'])
                FacturacionService.facturar_operacion_confirmada(op)
                return {"status": "SUCCESS", "message": f"Factura generada para operacion {op.id}"}

        return {
            "confirmador_comercial": TenienteConfirmadorComercial(),
            "admin_persistencia_archivistica": AdminTenientePersistenciaArchivistica()
        }
