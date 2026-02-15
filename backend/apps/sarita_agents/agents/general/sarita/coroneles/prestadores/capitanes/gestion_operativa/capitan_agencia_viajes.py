from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanAgenciaViajes(CapitanTemplate):
    """
    Misión: Gestionar las operaciones específicas de las agencias de viajes.
    """

    def __init__(self, coronel):
        super().__init__(coronel=coronel)


    def _get_tenientes(self) -> Dict[str, Any]:
        from ...tenientes.operativo_agencia_teniente import TenienteOperativoAgencia
        return {"operativo_agencia": TenienteOperativoAgencia()}

    def plan(self, mision):
        """
        El corazón del Capitán. Diseña el plan táctico para la Agencia.
        """
        p = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        p.pasos_del_plan = {
            "1": {
                "teniente": "operativo_agencia",
                "descripcion": "Ejecución operativa completa de la agencia (Sargento + Soldados)",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        p.save()
        return p

