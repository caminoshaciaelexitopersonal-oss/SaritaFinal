from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DeliveryCompany, Driver, Vehicle, DeliveryService, DeliveryEvent
from .serializers import (
    DeliveryCompanySerializer, DriverSerializer, VehicleSerializer,
    DeliveryServiceSerializer, DeliveryEventSerializer
)
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

class DeliveryCompanyViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCompany.objects.all()
    serializer_class = DeliveryCompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeliveryServiceViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return DeliveryService.objects.all()
        if user.role == 'TURISTA':
            return DeliveryService.objects.filter(tourist=user)
        if user.role == 'DELIVERY':
            return DeliveryService.objects.filter(driver__user=user)
        return DeliveryService.objects.none()

    @action(detail=False, methods=['post'])
    def request_delivery(self, request):
        kernel = GovernanceKernel(user=request.user)
        try:
            result = kernel.resolve_and_execute(
                intention_name="DELIVERY_REQUEST",
                parameters=request.data
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def add_event(self, request, pk=None):
        service = self.get_object()
        serializer = DeliveryEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(service=service)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
