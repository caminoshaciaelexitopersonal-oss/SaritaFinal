# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/coronel.py

from .....coronel_template import CoronelTemplate
# Importar los capitanes específicos de este dominio.
 
from .capitanes.onboarding_prestador_capitan import CapitanOnboardingPrestador
from .capitanes.gestion_comercial.capitan_contratacion import CapitanContratacion
from .capitanes.gestion_comercial.capitan_cumplimiento_comercial import CapitanCumplimientoComercial
from .capitanes.gestion_comercial.capitan_conversion import CapitanConversion
from .capitanes.gestion_comercial.capitan_comercial_estrategico import CapitanComercialEstrategico
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
    """
    Coronel para el dominio de Prestadores.
    Gestiona todas las misiones relacionadas con proveedores de servicios.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="prestadores")

    def _get_capitanes(self) -> dict:
        """
        Carga y devuelve el roster de Capitanes bajo el mando de este Coronel.
        """
        return {
            "onboarding": CapitanOnboardingPrestador(coronel=self),
            "contratacion": CapitanContratacion(coronel=self),
            "cumplimiento_comercial": CapitanCumplimientoComercial(coronel=self),
            "conversion": CapitanConversion(coronel=self),
            "comercial_estrategico": CapitanComercialEstrategico(coronel=self),
            "archivistico": CapitanArchivistico(coronel=self),
            "integridad_documental": CapitanIntegridadDocumental(coronel=self),
            "retencion_normativa": CapitanRetencionNormativa(coronel=self),
            "auditoria_documental": CapitanAuditoriaDocumental(coronel=self),
            "operativo_general": CapitanGestionOperativaGeneral(coronel=self),
            "seguimiento_operativo": CapitanControlOperativo(coronel=self),
            "incidentes_operativos": CapitanIncidentesOperativos(coronel=self),
            "cierre_operativo": CapitanCalidadYCumplimiento(coronel=self),
            "operacion_hotelera": CapitanOperacionHotelera(coronel=self),
            "operacion_restaurante": CapitanOperacionRestaurantes(coronel=self),
            "operacion_transporte": CapitanOperacionTransporte(coronel=self),
            "operacion_tours": CapitanOperacionTours(coronel=self),
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
        """
        Lógica para seleccionar el Capitán más adecuado para la misión.
        Para la Fase U, asumimos que cualquier misión de 'prestadores' es para onboarding.
        """
        mission_info = directiva.get("mission", {})
        mission_type = mission_info.get("type")

        if mission_type == "ONBOARDING_PRESTADOR":
            return self.capitanes.get("onboarding")
        elif mission_type == "CERRAR_CONTRATO":
            return self.capitanes.get("contratacion")
        elif mission_type == "VALIDAR_CUMPLIMIENTO_COMERCIAL":
            return self.capitanes.get("cumplimiento_comercial")
        elif mission_type == "AVANZAR_LEAD":
            return self.capitanes.get("conversion")
        elif mission_type == "ANALISIS_ESTRATEGICO_COMERCIAL":
            return self.capitanes.get("comercial_estrategico")
        elif mission_type == "GESTIONAR_ARCHIVO":
            return self.capitanes.get("archivistico")
        elif mission_type == "VERIFICAR_INTEGRIDAD":
            return self.capitanes.get("integridad_documental")
        elif mission_type == "APLICAR_RETENCION":
            return self.capitanes.get("retencion_normativa")
        elif mission_type == "AUDITAR_DOCUMENTOS":
            return self.capitanes.get("auditoria_documental")
        elif mission_type == "EJECUTAR_SERVICIO":
            return self.capitanes.get("operativo_general")
        elif mission_type == "MONITOREAR_OPERACION":
            return self.capitanes.get("seguimiento_operativo")
        elif mission_type == "REPORTAR_FALLA":
            return self.capitanes.get("incidentes_operativos")
        elif mission_type == "CERRAR_SERVICIO":
            return self.capitanes.get("cierre_operativo")
        elif mission_type == "REGISTRAR_CONTABILIDAD":
            return self.capitanes.get("contabilidad_general")
        elif mission_type == "GENERAR_ASIENTO":
            return self.capitanes.get("asientos_automaticos")
        elif mission_type == "EJECUTAR_CIERRE":
            return self.capitanes.get("cierre_contable")
        elif mission_type == "AUDITAR_CONTABILIDAD":
            return self.capitanes.get("auditoria_contable")
        elif mission_type == "GESTIONAR_FINANZAS":
            return self.capitanes.get("gestion_financiera")
        elif mission_type == "ANALIZAR_LIQUIDEZ":
            return self.capitanes.get("flujo_caja")
        elif mission_type == "EVALUAR_RIESGO_FINANCIERO":
            return self.capitanes.get("riesgo_financiero")
        elif mission_type == "CALCULAR_RATIOS":
            return self.capitanes.get("indicadores_financieros")
        elif mission_type == "GESTIONAR_SST":
            return self.capitanes.get("sst_general")
        elif mission_type == "REPORTAR_INCIDENTE_SST":
            return self.capitanes.get("sst_incidentes")
        elif mission_type == "AUDITAR_SST":
            return self.capitanes.get("sst_normativo")
        elif mission_type == "GESTIONAR_NOMINA":
            return self.capitanes.get("nomina_general")
        elif mission_type == "LIQUIDAR_CONTRATO":
            return self.capitanes.get("nomina_liquidacion")
        elif mission_type == "AUDITAR_LABORAL":
            return self.capitanes.get("nomina_legal")
        elif mission_type == "GESTIONAR_HOTEL":
            return self.capitanes.get("operacion_hotelera")
        elif mission_type == "GESTIONAR_RESTAURANTE":
            return self.capitanes.get("operacion_restaurante")
        elif mission_type == "GESTIONAR_TRANSPORTE":
            return self.capitanes.get("operacion_transporte")
        elif mission_type == "GESTIONAR_TOUR":
            return self.capitanes.get("operacion_tours")

        return None # No se encontró capitán para esta misión 
 
