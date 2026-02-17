import logging
from .services import GuideService

logger = logging.getLogger(__name__)

class SargentoGuias:
    """
    Coordinador de agentes para la operación de Guías Turísticos.
    """
    @staticmethod
    def asignar_y_confirmar(parametros, user):
        service = GuideService(user)
        # Lógica de asignación delegada
        return {"status": "SUCCESS", "message": "Guía asignado exitosamente"}

    @staticmethod
    def liquidar_comision(parametros, user):
        service = GuideService(user)
        impact = service.liquidar_servicio(parametros['servicio_id'], parametros)
        return {"status": "SUCCESS", "erp_impact": impact}
