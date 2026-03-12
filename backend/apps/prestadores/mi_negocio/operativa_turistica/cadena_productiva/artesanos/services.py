import logging
from decimal import Decimal
from django.db import transaction
from .models import RawMaterial, WorkshopOrder, ProductionLog

logger = logging.getLogger(__name__)

class ArtisanService:
    @staticmethod
    @transaction.atomic
    def registrar_produccion(order_id, material_id, cantidad, descripcion):
        """
        Registra un avance de producción y deduce automáticamente del inventario.
        """
        try:
            order = WorkshopOrder.objects.get(id=order_id)
            material = RawMaterial.objects.get(id=material_id)

            if material.stock_actual < Decimal(str(cantidad)):
                raise ValueError(f"Stock insuficiente de {material.nombre}")

            # Crear log de producción
            log = ProductionLog.objects.create(
                provider=order.provider,
                order=order,
                material=material,
                cantidad_consumida=Decimal(str(cantidad)),
                descripcion_avance=descripcion
            )

            # Deducir inventario
            material.stock_actual -= Decimal(str(cantidad))
            material.save()

            logger.info(f"Producción registrada para {order.producto_nombre}. Consumo: {cantidad} de {material.nombre}")
            return log
        except Exception as e:
            logger.error(f"Error al registrar producción: {e}")
            raise e

    @staticmethod
    def crear_orden_taller(provider, data):
        """
        Crea una nueva orden de trabajo en el taller.
        """
        return WorkshopOrder.objects.create(
            provider=provider,
            producto_nombre=data.get('producto_nombre'),
            cantidad=data.get('cantidad', 1),
            fecha_entrega_estimada=data.get('fecha_entrega_estimada'),
            cliente_nombre=data.get('cliente_nombre', '')
        )
