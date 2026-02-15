import logging
from .models import Reserva
logger = logging.getLogger(__name__)
class SargentoReservas:
    @staticmethod
    def confirmar_reserva(reserva_id):
        reserva = Reserva.objects.get(id=reserva_id)
        reserva.estado = 'CONFIRMADA'
        reserva.save()
        logger.info(f"SARGENTO: Reserva {reserva_id} confirmada.")
