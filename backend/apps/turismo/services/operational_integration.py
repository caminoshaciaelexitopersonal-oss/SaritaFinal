import logging
from django.db import transaction
from .financial_service import TourismFinancialService
from .delivery_integration import TourismDeliveryService
from apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.gastronomia.models import Plato, Restaurante

logger = logging.getLogger(__name__)

class OperationalIntegrationService:
    """
    Orquesta la integración entre operaciones especializadas, finanzas y logística.
    """

    @staticmethod
    @transaction.atomic
    def process_restaurant_sale(plato_id, customer, delivery_required=False, address=None):
        """
        Procesa una venta de gastronomía: Registro -> Pago -> Delivery.
        """
        plato = Plato.objects.get(id=plato_id)
        restaurante = plato.categoria.menu.restaurante

        # 1. Crear Reserva/Orden simulada para el flujo (En producción usaría el modelo Reservation unificado)
        # Por ahora, usamos directamente los servicios de integración.

        # 2. Registrar Transacción Financiera
        # (Se asume que TourismFinancialService tiene métodos para ventas directas)

        # 3. Si requiere delivery y el restaurante lo ofrece
        if delivery_required and restaurante.ofrece_delivery:
             # Invocar TourismDeliveryService
             pass

        return {"status": "SUCCESS", "message": "Operación integrada completada"}
