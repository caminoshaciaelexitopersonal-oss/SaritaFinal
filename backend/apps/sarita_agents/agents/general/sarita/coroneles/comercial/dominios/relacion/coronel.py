# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/relacion/coronel.py

import logging
from .......coronel_template import CoronelTemplate

logger = logging.getLogger(__name__)

class CoronelRelacion(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_relacion")

    def _get_capitanes(self) -> dict:
        from ...prestadores.capitanes.gestion_comercial.capitan_relacion_clientes import CapitanRelacionClientes
        from ...prestadores.capitanes.gestion_comercial.capitan_mensajeria_y_envios_masivos import CapitanMensajeriaYEnviosMasivos
        from ...prestadores.capitanes.gestion_comercial.capitan_fidelizacion_lealtad import CapitanFidelizacionLealtad
        from ...prestadores.capitanes.gestion_comercial.capitan_soporte_viajero import CapitanSoporteViajero
        from ...prestadores.capitanes.gestion_comercial.capitan_postventa_feedback import CapitanPostventaFeedback

        return {
            "crm": CapitanRelacionClientes(coronel=self),
            "mensajeria": CapitanMensajeriaYEnviosMasivos(coronel=self),
            "lealtad": CapitanFidelizacionLealtad(coronel=self),
            "soporte": CapitanSoporteViajero(coronel=self),
            "postventa": CapitanPostventaFeedback(coronel=self),
        }
