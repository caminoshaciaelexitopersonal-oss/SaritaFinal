import logging
from apps.sarita_agents.agents.coronel_template import CoronelTemplate

class CoronelOperativoHospedaje(CoronelTemplate):
    """
    Gobierna la operación especializada de Alojamientos y Hoteles.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="operativo_hospedaje")

    def _get_capitanes(self) -> dict:
        from .capitanes.capitan_gestion_habitaciones import CapitanGestionHabitaciones
        from .capitanes.capitan_checkin_checkout import CapitanCheckInCheckOut

        return {
            "gestion_habitaciones": CapitanGestionHabitaciones(coronel=self),
            "front_desk": CapitanCheckInCheckOut(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        m_type = directiva.get("mission", {}).get("type")
        mapping = {
            "UPDATE_ROOM_STATUS": "gestion_habitaciones",
            "EXECUTE_CHECK_IN": "front_desk",
            "EXECUTE_CHECK_OUT": "front_desk",
        }
        cap_key = mapping.get(m_type)
        return self.capitanes.get(cap_key) if cap_key else self.capitanes.get("gestion_habitaciones")
