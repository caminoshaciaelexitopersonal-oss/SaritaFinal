# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_operativa/sg_sst/capitan_sst.py
import logging
from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import Mision, PlanTáctico

logger = logging.getLogger(__name__)

class CapitanSST(CapitanTemplate):
    """
    Agente SST: Gestiona la matriz de riesgos y asegura el cumplimiento de la seguridad laboral.
    """

    def plan(self, mision: Mision) -> PlanTáctico:
        logger.info(f"CAPITÁN (SST): Planificando actualización de matriz para misión {mision.id}")

        pasos = {
            "actualizacion_matriz": {
                "descripcion": "Registrar o actualizar riesgos identificados en el entorno laboral.",
                "teniente": "admin_persistencia_operativa",
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
        from apps.sarita_agents.agents.general.sarita.coroneles.administrador_general.tenientes.operativos.tenientes_persistencia import AdminTenientePersistenciaOperativa
        return {
            "admin_persistencia_operativa": AdminTenientePersistenciaOperativa()
        }
