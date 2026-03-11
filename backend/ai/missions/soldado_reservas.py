import logging
from application.services.reservation_service import ReservationService

logger = logging.getLogger(__name__)

class ReservationSoldier:
    """NIVEL 6 - SOLDADO DE RESERVAS (Consolidado)"""
    async def execute(self, mission_data):
        data = mission_data.get("data", {})
        logger.info(f"Soldado Reservas: Procesando para {data.get('usuario')}")

        try:
            # Orquestación vía Application Service (Decoupled)
            is_available = await ReservationService.check_availability(
                data.get("destino"),
                data.get("fecha")
            )

            if not is_available:
                return {"status": "failed", "reason": "No availability"}

            reservation = await ReservationService.create_reservation(data)
            return {"status": "success", "reservation_id": reservation.id}
        except Exception as e:
            logger.error(f"Error en misión: {e}")
            return {"status": "error", "message": str(e)}
