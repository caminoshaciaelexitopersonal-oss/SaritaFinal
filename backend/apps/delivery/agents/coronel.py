import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate
from .capitanes import (
    CapitanAfiliacionDelivery,
    CapitanGestionConductores,
    CapitanGestionVehiculos,
    CapitanAsignacionServicios,
    CapitanEjecucionOperativaDelivery,
    CapitanPagosLiquidacionesDelivery,
    CapitanAuditoriaDelivery
)

logger = logging.getLogger(__name__)

class CoronelDelivery(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general, domain="delivery")

    def _get_capitanes(self) -> dict:
        return {
            "afiliacion": CapitanAfiliacionDelivery(self),
            "conductores": CapitanGestionConductores(self),
            "vehiculos": CapitanGestionVehiculos(self),
            "asignacion": CapitanAsignacionServicios(self),
            "ejecucion": CapitanEjecucionOperativaDelivery(self),
            "pagos": CapitanPagosLiquidacionesDelivery(self),
            "auditoria": CapitanAuditoriaDelivery(self)
        }

    def _select_capitan(self, mission: dict):
        action = mission.get("action", "").lower()
        if "afiliar" in action or "empresa" in action:
            return self.capitanes["afiliacion"]
        if "conductor" in action:
            return self.capitanes["conductores"]
        if "vehiculo" in action:
            return self.capitanes["vehiculos"]
        if "solicitar" in action or "asignar" in action:
            return self.capitanes["asignacion"]
        if "iniciar" in action or "completar" in action or "evento" in action:
            return self.capitanes["ejecucion"]
        if "pago" in action or "liquidar" in action:
            return self.capitanes["pagos"]

        return self.capitanes["auditoria"]
