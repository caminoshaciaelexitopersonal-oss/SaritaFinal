# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/descubrimiento/coronel.py

import logging
from .......coronel_template import CoronelTemplate
# Importar capitanes (se moverán o crearán aquí)

logger = logging.getLogger(__name__)

class CoronelDescubrimiento(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_descubrimiento")

    def _get_capitanes(self) -> dict:
        from ...capitanes.capitan_marketing import CapitanMarketing
        from ...capitanes.capitan_publicidad_y_adquisicion_de_trafico_ads import CapitanPublicidadYAdquisicionDeTraficoADS
        from ...capitanes.capitan_gestion_operativa_de_contenidos_comerciales import CapitanGestionOperativaDeContenidosComerciales
        from ...capitanes.capitan_produccion_y_automatizacion_audiovisual import CapitanProduccionYAutomatizacionAudiovisual
        from ...capitanes.capitan_seo_turistico import CapitanSEOTuristico
        from ...capitanes.capitan_recomendaciones_sadi import CapitanRecomendacionesSADI
        from ...capitanes.capitan_alianzas_comerciales import CapitanAlianzasComerciales

        # Nuevos capitanes especializados
        # from .capitanes.capitan_catalogo import CapitanCatalogo
        # ...

        return {
            "marketing": CapitanMarketing(coronel=self),
            "ads": CapitanPublicidadYAdquisicionDeTraficoADS(coronel=self),
            "contenidos": CapitanGestionOperativaDeContenidosComerciales(coronel=self),
            "audiovisual": CapitanProduccionYAutomatizacionAudiovisual(coronel=self),
            "seo": CapitanSEOTuristico(coronel=self),
            "sadi_matching": CapitanRecomendacionesSADI(coronel=self),
            "alianzas": CapitanAlianzasComerciales(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        m_type = directiva.get("mission", {}).get("type", "")
        if "MARKETING" in m_type: return self.capitanes.get("marketing")
        if "ADS" in m_type: return self.capitanes.get("ads")
        if "SEO" in m_type: return self.capitanes.get("seo")
        if "SADI" in m_type: return self.capitanes.get("sadi_matching")
        return self.capitanes.get("marketing")
