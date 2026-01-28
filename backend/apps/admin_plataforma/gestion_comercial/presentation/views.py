import logging
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin

logger = logging.getLogger(__name__)
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal

from rest_framework import serializers
from ..domain.models import FacturaVenta, ReciboCaja
from .serializers import (
    FacturaVentaListSerializer,
    FacturaVentaDetailSerializer,
    FacturaVentaWriteSerializer,
    ReciboCajaSerializer
)
from apps.prestadores.mi_negocio.gestion_financiera.models import TransaccionBancaria
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction as ContabTransaction, ChartOfAccount
from apps.prestadores.mi_negocio.gestion_contable.inventario.models import MovimientoInventario, Almacen

class FacturaVentaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_serializer_class(self):
        if self.action == 'list':
            return FacturaVentaListSerializer
        if self.action == 'retrieve':
            return FacturaVentaDetailSerializer
        return FacturaVentaWriteSerializer

    def get_queryset(self):
        return super().get_queryset().select_related('cliente')

    def perform_create(self, serializer):
        perfil = self.request.user.perfil_prestador
        log_context = {
            "user_id": self.request.user.id,
            "profile_id": perfil.id,
            "action": "CREATE_INVOICE",
        }

        try:
            with transaction.atomic():
                # Primero, intenta obtener las cuentas para fallar rápido si no existen.
                try:
                    cuenta_ingresos = ChartOfAccount.objects.get(perfil=perfil, code='4135')
                    cuenta_cxc = ChartOfAccount.objects.get(perfil=perfil, code='1305')
                except ChartOfAccount.DoesNotExist:
                    logger.error(
                        f"[FACTURACION] Error al crear factura: Cuentas contables no encontradas. Perfil={perfil.id}"
                    )
                    raise serializers.ValidationError({
                        "error": "CONFIGURACION_CONTABLE_INCOMPLETA",
                        "detalle": "No se encontraron las cuentas contables requeridas para registrar la venta (Ingresos '4135' o Cuentas por Cobrar '1305'). Asegúrese de que el plan de cuentas esté configurado."
                    })

                factura = serializer.save(perfil=perfil, creado_por=self.request.user)
                log_context['invoice_id'] = factura.id

                # --- Creación del Asiento Contable de la Venta ---
                journal_entry = JournalEntry.objects.create(
                    perfil=perfil,
                    entry_date=factura.fecha_emision,
                description=f"Venta según Factura No. {factura.numero_factura}",
                entry_type="VENTA",
                user=self.request.user,
                origin_document=factura
            )

            # Débito a Cuentas por Cobrar
            ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_cxc, debit=factura.total, credit=Decimal('0.00'))
            # Crédito a Ingresos
            ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_ingresos, debit=Decimal('0.00'), credit=factura.total)

            # --- Creación de Movimientos de Inventario ---
            # try:
            #     # Asumimos un almacén principal. En un sistema real, esto sería seleccionable.
            #     almacen_principal = Almacen.objects.get(perfil=perfil, nombre__icontains='principal')
            #     for item in factura.items.all():
            #         MovimientoInventario.objects.create(
            #             producto=item.producto,
            #             almacen=almacen_principal,
            #             tipo_movimiento=MovimientoInventario.TipoMovimiento.SALIDA,
            #             cantidad=item.cantidad,
            #             descripcion=f"Venta según Factura No. {factura.numero_factura}",
            #             usuario=self.request.user
            #         )
            # except Almacen.DoesNotExist:
            #     raise serializers.ValidationError(
            #         "No se encontró un 'Almacén Principal' para registrar la salida de inventario."
            #     )

            logger.info("Creación de factura exitosa.", extra=log_context)

        except serializers.ValidationError as e:
            # Errores de validación de negocio (ej. cuentas no encontradas)
            log_context['error'] = str(e.detail)
            logger.warning("Fallo en la creación de factura (Validación).", extra=log_context)
            # Re-lanza la excepción para que DRF la maneje y devuelva un 400.
            raise
        except Exception as e:
            # Errores inesperados del sistema
            log_context['error'] = str(e)
            logger.error("Fallo crítico en la creación de factura (Excepción).", extra=log_context)
            # Re-lanza la excepción para que DRF devuelva un 500.
            raise

    def perform_update(self, serializer):
        perfil = self.request.user.perfil_prestador
        log_context = {
            "user_id": self.request.user.id,
            "profile_id": perfil.id,
            "action": "UPDATE_INVOICE",
            "invoice_id": self.get_object().id,
        }

        try:
            with transaction.atomic():
                super().perform_update(serializer)
                logger.info("Actualización de factura exitosa.", extra=log_context)
        except serializers.ValidationError as e:
            log_context['error'] = str(e.detail)
            logger.warning("Fallo en la actualización de factura (Validación).", extra=log_context)
            raise
        except Exception as e:
            log_context['error'] = str(e)
            logger.error("Fallo crítico en la actualización de factura (Excepción).", extra=log_context)
            raise


    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        """
        Confirma una factura comercial, cambia su estado a COMERCIAL_CONFIRMADA,
        y emite una señal para notificar al pipeline de facturación.
        """
        factura = self.get_object()
        if factura.estado != FacturaVenta.Estado.BORRADOR:
            return Response(
                {"error": "Solo se pueden confirmar facturas en estado 'Borrador'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        factura.estado = FacturaVenta.Estado.COMERCIAL_CONFIRMADA
        factura.save()

        # Emitir la señal para el siguiente módulo del pipeline
        from ..signals import factura_comercial_confirmada
        factura_comercial_confirmada.send(sender=self.__class__, factura=factura)

        logger.info(
            "Factura comercial confirmada.",
            extra={
                "user_id": request.user.id,
                "profile_id": factura.perfil.id,
                "action": "CONFIRM_COMMERCIAL_INVOICE",
                "invoice_id": factura.id,
            }
        )

        return Response(
            {"status": "Factura confirmada y enviada al pipeline de facturación."},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], url_path='registrar-pago')
    @transaction.atomic
    def registrar_pago(self, request, pk=None):
        factura = self.get_object()
        perfil = request.user.perfil_prestador
        logger.info(
            f"[FACTURACION] Intento de registro de pago: Factura ID={factura.id}, Perfil={perfil.id}"
        )
        monto_str = request.data.get('monto')
        cuenta_bancaria_id = request.data.get('cuenta_bancaria_id')

        if not monto_str or not cuenta_bancaria_id:
            return Response({"error": "Se requiere 'monto' y 'cuenta_bancaria_id'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            monto = Decimal(monto_str)
            cuenta_bancaria = CuentaBancaria.objects.get(id=cuenta_bancaria_id, perfil=perfil)
        except (ValueError, CuentaBancaria.DoesNotExist):
            return Response({"error": "Monto inválido o cuenta bancaria no encontrada."}, status=status.HTTP_400_BAD_REQUEST)

        # 1. Crear Recibo de Caja
        recibo = ReciboCaja.objects.create(
            perfil=perfil,
            factura=factura,
            cuenta_bancaria=cuenta_bancaria,
            fecha_pago=request.data.get('fecha_pago'),
            monto=monto,
            metodo_pago=request.data.get('metodo_pago', 'TRANSFERENCIA')
        )

        # 2. Crear Transacción de Tesorería
        TransaccionBancaria.objects.create(
            cuenta=cuenta_bancaria,
            fecha=recibo.fecha_pago,
            tipo='INGRESO',
            monto=monto,
            descripcion=f"Pago de Factura No. {factura.numero_factura}",
            creado_por=request.user
        )

        # 3. Crear Asiento Contable del Pago
        try:
            cuenta_caja_bancos = cuenta_bancaria.chart_of_account
            cuenta_cxp = ChartOfAccount.objects.get(perfil=perfil, code='130505') # Cuentas por Cobrar
        except ChartOfAccount.DoesNotExist:
            return Response({"error": "Cuentas contables requeridas no encontradas."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=recibo.fecha_pago,
            description=f"Pago de Factura No. {factura.numero_factura}",
            entry_type="PAGO_RECIBIDO",
            user=request.user,
            origin_document=recibo
        )

        # Débito a Caja/Bancos
        ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_caja_bancos, debit=monto, credit=Decimal('0.00'))
        # Crédito a Cuentas por Cobrar
        ContabTransaction.objects.create(journal_entry=journal_entry, account=cuenta_cxp, debit=Decimal('0.00'), credit=monto)

        factura.actualizar_estado_pago()

        return Response({"status": "Pago registrado con éxito"}, status=status.HTTP_200_OK)

class ReciboCajaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ReciboCajaSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return super().get_queryset()
