from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico

class CapitanCalidadExperiencias(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"auditoria": "admin_persistencia_operativa"}

    def plan(self, mision):
        pasos = {"1": {"teniente": "auditoria", "descripcion": "Verificar estándares de calidad en la experiencia.", "parametros": mision.directiva_original.get("parameters", {})}}
        return PlanTáctico.objects.create(mision=mision, capitan_responsable=self.__class__.__name__, pasos_del_plan=pasos, estado='PLANIFICADO')
