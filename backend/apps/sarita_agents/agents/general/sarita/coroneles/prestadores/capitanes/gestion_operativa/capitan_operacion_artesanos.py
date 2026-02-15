from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanOperacionArtesanos(CapitanTemplate):
    """
    Misión: Gestionar las operaciones específicas de los artesanos y sus productos.
    """

    def __init__(self, coronel):
        super().__init__(coronel=coronel)


    def _get_tenientes(self) -> Dict[str, Any]:
        from ...tenientes.operativo_artesano_teniente import TenienteOperativoArtesano
        return {"operativo_artesano": TenienteOperativoArtesano()}

    def plan(self, mision):
        """
        El corazón del Capitán. Diseña el plan táctico para el taller Artesano.
        """
        p = self.coronel.get_or_create_plan_tactico(mision, self.__class__.__name__)
        p.pasos_del_plan = {
            "1": {
                "teniente": "operativo_artesano",
                "descripcion": "Gestión operativa del taller (Sargento + Soldados)",
                "parametros": mision.directiva_original.get("parameters", {})
            }
        }
        p.save()
        return p

