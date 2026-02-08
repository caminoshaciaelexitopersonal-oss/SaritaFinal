# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/coronel.py

import logging
from .....coronel_template import CoronelTemplate
from .dominios.descubrimiento.coronel import CoronelDescubrimiento
from .dominios.conversion.coronel import CoronelConversion
from .dominios.contratacion.coronel import CoronelContratacion
from .dominios.relacion.coronel import CoronelRelacion
from .dominios.cumplimiento.coronel import CoronelCumplimiento

logger = logging.getLogger(__name__)

class CoronelComercialGeneral(CoronelTemplate):
    """
    CORONEL COMERCIAL GENERAL (1)
    Gobierna la política comercial completa del sistema SARITA.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="comercial")

    def _get_capitanes(self) -> dict:
        # En esta jerarquía reforzada, el Coronel General delega en Coroneles de Dominio
        # que actúan como "Super Capitanes" o simplemente se registran aquí.
        return {
            "descubrimiento": CoronelDescubrimiento(general=self.general),
            "conversion": CoronelConversion(general=self.general),
            "contratacion": CoronelContratacion(general=self.general),
            "relacion": CoronelRelacion(general=self.general),
            "cumplimiento": CoronelCumplimiento(general=self.general),
        }

    def handle_mission(self, mision):
        logger.info(f"CORONEL COMERCIAL GENERAL: Misión {mision.id} recibida. Analizando dominio comercial...")

        # Lógica de enrutamiento basada en el tipo de misión o parámetros
        m_type = mision.directiva_original.get("mission", {}).get("type", "")

        target_domain = self._resolve_domain(m_type)
        coronel_dominio = self.capitanes.get(target_domain)

        if coronel_dominio:
            logger.info(f"CORONEL COMERCIAL GENERAL: Delegando a Coronel de Dominio '{target_domain}'")
            return coronel_dominio.handle_mission(mision)

        return super().handle_mission(mision)

    def _resolve_domain(self, m_type: str) -> str:
        if any(x in m_type for x in ["MARKETING", "ADS", "SEO", "CATALOG", "RANKING"]):
            return "descubrimiento"
        if any(x in m_type for x in ["SALE", "CONVERSION", "FUNNEL", "QUOTE", "CART"]):
            return "conversion"
        if any(x in m_type for x in ["CONTRACT", "LEGAL", "KYC", "CONSENT"]):
            return "contratacion"
        if any(x in m_type for x in ["CRM", "LOYALTY", "SUPPORT", "FEEDBACK"]):
            return "relacion"
        if any(x in m_type for x in ["AUDIT", "COMPLIANCE", "FRAUD", "ANOMALY"]):
            return "cumplimiento"
        return "conversion" # Default
