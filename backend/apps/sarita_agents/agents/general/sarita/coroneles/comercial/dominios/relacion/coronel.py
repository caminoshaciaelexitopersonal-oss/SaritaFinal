# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/relacion/coronel.py

import logging
from .......coronel_template import CoronelTemplate

logger = logging.getLogger(__name__)

class CoronelRelacion(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_relacion")

    def _get_capitanes(self) -> dict:
        from ...capitanes.capitan_relacion_clientes import CapitanRelacionClientes
        from ...capitanes.capitan_mensajeria_y_envios_masivos import CapitanMensajeriaYEnviosMasivos
        from ...capitanes.capitan_fidelizacion_lealtad import CapitanFidelizacionLealtad
        from ...capitanes.capitan_soporte_viajero import CapitanSoporteViajero
        from ...capitanes.capitan_postventa_feedback import CapitanPostventaFeedback

        return {
            "crm": CapitanRelacionClientes(coronel=self),
            "mensajeria": CapitanMensajeriaYEnviosMasivos(coronel=self),
            "lealtad": CapitanFidelizacionLealtad(coronel=self),
            "soporte": CapitanSoporteViajero(coronel=self),
            "postventa": CapitanPostventaFeedback(coronel=self),
        }
