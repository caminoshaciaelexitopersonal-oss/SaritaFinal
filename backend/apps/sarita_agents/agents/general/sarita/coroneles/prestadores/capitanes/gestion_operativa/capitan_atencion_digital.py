from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico

class CapitanAtencionDigital(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"atencion": "admin_persistencia_operativa"}

    def plan(self, mision):
        pasos = {"1": {"teniente": "atencion", "descripcion": "Gestionar solicitud de atención vía canal digital.", "parametros": mision.directiva_original.get("parameters", {})}}
        return PlanTáctico.objects.create(mision=mision, capitan_responsable=self.__class__.__name__, pasos_del_plan=pasos, estado='PLANIFICADO')
