import logging
from decimal import Decimal
from .services import ArtisanService
from .models import WorkshopOrder, RawMaterial

logger = logging.getLogger(__name__)

class SargentoArtesano:
    """
    Ejecutor de acciones atómicas para el dominio de Artesanos.
    """

    @staticmethod
    def registrar_entrada_inventario(params, user):
        provider = user.perfil_prestador
        nombre = params.get("nombre")
        cantidad = params.get("cantidad")
        unidad = params.get("unidad", "unidades")

        material, created = RawMaterial.objects.get_or_create(
            provider=provider,
            nombre=nombre,
            defaults={"unidad_medida": unidad}
        )
        material.stock_actual += Decimal(str(cantidad))
        material.save()

        logger.info(f"SARGENTO ARTESANO: Entrada de {cantidad} {unidad} de {nombre}")
        return {"status": "SUCCESS", "material_id": str(material.id), "nuevo_stock": float(material.stock_actual)}

    @staticmethod
    def actualizar_produccion(params, user):
        order_id = params.get("order_id")
        material_id = params.get("material_id")
        cantidad = params.get("cantidad")
        descripcion = params.get("descripcion", "Avance de producción")

        try:
            log = ArtisanService.registrar_produccion(order_id, material_id, cantidad, descripcion)
            return {"status": "SUCCESS", "log_id": str(log.id)}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}
