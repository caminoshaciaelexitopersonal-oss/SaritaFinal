# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/coronel.py

from .....coronel_template import CoronelTemplate

# --- GESTION COMERCIAL ---
from .capitanes.gestion_comercial.capitan_marketing import CapitanMarketing
from .capitanes.gestion_comercial.capitan_publicidad_y_adquisicion_de_trafico_ads import CapitanPublicidadYAdquisicionDeTraficoADS
from .capitanes.gestion_comercial.capitan_gestion_operativa_de_contenidos_comerciales import CapitanGestionOperativaDeContenidosComerciales
from .capitanes.gestion_comercial.capitan_produccion_y_automatizacion_audiovisual import CapitanProduccionYAutomatizacionAudiovisual
from .capitanes.gestion_comercial.capitan_seo_turistico import CapitanSEOTuristico
from .capitanes.gestion_comercial.capitan_recomendaciones_sadi import CapitanRecomendacionesSADI
from .capitanes.gestion_comercial.capitan_alianzas_comerciales import CapitanAlianzasComerciales
from .capitanes.gestion_comercial.capitan_conversion import CapitanConversion
from .capitanes.gestion_comercial.capitan_embudos_conversion import CapitanEmbudosConversion
from .capitanes.gestion_comercial.capitan_implementacion_tecnica_de_embudos_y_crm import CapitanImplementacionTecnicaDeEmbudosYCRM
from .capitanes.gestion_comercial.capitan_pasarela_pagos import CapitanPasarelaPagos
from .capitanes.gestion_comercial.capitan_cotizaciones_dinamicas import CapitanCotizacionesDinamicas
from .capitanes.gestion_comercial.capitan_venta_conversacional import CapitanVentaConversacional
from .capitanes.gestion_comercial.capitan_contratacion import CapitanContratacion
from .capitanes.gestion_comercial.capitan_firma_digital import CapitanFirmaDigital
from .capitanes.gestion_comercial.capitan_kyc_verificacion import CapitanKYCVerificacion
from .capitanes.gestion_comercial.capitan_legalidad_y_privacidad import CapitanLegalidadYPrivacidad
from .capitanes.gestion_comercial.capitan_relacion_clientes import CapitanRelacionClientes
from .capitanes.gestion_comercial.capitan_mensajeria_y_envios_masivos import CapitanMensajeriaYEnviosMasivos
from .capitanes.gestion_comercial.capitan_fidelizacion_lealtad import CapitanFidelizacionLealtad
from .capitanes.gestion_comercial.capitan_soporte_viajero import CapitanSoporteViajero
from .capitanes.gestion_comercial.capitan_postventa_feedback import CapitanPostventaFeedback
from .capitanes.gestion_comercial.capitan_cumplimiento_comercial import CapitanCumplimientoComercial
from .capitanes.gestion_comercial.capitan_inteligencia_analitica_y_optimizacion import CapitanInteligenciaAnaliticaYOptimizacion
from .capitanes.gestion_comercial.capitan_auditoria_ventas import CapitanAuditoriaVentas
from .capitanes.gestion_comercial.capitan_prevencion_fraude import CapitanPrevencionFraude
from .capitanes.gestion_comercial.capitan_comercial_estrategico import CapitanComercialEstrategico
from .capitanes.gestion_comercial.capitan_gestion_comercial_general import CapitanGestionComercialGeneral
from .capitanes.gestion_comercial.capitan_comercial_hotelero import CapitanComercialHotelero
from .capitanes.gestion_comercial.capitan_comercial_gastronomico import CapitanComercialGastronomico
from .capitanes.gestion_comercial.capitan_comercial_turistico_tours import CapitanComercialTuristicoTours
from .capitanes.gestion_comercial.capitan_comercial_transporte import CapitanComercialTransporte

