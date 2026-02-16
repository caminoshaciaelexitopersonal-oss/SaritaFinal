import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from .models import (
    RawMaterial, ArtisanProduct, WorkshopOrder, ProductionLog, MaterialConsumption
)
from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService

logger = logging.getLogger(__name__)

class ArtisanService:
    """
    Motor de Gestión de Taller Artesanal (Fase 15)
    """
    def __init__(self, user):
        self.user = user
        self.provider = user.perfil_prestador

    @transaction.atomic
    def registrar_materia_prima(self, data):
        """
        Registra o actualiza stock de materia prima.
        """
        material, created = RawMaterial.objects.get_or_create(
            provider=self.provider,
            nombre=data['nombre'],
            defaults={
                'unidad_medida': data['unidad_medida'],
                'costo_por_unidad': Decimal(str(data['costo_por_unidad']))
            }
        )

        cantidad = Decimal(str(data['cantidad']))
        material.stock_actual += cantidad
        material.save()

        # Impacto ERP: Incremento de Inventario (Activo)
        erp_service = QuintupleERPService(user=self.user)
        erp_service.record_impact("RAW_MATERIAL_REGISTERED", {
            "material_id": str(material.id),
            "cantidad": float(cantidad),
            "costo_total": float(cantidad * material.costo_por_unidad)
        })

        return material

    @transaction.atomic
    def crear_orden_taller(self, data):
        """
        Crea una orden de trabajo para una pieza artesanal.
        """
        artisan_product = ArtisanProduct.objects.get(id=data['artisan_product_id'])

        order = WorkshopOrder.objects.create(
            provider=self.provider,
            cliente_ref_id=data['cliente_ref_id'],
            artisan_product=artisan_product,
            especificaciones=data.get('especificaciones', ''),
            fecha_entrega_prometida=data['fecha_entrega_prometida'],
            total_precio=Decimal(str(data['total_precio'])),
            anticipo_pagado=Decimal(str(data.get('anticipo_pagado', 0)))
        )

        ProductionLog.objects.create(
            order=order,
            etapa='DISENO',
            descripcion='Orden de taller iniciada.'
        )

        return order

    @transaction.atomic
    def actualizar_etapa_produccion(self, order_id, nueva_etapa, descripcion='', materiales=None):
        """
        Avanza la etapa de producción y descuenta materiales si aplica.
        """
        order = WorkshopOrder.objects.select_for_update().get(id=order_id, provider=self.provider)

        # Validar flujo lógico (opcional, pero recomendado)
        order.estado = nueva_etapa
        order.save()

        ProductionLog.objects.create(
            order=order,
            etapa=nueva_etapa,
            descripcion=descripcion
        )

        if materiales:
            for mat_data in materiales:
                self._consumir_material(order, mat_data)

        return order

    def _consumir_material(self, order, mat_data):
        material = RawMaterial.objects.select_for_update().get(id=mat_data['material_id'], provider=self.provider)
        cantidad = Decimal(str(mat_data['cantidad']))

        if material.stock_actual < cantidad:
            raise ValueError(f"Stock insuficiente de {material.nombre}. Disponible: {material.stock_actual}")

        material.stock_actual -= cantidad
        material.save()

        MaterialConsumption.objects.create(
            order=order,
            material=material,
            cantidad_usada=cantidad,
            costo_aplicado=material.costo_por_unidad * cantidad
        )

        # Impacto ERP: Registro de Costo de Producción
        erp_service = QuintupleERPService(user=self.user)
        erp_service.record_impact("ARTISAN_MATERIAL_CONSUMPTION", {
            "order_id": str(order.id),
            "material_id": str(material.id),
            "costo": float(material.costo_por_unidad * cantidad)
        })
