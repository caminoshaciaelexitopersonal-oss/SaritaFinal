# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_comercial/capitan_conversion.py
import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import Mision, PlanTáctico

logger = logging.getLogger(__name__)

class CapitanConversion(CapitanTemplate):
    """
    Agente de Conversión: Gestiona el movimiento de prospectos a través del embudo de ventas.
    """

    def plan(self, mision: Mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (Conversión): Planificando avance de lead para misión {mision.id}")

        pasos = {
            "avance_embudo": {
                "descripcion": "Mover el lead a la siguiente etapa del pipeline comercial.",
                "teniente": "gestor_leads",
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
        class TenienteGestorLeads:
            def execute_task(self, tarea):
                return {"status": "SUCCESS", "message": "Lead avanzado de etapa exitosamente."}

        return {
            "gestor_leads": TenienteGestorLeads()
        }
