# backend/apps/sarita_agents/agents/general/sarita/coroneles/financiero/sargentos/sargento_flujo_real.py

from apps.sarita_agents.agents.sargento_template import SergeantTemplate
from ..soldados.soldados_financieros import (
    SoldadoRegistroIngresos, SoldadoRegistroEgresos,
    SoldadoVerificadorSoportes, SoldadoValidadorTransacciones,
    SoldadoConsolidadorDiario
)

class SargentoFlujoReal(SergeantTemplate):
    """
    NIVEL 5 — SARGENTO DE FLUJO REAL
    Supervisión de ingresos y egresos efectivos.
    """
    def _get_soldiers(self):
        return [
            SoldadoRegistroIngresos(sargento=self),
            SoldadoRegistroEgresos(sargento=self),
            SoldadoVerificadorSoportes(sargento=self),
            SoldadoValidadorTransacciones(sargento=self),
            SoldadoConsolidadorDiario(sargento=self),
        ]

    def plan_microtasks(self, params: dict):
        return [{"type": "CASH_FLOW_REAL", "provider_id": params.get("provider_id")} for _ in range(5)]
