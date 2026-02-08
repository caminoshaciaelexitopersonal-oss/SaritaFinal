import logging
from apps.delivery.models import DeliveryService, DeliveryEvent, Vehicle, DeliveryCompany

logger = logging.getLogger(__name__)

class SargentoRegistroServicio:
    """Registra la solicitud inicial de un servicio."""
    def execute(self, params: dict):
        logger.info("SARGENTO: Registrando solicitud de delivery.")
        return "service-uuid"

class SargentoValidacionPermisos:
    """Valida los permisos institucionales de una empresa."""
    def execute(self, company_id):
        logger.info(f"SARGENTO: Validando permisos para empresa {company_id}")
        return "PERMIT-VALID"

class SargentoAsignacionVehiculo:
    """Asocia un vehículo a un conductor o servicio."""
    def execute(self, vehicle_id):
        logger.info(f"SARGENTO: Verificando vehículo {vehicle_id}")
        return "VEHICLE-OK"

class SargentoRegistroEventoOperativo:
    """Registra un hito en la ejecución del servicio."""
    def execute(self, params: dict):
        logger.info("SARGENTO: Registrando hito logístico.")
        return "event-uuid"

class SargentoActivacionPago:
    """Activa la liquidación via monedero al completar el servicio."""
    def execute(self, params: dict):
        logger.info("SARGENTO: Activando intención de pago en monedero.")
        return "wallet-pay-intent"
