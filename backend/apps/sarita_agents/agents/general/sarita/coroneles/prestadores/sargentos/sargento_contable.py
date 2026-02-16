# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/sargentos/sargento_contable.py

from apps.sarita_agents.agents.sargento_template import SergeantTemplate
from ..soldados.soldados_contables import (
    SoldadoRegistroContable, SoldadoVerificacionContable,
    SoldadoTrazabilidadContable, SoldadoIntegraciónContable,
    SoldadoMonitoreoContable
)
import logging

logger = logging.getLogger(__name__)

class SargentoRegistroContable(SergeantTemplate):
    def _get_soldiers(self):
        return [
            SoldadoRegistroContable(sargento=self),
            SoldadoVerificacionContable(sargento=self),
            SoldadoTrazabilidadContable(sargento=self),
            SoldadoIntegraciónContable(sargento=self),
            SoldadoMonitoreoContable(sargento=self),
        ]

    def plan_microtasks(self, params: dict):
        # Divide el trabajo en 5 microtareas según el tipo de soldado
        return [
            {"comprobante_id": params.get("comprobante_id"), "type": "REGISTRO"},
            {"asiento_id": params.get("asiento_id"), "type": "VERIFICACION"},
            {"uuid": params.get("operacion_id"), "type": "TRAZABILIDAD"},
            {"tx_id": params.get("tx_id"), "type": "INTEGRACION"},
            {"metric": "performance", "type": "MONITOREO"}
        ]
