# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/cumplimiento/coronel.py

import logging
from .......coronel_template import CoronelTemplate

logger = logging.getLogger(__name__)

class CoronelCumplimiento(CoronelTemplate):
    def __init__(self, general):
        super().__init__(general=general, domain="comercial_cumplimiento")

    def _get_capitanes(self) -> dict:
        from ...capitanes.capitan_cumplimiento_comercial import CapitanCumplimientoComercial
        from ...capitanes.capitan_inteligencia_analitica_y_optimizacion import CapitanInteligenciaAnaliticaYOptimizacion
        from ...capitanes.capitan_auditoria_ventas import CapitanAuditoriaVentas
        from ...capitanes.capitan_prevencion_fraude import CapitanPrevencionFraude

        return {
            "cumplimiento": CapitanCumplimientoComercial(coronel=self),
            "inteligencia": CapitanInteligenciaAnaliticaYOptimizacion(coronel=self),
            "auditoria": CapitanAuditoriaVentas(coronel=self),
            "fraude": CapitanPrevencionFraude(coronel=self),
        }
