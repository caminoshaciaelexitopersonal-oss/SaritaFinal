# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/conversion/coronel.py

import logging
from .......coronel_template import CoronelTemplate

logger = logging.getLogger(__name__)

class CoronelConversion(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_conversion")

    def _get_capitanes(self) -> dict:
        from ...prestadores.capitanes.gestion_comercial.capitan_conversion import CapitanConversion
        from ...prestadores.capitanes.gestion_comercial.capitan_embudos_conversion import CapitanEmbudosConversion
        from ...prestadores.capitanes.gestion_comercial.capitan_implementacion_tecnica_de_embudos_y_crm import CapitanImplementacionTecnicaDeEmbudosYCRM
        from ...prestadores.capitanes.gestion_comercial.capitan_pasarela_pagos import CapitanPasarelaPagos
        from ...prestadores.capitanes.gestion_comercial.capitan_cotizaciones_dinamicas import CapitanCotizacionesDinamicas
        from ...prestadores.capitanes.gestion_comercial.capitan_venta_conversacional import CapitanVentaConversacional
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_hotelero import CapitanComercialHotelero
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_gastronomico import CapitanComercialGastronomico
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_turistico_tours import CapitanComercialTuristicoTours
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_transporte import CapitanComercialTransporte
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_artesanos import CapitanComercialArtesanos
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_agencias import CapitanComercialAgencias
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_internacional import CapitanComercialInternacional
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_corporativo import CapitanComercialCorporativo
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_voz import CapitanComercialVoz
        from ...prestadores.capitanes.gestion_comercial.capitan_comercial_presencial import CapitanComercialPresencial

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
