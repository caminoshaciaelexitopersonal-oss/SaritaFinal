# backend/apps/prestadores/mi_negocio/gestion_comercial/services.py
from django.db import transaction
from django.utils import timezone

from .domain.models import OperacionComercial, FacturaVenta, ItemFactura
from apps.prestadores.mi_negocio.gestion_contable.services.facturacion import FacturaVentaAccountingService
from .dian_services import DianService

class FacturacionService:
    @staticmethod
    @transaction.atomic
    def facturar_operacion_confirmada(operacion: OperacionComercial):
        """
        Orquesta el proceso completo de facturación para una operación confirmada.
        """
        # 1. Crear la FacturaVenta interna a partir de la OperacionComercial
        factura = FacturaVenta.objects.create(
            operacion=operacion,
            perfil=operacion.perfil,
            cliente=operacion.cliente,
            numero_factura=f"FV-{operacion.id}", # Lógica de numeración simple
            fecha_emision=timezone.now().date(),
            subtotal=operacion.subtotal,
            impuestos=operacion.impuestos,
            total=operacion.total,
            creado_por=operacion.creado_por,
            estado=FacturaVenta.Estado.EMITIDA
        )
        for item_op in operacion.items.all():
            ItemFactura.objects.create(
                factura=factura,
                producto=item_op.producto,
                descripcion=item_op.descripcion,
                cantidad=item_op.cantidad,
                precio_unitario=item_op.precio_unitario
            )

        # 2. Registrar el asiento contable
        FacturaVentaAccountingService.registrar_factura_venta(factura)

        # 3. Enviar a la DIAN (simulado) y actualizar estado
        dian_response = DianService.enviar_factura(factura)
        if dian_response["success"]:
            factura.estado_dian = FacturaVenta.EstadoDIAN.ACEPTADA
            factura.cufe = dian_response["cufe"]
        else:
            factura.estado_dian = FacturaVenta.EstadoDIAN.RECHAZADA
        factura.dian_response_log = dian_response
        factura.save()

        # 4. Actualizar estado de la operación original
        operacion.estado = OperacionComercial.Estado.FACTURADA
        operacion.save()

        return factura
