from django.db import models
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models.provider_models import TourismProvider, BusinessProfile, TourismService, Reservation
from ..serializers.provider_serializers import (
    TourismProviderSerializer, BusinessProfileSerializer,
    TourismServiceSerializer, ReservationSerializer,
    TourismSubClassificationSerializer
)
from ..services.financial_service import TourismFinancialService
from ..models.provider_models import TourismSubClassification

class TourismSubClassificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TourismSubClassification.objects.all()
    serializer_class = TourismSubClassificationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']

class TourismProviderViewSet(viewsets.ModelViewSet):
    queryset = TourismProvider.objects.all()
    serializer_class = TourismProviderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['municipality', 'provider_type', 'status', 'department']
    search_fields = ['name', 'sub_classification']
    ordering_fields = ['puntuacion_total', 'created_at']

    def get_queryset(self):
        # Si es una petición de lectura (GET), mostrar solo los aprobados (PUBLICADO)
        if self.request.method == 'GET':
            # Si el usuario es staff, puede ver todos
            if self.request.user.is_authenticated and self.request.user.is_staff:
                return TourismProvider.objects.all()
            return TourismProvider.objects.filter(status='PUBLICADO')

        # Para peticiones de escritura, cada dueño solo ve sus propios prestadores
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return TourismProvider.objects.all()
            return TourismProvider.objects.filter(owner=self.request.user)
        return TourismProvider.objects.none()

    def perform_create(self, serializer):
        provider = serializer.save(owner=self.request.user)
        # Sincronización automática con RNT si se proveyó número
        if provider.rnt_number:
            from ..services.rnt_integration import RNTIntegrationService
            RNTIntegrationService.sync_provider(provider.id)

    @action(detail=True, methods=['post'])
    def sync_rnt(self, request, pk=None):
        """
        Fuerza la sincronización manual con el Registro Nacional de Turismo.
        """
        from ..services.rnt_integration import RNTIntegrationService
        success = RNTIntegrationService.sync_provider(pk)
        if success:
            return Response({"status": "success", "message": "Datos sincronizados con éxito."})
        return Response({"status": "error", "message": "No se pudo validar el RNT."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        """
        Devuelve el perfil del prestador logueado.
        """
        provider = TourismProvider.objects.filter(owner=request.user).first()
        if not provider:
             return Response({"error": "No provider profile found"}, status=404)
        return Response(TourismProviderSerializer(provider).data)

    @action(detail=False, methods=['get'], url_path='nearby')
    def nearby(self, request):
        """
        Busca prestadores cercanos a una ubicación (lat, lng).
        Uso: /api/v1/turismo/tourism-providers/nearby/?lat=1.23&lng=-73.45&radius=5
        """
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        radius = request.query_params.get('radius', 10) # km default

        if not lat or not lng:
            return Response({"error": "Se requieren lat y lng"}, status=400)

        # Simple bounding box for demo (real GIS would use Point/Distance)
        # 0.1 deg is approx 11km
        delta = float(radius) / 111.0

        qs = TourismProvider.objects.filter(
            status='PUBLICADO',
            location__lat__gte=float(lat) - delta,
            location__lat__lte=float(lat) + delta,
            location__lng__gte=float(lng) - delta,
            location__lng__lte=float(lng) + delta
        )

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        """
        Aprueba un prestador para que sea visible en el directorio público.
        """
        provider = self.get_object()
        provider.status = 'PUBLICADO'
        provider.save()
        return Response({"status": "success", "message": "Prestador aprobado exitosamente."})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk=None):
        """
        Rechaza un prestador o lo devuelve a estado pendiente.
        """
        provider = self.get_object()
        provider.status = 'RECHAZADO'
        provider.save()
        return Response({"status": "success", "message": "Prestador rechazado."})

    @action(detail=False, methods=['post'], url_path='login-rnt', permission_classes=[permissions.AllowAny])
    def login_rnt(self, request):
        """
        Inicia sesión utilizando credenciales validadas del Registro Nacional de Turismo.
        """
        rnt_number = request.data.get('rnt_number')
        # password_token = request.data.get('rnt_token') # En producción

        from ..services.rnt_integration import RNTIntegrationService
        user = RNTIntegrationService.login_via_rnt(rnt_number, None)

        if user:
            # Aquí se retornaría un JWT real
            return Response({
                "status": "success",
                "message": f"Acceso concedido para RNT {rnt_number}",
                "user": user.username
            })
        return Response({"error": "Credenciales RNT inválidas o prestador no registrado."}, status=status.HTTP_401_UNAUTHORIZED)

class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class TourismServiceViewSet(viewsets.ModelViewSet):
    queryset = TourismService.objects.all()
    serializer_class = TourismServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Reservation.objects.all()
        # Turista ve sus reservas, Dueño ve las reservas de sus prestadores
        return Reservation.objects.filter(
            models.Q(customer=user) | models.Q(provider__owner=user)
        ).distinct()

    @action(detail=True, methods=['post'])
    def process_payment(self, request, pk=None):
        """
        Inicia el flujo de pago de la reserva.
        """
        try:
            result = TourismFinancialService.process_reservation_payment(pk)
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
