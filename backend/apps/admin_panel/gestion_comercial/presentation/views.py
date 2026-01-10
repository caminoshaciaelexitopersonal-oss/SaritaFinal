
import logging
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal
from django.core.exceptions import ValidationError

# Se importan los serializadores desde la nueva ubicación del admin_panel
from .serializers import (
    FacturaVentaListSerializer,
    FacturaVentaDetailSerializer,
    OperacionComercialSerializer
)
# Los modelos se importan desde su ubicación original en el dominio del prestador
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import OperacionComercial, FacturaVenta
from apps.prestadores.mi_negocio.gestion_comercial.services import FacturacionService

# Vista para el Administrador General
# Permite ver y gestionar las operaciones de TODOS los prestadores.

class OperacionComercialAdminViewSet(viewsets.ModelViewSet):
    """
    ViewSet para que el Administrador gestione Operaciones Comerciales de todos los prestadores.
    """
    serializer_class = OperacionComercialSerializer
    permission_classes = [permissions.IsAdminUser] # Solo Admins

    def get_queryset(self):
        # El admin puede ver todas las operaciones comerciales
        return OperacionComercial.objects.all().select_related('perfil', 'cliente')

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        # La lógica de negocio se mantiene, ya que es parte del dominio.
        operacion = self.get_object()
        if operacion.estado != OperacionComercial.Estado.BORRADOR:
            return Response(
                {"error": "Solo se pueden confirmar operaciones en estado 'Borrador'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # El servicio de facturación no necesita cambios
            FacturacionService.facturar_operacion_confirmada(operacion)
        except ValidationError as e:
            return Response({"error": "Error de validación durante la facturación.", "detalle": e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"Error inesperado en confirmación de operación (Admin): {e}", exc_info=True)
            return Response({"error": "Error inesperado durante la facturación.", "detalle": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(OperacionComercialSerializer(operacion).data)


class FacturaVentaAdminViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para que el Administrador vea las Facturas de Venta de todos los prestadores.
    Es de solo lectura para supervisión.
    """
    permission_classes = [permissions.IsAdminUser] # Solo Admins

    def get_serializer_class(self):
        if self.action == 'list':
            return FacturaVentaListSerializer
        return FacturaVentaDetailSerializer

    def get_queryset(self):
        # El admin puede ver todas las facturas
        return FacturaVenta.objects.all().select_related('perfil', 'cliente')

    @action(detail=True, methods=['post'], url_path='registrar-pago')
    def registrar_pago(self, request, pk=None):
        # Esta acción se mantiene como no implementada, consistente con el módulo original.
        return Response(
            {"message": "Endpoint de registro de pago. La lógica se implementará en el módulo correcto."},
            status=status.HTTP_501_NOT_IMPLEMENTED
        )
