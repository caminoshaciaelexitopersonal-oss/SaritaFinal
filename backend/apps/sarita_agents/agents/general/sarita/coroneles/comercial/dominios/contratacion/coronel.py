# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/contratacion/coronel.py

import logging
from .......coronel_template import CoronelTemplate

logger = logging.getLogger(__name__)

class CoronelContratacion(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_contratacion")

    def _get_capitanes(self) -> dict:
        from ...capitanes.capitan_contratacion import CapitanContratacion
        from ...capitanes.capitan_firma_digital import CapitanFirmaDigital
        from ...capitanes.capitan_kyc_verificacion import CapitanKYCVerificacion
        from ...capitanes.capitan_legalidad_y_privacidad import CapitanLegalidadYPrivacidad

        return {
            "contratacion": CapitanContratacion(coronel=self),
            "firma_digital": CapitanFirmaDigital(coronel=self),
            "kyc": CapitanKYCVerificacion(coronel=self),
            "legal_privacidad": CapitanLegalidadYPrivacidad(coronel=self),
        }