# --- OTROS DOMINIOS ---
from .capitanes.onboarding_prestador_capitan import CapitanOnboardingPrestador
from .capitanes.gestion_archivistica.capitan_archivistico import CapitanArchivistico
from .capitanes.gestion_archivistica.capitan_integridad_documental import CapitanIntegridadDocumental
from .capitanes.gestion_archivistica.capitan_retencion_normativa import CapitanRetencionNormativa
from .capitanes.gestion_archivistica.capitan_auditoria_documental import CapitanAuditoriaDocumental
from .capitanes.gestion_operativa.capitan_gestion_operativa_general import CapitanGestionOperativaGeneral
from .capitanes.gestion_operativa.capitan_control_operativo import CapitanControlOperativo
from .capitanes.gestion_operativa.capitan_incidentes_operativos import CapitanIncidentesOperativos
from .capitanes.gestion_operativa.capitan_calidad_y_cumplimiento import CapitanCalidadYCumplimiento
from .capitanes.gestion_contable.capitan_contabilidad_general import CapitanContabilidadGeneral
from .capitanes.gestion_contable.capitan_asientos_automaticos import CapitanAsientosAutomaticos
from .capitanes.gestion_contable.capitan_cierre_contable import CapitanCierreContable
from .capitanes.gestion_contable.capitan_auditoria_contable import CapitanAuditoriaContable
from .capitanes.gestion_financiera.capitan_base import CapitanFinancieraBase # Use base if specific missing
from .capitanes.gestion_financiera.capitan_gestion_financiera import CapitanGestionFinanciera
from .capitanes.gestion_financiera.capitan_flujo_caja import CapitanFlujoCaja
from .capitanes.gestion_financiera.capitan_riesgo_financiero import CapitanRiesgoFinanciero
from .capitanes.gestion_financiera.capitan_ratios_y_formulas_financieras import CapitanRatiosYFormulasFinancieras
from .capitanes.gestion_operativa.sg_sst.capitan_sst import CapitanSST
from .capitanes.gestion_operativa.sg_sst.capitan_incidentes_sst import CapitanIncidentesSST
from .capitanes.gestion_operativa.sg_sst.capitan_normativo_sst import CapitanNormativoSST
from .capitanes.gestion_contable.nomina.capitan_nomina import CapitanNomina
from .capitanes.gestion_contable.nomina.capitan_liquidacion_contratos import CapitanLiquidacionContratos
from .capitanes.gestion_contable.nomina.capitan_legal_laboral import CapitanLegalLaboral

