# backend/apps/prestadores/mi_negocio/gestion_comercial/services.py
import logging
from django.db import transaction
from django.utils import timezone
import json

from .domain.models import OperacionComercial, FacturaVenta, ItemFactura
from apps.prestadores.mi_negocio.gestion_contable.services.facturacion import FacturaVentaAccountingService
from apps.prestadores.mi_negocio.gestion_archivistica.archiving import ArchivingService
from .dian_services import DianService
# --- IMPORTACIÓN DE SERVICIOS DE DOMINIO OPERATIVO ---
from apps.prestadores.mi_negocio.gestion_operativa.services import (
    ProviderProfileService,
    ClienteService,
    ProductoService,
)

# Configurar un logger para este módulo
logger = logging.getLogger(__name__)

class FacturacionService:
    @staticmethod
    @transaction.atomic
    def facturar_operacion_confirmada(operacion: OperacionComercial):
        """
        Orquesta el proceso completo de facturación para una operación confirmada.
        AHORA UTILIZA SERVICIOS DE DOMINIO PARA RESOLVER REFERENCIAS.
        """
        # --- RESOLUCIÓN DE DEPENDENCIAS VÍA SERVICIOS DE DOMINIO ---
        perfil = ProviderProfileService.get_profile_by_id(operacion.perfil_ref_id)
        cliente = ClienteService.get_cliente_by_id(operacion.cliente_ref_id)

        if not perfil or not cliente:
            # Manejo de error si las referencias no se pueden resolver
            logger.error(f"No se pudo resolver el perfil ({operacion.perfil_ref_id}) o el cliente ({operacion.cliente_ref_id}) para la operación {operacion.id}")
            # En un caso real, aquí se lanzaría una excepción para abortar la transacción
            raise ValueError("Referencias de perfil o cliente no válidas.")

        # 1. Crear la FacturaVenta interna
        factura = FacturaVenta.objects.create(
            operacion=operacion,
            perfil_ref_id=operacion.perfil_ref_id,
            cliente_ref_id=operacion.cliente_ref_id,
            numero_factura=f"FV-{operacion.id}",
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
                producto_ref_id=item_op.producto_ref_id,
                descripcion=item_op.descripcion,
                cantidad=item_op.cantidad,
                precio_unitario=item_op.precio_unitario,
            )

        # 2. Registrar el asiento contable
        # Nota: El servicio de contabilidad también deberá ser refactorizado para
        # resolver las referencias por ID en lugar de esperar objetos.
        # Por ahora, se asume que esta adaptación es parte de la FASE 14.5.
        FacturaVentaAccountingService.registrar_factura_venta(factura, cliente=cliente, perfil=perfil)

        # 3. Enviar a la DIAN (simulado)
        dian_response = DianService.enviar_factura(factura, cliente=cliente)
        if dian_response["success"]:
            factura.estado_dian = FacturaVenta.EstadoDIAN.ACEPTADA
            factura.cufe = dian_response["cufe"]
        else:
            factura.estado_dian = FacturaVenta.EstadoDIAN.RECHAZADA
        factura.dian_response_log = dian_response

        # --- INICIO DE INTEGRACIÓN CON SGA ---
        # 4. Archivar el documento de la factura
        try:
            # Preparar contenido y metadatos para el SGA
            factura_content = {
                "numero_factura": factura.numero_factura,
                "cliente": cliente.nombre, # Usar el objeto resuelto
                "total": str(factura.total),
                "cufe": factura.cufe
            }
            factura_bytes = json.dumps(factura_content, indent=2).encode('utf-8')

            metadata = {'source_model': 'FacturaVenta', 'source_id': factura.id}

            # Invocar al servicio de archivado
            # Nota: factura.perfil.company.id es un anti-patrón.
            # El company_id debería obtenerse del perfil resuelto.
            document_version = ArchivingService.archive_document(
                company_id=perfil.company_id, # Usar el ID de referencia
                user_id=factura.creado_por.id,
                process_type_code='CONT',
                process_code='FACT',
                document_type_code='FV',
                document_content=factura_bytes,
                original_filename=f"{factura.numero_factura}.json",
                document_metadata=metadata,
                requires_blockchain_notarization=True
            )

            # Vincular el registro de archivo con la factura
            factura.documento_archivistico = document_version.document
        except Exception as e:
            # Usar logging estructurado en lugar de print
            logger.error(
                "Error al archivar la factura %s: %s",
                factura.numero_factura,
                e,
                exc_info=True  # Adjuntar traceback al log
            )
        # --- FIN DE INTEGRACIÓN CON SGA ---

        factura.save()

        # 5. Actualizar estado de la operación original
        operacion.estado = OperacionComercial.Estado.FACTURADA
        operacion.save()

        return factura
