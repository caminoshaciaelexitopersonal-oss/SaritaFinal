# backend/apps/sarita_agents/agents/general/sarita/coroneles/administrador_general/coronel.py

from .....coronel_template import CoronelTemplate
from .capitanes.capitan_auditoria_global import CapitanAuditoriaGlobal

class AdministradorGeneralCoronel(CoronelTemplate):
    """
    Coronel para el dominio de Administración General.
    Gestiona auditorías, seguridad, monitoreo y configuración global.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="administrador_general")

    def _get_capitanes(self) -> dict:
        return {
            "auditoria": CapitanAuditoriaGlobal(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        mission_info = directiva.get("mission", {})
        mission_type = mission_info.get("type")

        if mission_type == "AUDITORIA_GLOBAL":
            return self.capitanes.get("auditoria")

        return super()._select_capitan(directiva)
