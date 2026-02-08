from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico

class CapitanMonitoreoZonas(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"monitoreo": "operativo_monitoreo_seguridad"}

    def plan(self, mision):
        pasos = {"1": {"teniente": "monitoreo", "descripcion": "Ejecutar monitoreo preventivo de zona crítica.", "parametros": mision.directiva_original.get("parameters", {})}}
        return PlanTáctico.objects.create(mision=mision, capitan_responsable=self.__class__.__name__, pasos_del_plan=pasos, estado='PLANIFICADO')
