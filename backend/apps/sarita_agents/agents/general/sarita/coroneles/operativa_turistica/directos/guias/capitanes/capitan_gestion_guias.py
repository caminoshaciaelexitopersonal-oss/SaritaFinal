import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico

logger = logging.getLogger(__name__)

class CapitanGestionGuias(CapitanTemplate):
    """
    Capitán responsable de la ejecución táctica en la gestión de Guías Turísticos.
    """
    def _get_tenientes(self) -> dict:
        return {
            "teniente_guias": "teniente_guias"
        }

    def plan(self, mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (Guías): Creando plan para misión {mision.id}")

        pasos = {
            "1": {
                "teniente": "teniente_guias",
                "descripcion": "Ejecutar acción operativa de guías",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }

        return PlanTáctico.objects.create(
            mision=mision,
            capitan_responsable=self.__class__.__name__,
            pasos_del_plan=pasos,
            estado='PLANIFICADO'
        )
