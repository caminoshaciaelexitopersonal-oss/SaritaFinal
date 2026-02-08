from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from apps.sarita_agents.models import PlanTáctico

class CapitanRutasEstrategicas(CapitanTemplate):
    def _get_tenientes(self) -> dict:
        return {"enrutamiento": "operativo_despacho_logistico"}

    def plan(self, mision):
        pasos = {"1": {"teniente": "enrutamiento", "descripcion": "Definir ruta óptima para el servicio logístico.", "parametros": mision.directiva_original.get("parameters", {})}}
        return PlanTáctico.objects.create(mision=mision, capitan_responsable=self.__class__.__name__, pasos_del_plan=pasos, estado='PLANIFICADO')
