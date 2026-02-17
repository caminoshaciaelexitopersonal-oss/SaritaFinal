# backend/apps/prestadores/mi_negocio/gestion_comercial/services.py
import logging
from django.db import transaction
from django.utils import timezone
import json

from .domain.models import OperacionComercial, FacturaVenta, ItemFactura
from apps.audit.models import AuditLog
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
    def procesar_intencion_venta(perfil_id, cliente_id, items_data, usuario):
        """
        Punto de entrada para el flujo comercial gobernado por agentes.
        1. Registra Intención.
        2. Crea Operación Comercial (Borrador).
        3. Delega a Agentes la validación y creación de contrato.
        """
        perfil = ProviderProfileService.get_profile_by_id(perfil_id)
        # 1. Crear Operación Comercial
        operacion = OperacionComercial.objects.create(
            provider=perfil,
            perfil_ref_id=perfil_id,
            cliente_ref_id=cliente_id,
            creado_por=usuario,
            estado=OperacionComercial.Estado.BORRADOR
        )
        total_subtotal = 0
        for item in items_data:
            producto_id = item['producto']
            cantidad = item['cantidad']
            precio = item['precio_unitario']
            subtotal = Decimal(cantidad) * Decimal(precio)
            total_subtotal += subtotal
            ItemOperacionComercial.objects.create(
                operacion=operacion,
                producto_ref_id=producto_id,
                descripcion=f"Producto {producto_id}", # Idealmente traer de ProductoService
                cantidad=cantidad,
                precio_unitario=precio,
                subtotal=subtotal
            )
        operacion.subtotal = total_subtotal
        operacion.total = total_subtotal # Sin impuestos por ahora
        operacion.save()

        # 2. Registrar Auditoría de Intención
        AuditLog.objects.create(
            user=usuario,
            username=usuario.username,
            action="SALE_INTENT_DETECTED",
            details={"operacion_id": str(operacion.id), "total": str(operacion.total)}
        )

        # 3. Delegar a Agente de Contratación
        from apps.sarita_agents.orchestrator import sarita_orchestrator
        directive = {
            "domain": "prestadores",
            "mission": {"type": "SIGN_CONTRACT"},
            "parameters": {"operacion_id": str(operacion.id)}
        }
        sarita_orchestrator.handle_directive(directive)

        return operacion

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
            provider=perfil,
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

        # 2. Registrar el reflejo contable vía Agentes (Fase 5)
        try:
            from apps.sarita_agents.orchestrator import sarita_orchestrator

            # TODO: Obtener el periodo contable activo real
            from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import PeriodoContable, Cuenta
            periodo = PeriodoContable.objects.filter(provider_id=operacion.perfil_ref_id, cerrado=False).first()

            if periodo:
                # Buscar cuentas base para el asiento (simplificado)
                cuenta_cxc = Cuenta.objects.filter(plan_de_cuentas__provider_id=operacion.perfil_ref_id, codigo='1305').first()
                cuenta_ingreso = Cuenta.objects.filter(plan_de_cuentas__provider_id=operacion.perfil_ref_id, codigo='4135').first()

                if cuenta_cxc and cuenta_ingreso:
                    movimientos = [
                        {"cuenta_id": str(cuenta_cxc.id), "debito": float(factura.total), "descripcion": "CxC Cliente"},
                        {"cuenta_id": str(cuenta_ingreso.id), "credito": float(factura.total), "descripcion": "Venta de servicios"}
                    ]

                    directive_acc = {
                        "domain": "contabilidad",
                        "mission": {"type": "RECOGNIZE_REVENUE"},
                        "parameters": {
                            "periodo_id": str(periodo.id),
                            "fecha": str(factura.fecha_emision),
                            "descripcion": f"Factura {factura.numero_factura}",
                            "movimientos": movimientos,
                            "usuario_id": factura.creado_por.id
                        }
                    }
                    sarita_orchestrator.handle_directive(directive_acc)
                    logger.info(f"GESTIÓN COMERCIAL: Misión de registro contable delegada para factura {factura.numero_factura}")
        except Exception as e:
            logger.error(f"Error al delegar reflejo contable de factura {factura.numero_factura}: {e}")

        # 3. Enviar a la DIAN (simulado)
        dian_response = DianService.enviar_factura(factura, cliente=cliente)
        if dian_response["success"]:
            factura.estado_dian = FacturaVenta.EstadoDIAN.ACEPTADA
            factura.cufe = dian_response["cufe"]
        else:
            factura.estado_dian = FacturaVenta.EstadoDIAN.RECHAZADA
        factura.dian_response_log = dian_response

        # --- INTEGRACIÓN CON SGA VÍA AGENTES ---
        try:
            from apps.sarita_agents.orchestrator import sarita_orchestrator

            factura_content = {
                "numero_factura": factura.numero_factura,
                "cliente": cliente.nombre,
                "total": str(factura.total),
                "cufe": factura.cufe
            }

            directive = {
                "domain": "prestadores",
                "mission": {"type": "ARCHIVE_ACCOUNTING_DOC"},
                "parameters": {
                    "company_id": perfil.company_id,
                    "user_id": factura.creado_por.id,
                    "process_type_code": 'CONT',
                    "process_code": 'FACT',
                    "document_type_code": 'FV',
                    "document_content": json.dumps(factura_content).encode('utf-8'),
                    "original_filename": f"{factura.numero_factura}.json",
                    "document_metadata": {'source_model': 'FacturaVenta', 'source_id': str(factura.id)},
                }
            }
            sarita_orchestrator.handle_directive(directive)
            logger.info(f"GESTIÓN COMERCIAL: Misión de archivado delegada para factura {factura.numero_factura}")

        except Exception as e:
            logger.error(f"Error al delegar archivado de factura {factura.numero_factura}: {e}")

        factura.save()

        # 4.5 Registrar en el Log de Auditoría
        AuditLog.objects.create(
            user=factura.creado_por,
            username=factura.creado_por.username,
            company_id=perfil.company_id,
            action=AuditLog.Action.INVOICE_GENERATED,
            details={
                "factura_id": str(factura.id),
                "numero_factura": factura.numero_factura,
                "total": str(factura.total),
                "operacion_id": str(operacion.id)
            }
        )

        # 5. Actualizar estado de la operación original
        operacion.estado = OperacionComercial.Estado.FACTURADA
        operacion.save()

        return factura
