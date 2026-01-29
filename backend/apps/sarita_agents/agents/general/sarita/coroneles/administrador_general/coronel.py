# backend/apps/sarita_agents/agents/general/sarita/coroneles/administrador_general/coronel.py

from .....coronel_template import CoronelTemplate
from .capitanes.capitan_auditoria_global import CapitanAuditoriaGlobal
from .capitanes.operativos.capitan_ventas import AdminCapitanVentas
from .capitanes.operativos.capitan_contabilidad import AdminCapitanContabilidad
from .capitanes.operativos.capitan_financiero import AdminCapitanFinanciero

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
            "admin_ventas": AdminCapitanVentas(coronel=self),
            "admin_contabilidad": AdminCapitanContabilidad(coronel=self),
            "admin_financiero": AdminCapitanFinanciero(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        mission_info = directiva.get("mission", {})
        mission_type = mission_info.get("type")

        if mission_type == "AUDITORIA_GLOBAL":
            return self.capitanes.get("auditoria")
        elif mission_type == "ADMIN_VENTAS":
            return self.capitanes.get("admin_ventas")
        elif mission_type == "ADMIN_CONTABILIDAD":
            return self.capitanes.get("admin_contabilidad")
        elif mission_type == "ADMIN_FINANCIERO":
            return self.capitanes.get("admin_financiero")

        return super()._select_capitan(directiva)