class PrestadoresCoronel(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="prestadores")

    def _get_capitanes(self) -> dict:
        return {
            # Comercial
            "marketing": CapitanMarketing(coronel=self),
            "ads": CapitanPublicidadYAdquisicionDeTraficoADS(coronel=self),
            "contenidos": CapitanGestionOperativaDeContenidosComerciales(coronel=self),
            "audiovisual": CapitanProduccionYAutomatizacionAudiovisual(coronel=self),
            "seo": CapitanSEOTuristico(coronel=self),
            "sadi_matching": CapitanRecomendacionesSADI(coronel=self),
            "alianzas": CapitanAlianzasComerciales(coronel=self),
            "conversion": CapitanConversion(coronel=self),
            "embudos": CapitanEmbudosConversion(coronel=self),
            "crm_tech": CapitanImplementacionTecnicaDeEmbudosYCRM(coronel=self),
            "pagos": CapitanPasarelaPagos(coronel=self),
            "cotizaciones": CapitanCotizacionesDinamicas(coronel=self),
            "venta_conversacional": CapitanVentaConversacional(coronel=self),
            "contratacion": CapitanContratacion(coronel=self),
            "firma_digital": CapitanFirmaDigital(coronel=self),
            "kyc": CapitanKYCVerificacion(coronel=self),
            "legal_privacidad": CapitanLegalidadYPrivacidad(coronel=self),
            "crm_relacion": CapitanRelacionClientes(coronel=self),
            "mensajeria_masiva": CapitanMensajeriaYEnviosMasivos(coronel=self),
            "lealtad": CapitanFidelizacionLealtad(coronel=self),
            "soporte_viajero": CapitanSoporteViajero(coronel=self),
            "postventa": CapitanPostventaFeedback(coronel=self),
            "cumplimiento_comercial": CapitanCumplimientoComercial(coronel=self),
            "inteligencia_comercial": CapitanInteligenciaAnaliticaYOptimizacion(coronel=self),
            "auditoria_ventas": CapitanAuditoriaVentas(coronel=self),
            "prevencion_fraude": CapitanPrevencionFraude(coronel=self),
            "comercial_estrategico": CapitanComercialEstrategico(coronel=self),
            "comercial_general": CapitanGestionComercialGeneral(coronel=self),
            "comercial_hotel": CapitanComercialHotelero(coronel=self),
            "comercial_gastronomia": CapitanComercialGastronomico(coronel=self),
            "comercial_tours": CapitanComercialTuristicoTours(coronel=self),
            "comercial_transporte": CapitanComercialTransporte(coronel=self),

            # Otros
            "onboarding": CapitanOnboardingPrestador(coronel=self),
            "archivistico": CapitanArchivistico(coronel=self),
            "integridad_documental": CapitanIntegridadDocumental(coronel=self),
            "retencion_normativa": CapitanRetencionNormativa(coronel=self),
            "auditoria_documental": CapitanAuditoriaDocumental(coronel=self),
            "operativo_general": CapitanGestionOperativaGeneral(coronel=self),
            "seguimiento_operativo": CapitanControlOperativo(coronel=self),
            "incidentes_operativos": CapitanIncidentesOperativos(coronel=self),
            "cierre_operativo": CapitanCalidadYCumplimiento(coronel=self),
            "contabilidad_general": CapitanContabilidadGeneral(coronel=self),
            "asientos_automaticos": CapitanAsientosAutomaticos(coronel=self),
            "cierre_contable": CapitanCierreContable(coronel=self),
            "auditoria_contable": CapitanAuditoriaContable(coronel=self),
            "gestion_financiera": CapitanGestionFinanciera(coronel=self),
            "flujo_caja": CapitanFlujoCaja(coronel=self),
            "riesgo_financiero": CapitanRiesgoFinanciero(coronel=self),
            "indicadores_financieros": CapitanRatiosYFormulasFinancieras(coronel=self),
            "sst_general": CapitanSST(coronel=self),
            "sst_incidentes": CapitanIncidentesSST(coronel=self),
            "sst_normativo": CapitanNormativoSST(coronel=self),
            "nomina_general": CapitanNomina(coronel=self),
            "nomina_liquidacion": CapitanLiquidacionContratos(coronel=self),
            "nomina_legal": CapitanLegalLaboral(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        m_type = directiva.get("mission", {}).get("type")

        # Mapeo de tipos de misión a llaves del roster
        mapping = {
            "MARKETING_CAMP": "marketing",
            "ADS_CAMPAIGN": "ads",
            "SEO_AUDIT": "seo",
            "SADI_MATCH": "sadi_matching",
            "PROCESS_PAYMENT": "pagos",
            "GENERATE_QUOTE": "cotizaciones",
            "SALES_CHAT": "venta_conversacional",
            "SIGN_CONTRACT": "firma_digital",
            "KYC_CHECK": "kyc",
            "AUDIT_SALES": "auditoria_ventas",
            "FRAUD_CHECK": "prevencion_fraude",
            # ... (se pueden agregar todos los nuevos tipos aquí)
            "ONBOARDING_PRESTADOR": "onboarding",
            "CERRAR_CONTRATO": "contratacion",
            "VALIDAR_CUMPLIMIENTO_COMERCIAL": "cumplimiento_comercial",
            "AVANZAR_LEAD": "conversion",
            "ANALISIS_ESTRATEGICO_COMERCIAL": "comercial_estrategico",
        }

        cap_key = mapping.get(m_type)
        if cap_key:
            return self.capitanes.get(cap_key)

        # Fallback por prefijo si no hay match exacto
        if m_type and m_type.startswith("COMERCIAL_"):
            return self.capitanes.get("comercial_general")

        return None
