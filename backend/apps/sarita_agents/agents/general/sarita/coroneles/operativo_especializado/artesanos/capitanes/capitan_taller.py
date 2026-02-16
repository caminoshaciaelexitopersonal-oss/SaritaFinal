from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico
from apps.sarita_agents.agents.general.sarita.coroneles.operativo_especializado.tenientes_especializados import TenienteOperativoArtesano

class CapitanTaller(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"teniente_artesano": TenienteOperativoArtesano()}

    def plan(self, mision):
        p = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        p.pasos_del_plan = {
            "1": {
                "teniente": "teniente_artesano",
                "descripcion": f"Operación de Taller: {mision.directiva_original.get('action')}",
                "parametros": mision.directiva_original.get('parameters', {})
            }
        }
        p.save()
        return p
