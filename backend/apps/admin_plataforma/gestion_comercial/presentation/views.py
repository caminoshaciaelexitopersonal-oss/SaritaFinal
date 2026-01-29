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
# IMPORTAR DESDE PRESTADORES (CANÓNICO)
from apps.admin_plataforma.gestion_comercial.domain.models import FacturaVenta, ReciboCaja
from .serializers import (
    FacturaVentaListSerializer,
    FacturaVentaDetailSerializer,
    FacturaVentaWriteSerializer,
    ReciboCajaSerializer
)
# Modelos financieros actualizados
from apps.admin_plataforma.gestion_financiera.models import CuentaBancaria, OrdenPago

class FacturaVentaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_serializer_class(self):
        if self.action == 'list':
            return FacturaVentaListSerializer
        if self.action == 'retrieve':
            return FacturaVentaDetailSerializer
        return FacturaVentaWriteSerializer

    def get_queryset(self):
 
        # El modelo FacturaVenta no tiene relación directa 'cliente' en algunos esquemas
        # pero el Mixin filtrará por perfil_ref_id
        return super().get_queryset()
 

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(perfil_ref_id=perfil.id, creado_por=self.request.user)

class ReciboCajaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ReciboCajaSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return super().get_queryset()
