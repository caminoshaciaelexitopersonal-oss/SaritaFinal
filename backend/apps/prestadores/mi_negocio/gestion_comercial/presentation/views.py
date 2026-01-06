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
    OperacionComercialSerializer
)
from ..domain.models import OperacionComercial, FacturaVenta
from ..services import FacturacionService

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class OperacionComercialViewSet(viewsets.ModelViewSet):
    serializer_class = OperacionComercialSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    def get_queryset(self):
        return OperacionComercial.objects.filter(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        operacion = self.get_object()
        # ... (lógica de confirmación existente)
        return Response(OperacionComercialSerializer(operacion).data)


class FacturaVentaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_serializer_class(self):
        if self.action == 'list':
            return FacturaVentaListSerializer
        return FacturaVentaDetailSerializer

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador).select_related('cliente')

    @action(detail=True, methods=['post'], url_path='registrar-pago')
    @transaction.atomic
    def registrar_pago(self, request, pk=None):
        # NOTA ARQUITECTÓNICA: La lógica de pago fue eliminada de este módulo.
        # Un servicio de aplicación debería orquestar esta llamada.
        # 1. Validar la factura (pertenece a gestion_comercial).
        # 2. Llamar a un servicio de pagos (pertenece a gestion_financiera).
        # 3. El servicio de pagos crea la OrdenPago y llama al servicio de contabilidad.

        # Por ahora, esta acción queda como un placeholder para no romper la URL.
        return Response(
            {"message": "Endpoint de registro de pago. La lógica se implementará en el módulo correcto."},
            status=status.HTTP_501_NOT_IMPLEMENTED
        )
