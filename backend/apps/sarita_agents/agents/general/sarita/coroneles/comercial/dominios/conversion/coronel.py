# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/conversion/coronel.py

import logging
from .......coronel_template import CoronelTemplate

logger = logging.getLogger(__name__)

class CoronelConversion(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_conversion")

    def _get_capitanes(self) -> dict:
        from ...capitanes.capitan_conversion import CapitanConversion
        from ...capitanes.capitan_embudos_conversion import CapitanEmbudosConversion
        from ...capitanes.capitan_implementacion_tecnica_de_embudos_y_crm import CapitanImplementacionTecnicaDeEmbudosYCRM
        from ...capitanes.capitan_pasarela_pagos import CapitanPasarelaPagos
        from ...capitanes.capitan_cotizaciones_dinamicas import CapitanCotizacionesDinamicas
        from ...capitanes.capitan_venta_conversacional import CapitanVentaConversacional
        from ...capitanes.capitan_comercial_hotelero import CapitanComercialHotelero
        from ...capitanes.capitan_comercial_gastronomico import CapitanComercialGastronomico
        from ...capitanes.capitan_comercial_turistico_tours import CapitanComercialTuristicoTours
        from ...capitanes.capitan_comercial_transporte import CapitanComercialTransporte
        from ...capitanes.capitan_comercial_artesanos import CapitanComercialArtesanos
        from ...capitanes.capitan_comercial_agencias import CapitanComercialAgencias
        from ...capitanes.capitan_comercial_internacional import CapitanComercialInternacional
        from ...capitanes.capitan_comercial_corporativo import CapitanComercialCorporativo
        from ...capitanes.capitan_comercial_voz import CapitanComercialVoz
        from ...capitanes.capitan_comercial_presencial import CapitanComercialPresencial

        return {
            "conversion": CapitanConversion(coronel=self),
            "embudos": CapitanEmbudosConversion(coronel=self),
            "crm_tech": CapitanImplementacionTecnicaDeEmbudosYCRM(coronel=self),
            "pagos": CapitanPasarelaPagos(coronel=self),
            "cotizaciones": CapitanCotizacionesDinamicas(coronel=self),
            "venta_conversacional": CapitanVentaConversacional(coronel=self),
            "hotel": CapitanComercialHotelero(coronel=self),
            "gastronomia": CapitanComercialGastronomico(coronel=self),
            "tours": CapitanComercialTuristicoTours(coronel=self),
            "transporte": CapitanComercialTransporte(coronel=self),
            "artesanos": CapitanComercialArtesanos(coronel=self),
            "agencias": CapitanComercialAgencias(coronel=self),
            "internacional": CapitanComercialInternacional(coronel=self),
            "corporativo": CapitanComercialCorporativo(coronel=self),
            "voz": CapitanComercialVoz(coronel=self),
            "presencial": CapitanComercialPresencial(coronel=self),
        }
