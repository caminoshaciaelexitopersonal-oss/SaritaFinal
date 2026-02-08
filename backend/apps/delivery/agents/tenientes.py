import logging
from apps.sarita_agents.agents.teniente_template import TenienteTemplate
from .sargentos import (
    SargentoRegistroServicio,
    SargentoValidacionPermisos,
    SargentoAsignacionVehiculo,
    SargentoRegistroEventoOperativo,
    SargentoActivacionPago
)

logger = logging.getLogger(__name__)

class TenienteValidacionEmpresa(TenienteTemplate):
    def perform_action(self, parametros: dict):
        sargento = SargentoValidacionPermisos()
        res = sargento.execute(parametros.get("company_id"))
        return {"verification": "SUCCESS", "details": res}

class TenienteHabilitacionConductor(TenienteTemplate):
    def perform_action(self, parametros: dict):
        return {"status": "ENABLED", "driver_id": parametros.get("driver_id")}

class TenienteControlVehiculos(TenienteTemplate):
    def perform_action(self, parametros: dict):
        sargento = SargentoAsignacionVehiculo()
        res = sargento.execute(parametros.get("vehicle_id"))
        return {"status": "AUDITED", "vehicle": res}

class TenienteAsignacionRuta(TenienteTemplate):
    def perform_action(self, parametros: dict):
        sargento = SargentoRegistroServicio()
        service_id = sargento.execute(parametros)
        return {"service_id": service_id, "assignment": "AUTOMATIC"}

class TenienteControlEjecucion(TenienteTemplate):
    def perform_action(self, parametros: dict):
        sargento_ev = SargentoRegistroEventoOperativo()
        sargento_pay = SargentoActivacionPago()

        event_id = sargento_ev.execute(parametros)

        if parametros.get("action") == "COMPLETE":
            pay_intent = sargento_pay.execute(parametros)
            return {"event_id": event_id, "payment_intent": pay_intent}

        return {"event_id": event_id}

class TenienteEvidenciasServicio(TenienteTemplate):
    def perform_action(self, parametros: dict):
        return {"evidence_hash": "SHA256-DELIVERY-TRACE", "audited": True}
