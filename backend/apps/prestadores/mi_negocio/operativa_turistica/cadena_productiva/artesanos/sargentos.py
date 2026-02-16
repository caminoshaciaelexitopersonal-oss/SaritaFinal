import logging
from .services import ArtisanService

logger = logging.getLogger(__name__)

class SargentoArtesano:
    """
    Coordinador de agentes para la operación de Artesanos y Talleres.
    """
    @staticmethod
    def registrar_suministros(parametros, user):
        service = ArtisanService(user)
        material = service.registrar_materia_prima(parametros)
        return {"status": "SUCCESS", "material_id": str(material.id), "stock": float(material.stock_actual)}

    @staticmethod
    def iniciar_pedido_artesanal(parametros, user):
        service = ArtisanService(user)
        order = service.crear_orden_taller(parametros)
        return {"status": "SUCCESS", "order_id": str(order.id)}

    @staticmethod
    def avanzar_produccion(parametros, user):
        service = ArtisanService(user)
        order = service.actualizar_etapa_produccion(
            parametros['order_id'],
            parametros['nueva_etapa'],
            parametros.get('descripcion', ''),
            parametros.get('materiales')
        )
        return {"status": "SUCCESS", "order_id": str(order.id), "estado": order.estado}
