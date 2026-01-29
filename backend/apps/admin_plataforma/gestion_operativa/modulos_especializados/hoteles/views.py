from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.hoteles.models import Amenity, RoomType, Room
from .serializers import AmenitySerializer, RoomTypeSerializer, RoomSerializer

class HotelFeatureViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

class AmenityViewSet(HotelFeatureViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

class RoomTypeViewSet(HotelFeatureViewSet):
    queryset = RoomType.objects.select_related('product').prefetch_related('amenities').all()
    serializer_class = RoomTypeSerializer

class RoomViewSet(HotelFeatureViewSet):
    queryset = Room.objects.select_related('room_type__product').all()
    serializer_class = RoomSerializer
    filterset_fields = ['room_type', 'housekeeping_status']
