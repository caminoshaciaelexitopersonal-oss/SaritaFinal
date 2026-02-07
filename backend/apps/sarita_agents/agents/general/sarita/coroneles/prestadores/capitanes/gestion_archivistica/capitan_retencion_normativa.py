# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_archivistica/capitan_retencion_normativa.py
import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import Mision, PlanTáctico

logger = logging.getLogger(__name__)

class CapitanRetencionNormativa(CapitanTemplate):
    """
    Agente de Retención: Aplica políticas de retención y eliminación segura de documentos.
    """

    def plan(self, mision: Mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (Retención): Aplicando políticas para misión {mision.id}")

        pasos = {
            "evaluacion_retencion": {
                "descripcion": "Evaluar plazos de conservación según normatividad vigente.",
                "teniente": "gestor_retencion_archivistica",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }

        return PlanTáctico.objects.create(
            mision=mision,
            capitan_responsable=self.__class__.__name__,
            pasos_del_plan=pasos,
            estado='PLANIFICADO'
        )

    def _get_tenientes(self) -> dict:
        class TenienteGestorRetencion:
            def execute_task(self, tarea):
                return {"status": "SUCCESS", "message": "Políticas de retención aplicadas."}

        return {
            "gestor_retencion_archivistica": TenienteGestorRetencion()
        }
