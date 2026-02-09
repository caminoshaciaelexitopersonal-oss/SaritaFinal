from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico

class CapitanCreacionOrdenes(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"creacion": "operativo_creacion_orden"}

    def plan(self, mision):
        p = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        p.pasos_del_plan = {
            "1": {
                "teniente": "creacion",
                "descripcion": "Crear orden operativa desde directiva",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        p.save()
        return p
