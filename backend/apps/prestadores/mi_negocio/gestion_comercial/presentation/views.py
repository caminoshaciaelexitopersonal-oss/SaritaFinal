import logging
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal
from django.core.exceptions import ValidationError

from .serializers import (
    FacturaVentaListSerializer,
    FacturaVentaDetailSerializer,
    FacturaVentaWriteSerializer,
    OperacionComercialSerializer
)
from ..domain.models import OperacionComercial, FacturaVenta
from ..services import FacturacionService

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil_ref_id'):
            return obj.perfil_ref_id == request.user.perfil_prestador.id
        return obj.perfil == request.user.perfil_prestador

class OperacionComercialViewSet(viewsets.ModelViewSet):
    serializer_class = OperacionComercialSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return OperacionComercial.objects.filter(perfil_ref_id=self.request.user.perfil_prestador.id)
        return OperacionComercial.objects.none()

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        operacion = self.get_object()
        if operacion.estado != OperacionComercial.Estado.BORRADOR:
            return Response(
                {"error": "Solo se pueden confirmar operaciones en estado 'Borrador'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            FacturacionService.facturar_operacion_confirmada(operacion)
        except ValidationError as e:
            return Response({"error": "Error de validación durante la facturación.", "detalle": e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error inesperado durante la facturación.", "detalle": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(OperacionComercialSerializer(operacion).data)


class FacturaVentaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_serializer_class(self):
        if self.action == 'list':
            return FacturaVentaListSerializer
        if self.action == 'retrieve':
            return FacturaVentaDetailSerializer
        return FacturaVentaWriteSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return FacturaVenta.objects.filter(perfil_ref_id=self.request.user.perfil_prestador.id)
        return FacturaVenta.objects.none()

    @action(detail=True, methods=['post'], url_path='registrar-pago')
    @transaction.atomic
    def registrar_pago(self, request, pk=None):
        factura = self.get_object()
        if factura.estado == FacturaVenta.Estado.PAGADA:
             return Response({"detail": "La factura ya está pagada."}, status=status.HTTP_400_BAD_REQUEST)

        # Usar WalletService para ejecutar el pago real si es vía Monedero
        from apps.wallet.services.wallet_service import WalletService
        from apps.wallet.models import Wallet
        import uuid

        wallet_service = WalletService(user=request.user)
        to_wallet = Wallet.objects.filter(owner_id=str(factura.perfil_ref_id)).first()

        if not to_wallet:
            return Response({"detail": "El prestador no tiene un monedero configurado para recibir pagos digitales."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Ejecutar el pago sistémico
            tx = wallet_service.pay(
                to_wallet_id=str(to_wallet.id),
                amount=factura.total,
                related_service_id=str(factura.id),
                description=f"Pago Factura {factura.numero_factura}"
            )

            # Actualizar estado de la factura
            factura.estado = FacturaVenta.Estado.PAGADA
            factura.save()

            # Registrar impacto en ERP Quíntuple (Automático vía WalletService._integrate_erp)
            # El WalletService ya llama a record_impact para cada movimiento.

            return Response({
                "status": "SUCCESS",
                "transaction_id": str(tx.id),
                "message": "Pago procesado y conciliado en el Monedero Soberano."
            })

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
 

    @action(detail=True, methods=['post'], url_path='send-dian')
    def send_dian(self, request, pk=None):
        factura = self.get_object()
        from ..dian_services import FacturacionElectronicaService
        try:
            log = FacturacionElectronicaService.procesar_envio_dian(factura)
            return Response({
                "status": "SUCCESS" if log.success else "REJECTED",
                "message": "Documento procesado por DIAN" if log.success else log.error_detail,
                "cufe": factura.cufe
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='dian-status')
    def dian_status(self, request, pk=None):
        factura = self.get_object()
        return Response({
            "id": factura.id,
            "numero": factura.numero_factura,
            "estado_dian": factura.get_estado_dian_display(),
            "cufe": factura.cufe,
            "logs": factura.dian_logs.values('timestamp', 'success', 'error_detail')[:5]
        })

    @action(detail=True, methods=['post'], url_path='resend-dian')
    def resend_dian(self, request, pk=None):
        return self.send_dian(request, pk)
 
