from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    NightclubProfile, NightEvent, NightZone, NightTable,
    NightConsumption, NightConsumptionItem, LiquorInventory,
    InventoryMovement, CashClosing, EventLiquidation
)
from .serializers import *

class NightclubBaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(provider=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user.perfil_prestador)

class NightclubProfileViewSet(NightclubBaseViewSet):
    model = NightclubProfile
    serializer_class = NightclubProfileSerializer

class NightEventViewSet(NightclubBaseViewSet):
    model = NightEvent
    serializer_class = NightEventSerializer

    @action(detail=True, methods=['post'])
    def activar(self, request, pk=None):
        evento = self.get_object()
        evento.estado = NightEvent.EventStatus.ACTIVO
        evento.save()
        return Response({'status': 'Evento activado'})

class NightZoneViewSet(NightclubBaseViewSet):
    model = NightZone
    serializer_class = NightZoneSerializer

class NightTableViewSet(NightclubBaseViewSet):
    model = NightTable
    serializer_class = NightTableSerializer

class NightConsumptionViewSet(NightclubBaseViewSet):
    model = NightConsumption
    serializer_class = NightConsumptionSerializer

    @action(detail=True, methods=['post'])
    def agregar_item(self, request, pk=None):
        consumption = self.get_object()
        # Lógica para agregar item y descontar inventario
        return Response({'status': 'Item agregado'})

class LiquorInventoryViewSet(NightclubBaseViewSet):
    model = LiquorInventory
    serializer_class = LiquorInventorySerializer

class InventoryMovementViewSet(NightclubBaseViewSet):
    model = InventoryMovement
    serializer_class = InventoryMovementSerializer

class CashClosingViewSet(NightclubBaseViewSet):
    model = CashClosing
    serializer_class = CashClosingSerializer

class EventLiquidationViewSet(NightclubBaseViewSet):
    model = EventLiquidation
    serializer_class = EventLiquidationSerializer
