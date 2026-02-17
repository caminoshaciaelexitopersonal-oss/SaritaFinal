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

        if "servicio_id" in parametros:
            # Re-asignación o actualización
            servicio = service.actualizar_estado_servicio(
                parametros['servicio_id'],
                parametros.get('nuevo_estado', 'CONFIRMADO')
            )
            return {"status": "SUCCESS", "servicio_id": str(servicio.id)}
        else:
            # Nueva programación
            servicio = service.programar_servicio(parametros)
            return {"status": "SUCCESS", "servicio_id": str(servicio.id)}

    @staticmethod
    def liquidar_comision(parametros, user):
        service = GuideService(user)
        impact = service.liquidar_servicio(parametros['servicio_id'], parametros)
        return {"status": "SUCCESS", "erp_impact": impact}
