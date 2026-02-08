from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico
import logging

logger = logging.getLogger(__name__)

class CapitanComercialInternacional(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"generico": "teniente_comercial_base"}

    def plan(self, mision) -> PlanTáctico:
        logger.info(f"CAPITÁN CapitanComercialInternacional: Planificando misión comercial especializada.")
        pasos = {"1": {"teniente": "generico", "descripcion": "Ejecutar acción comercial especializada", "parametros": mision.directiva_original.get("parameters", {})}}
        return self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
