# backend/apps/sarita_agents/agents/general/sarita/coroneles/contable/sargentos/sargento_asientos.py

from apps.sarita_agents.agents.sargento_template import SergeantTemplate
from ..soldados.soldados_contables import (
    SoldadoRegistroIngreso, SoldadoRegistroGasto,
    SoldadoConciliacionWallet, SoldadoVerificacionFiscal,
    SoldadoCierreParcial
)
import logging

logger = logging.getLogger(__name__)

class SargentoAsientosContables(SergeantTemplate):
    """
    NIVEL 5 — SARGENTO DE ASIENTOS
    Coordinador operativo. Divide el trabajo contable entre sus 5 soldados.
    """
    def _get_soldiers(self):
        return [
            SoldadoRegistroIngreso(sargento=self),
            SoldadoRegistroGasto(sargento=self),
            SoldadoConciliacionWallet(sargento=self),
            SoldadoVerificacionFiscal(sargento=self),
            SoldadoCierreParcial(sargento=self),
        ]

    def plan_microtasks(self, params: dict):
        # Pasar parámetros de persistencia a los soldados si existen
        common = {
            "periodo_id": params.get("periodo_id"),
            "fecha": params.get("fecha"),
            "usuario_id": params.get("usuario_id"),
            "movimientos": params.get("movimientos")
        }

        return [
            {**common, "monto": params.get("monto_ingreso", 0), "type": "INGRESO"},
            {**common, "monto": params.get("monto_gasto", 0), "type": "GASTO"},
            {"type": "CONCILIACION_WALLET"},
            {"type": "FISCAL"},
            {"periodo": params.get("periodo", "actual"), "type": "CIERRE"}
        ]
