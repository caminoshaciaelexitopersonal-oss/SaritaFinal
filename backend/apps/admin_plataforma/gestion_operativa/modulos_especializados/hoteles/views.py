from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_operativa.modulos_especializados.hoteles.models import Amenity, RoomType, Room
from .serializers import AdminAmenitySerializer, AdminRoomTypeSerializer, AdminRoomSerializer

class HotelFeatureViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

class AmenityViewSet(HotelFeatureViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AdminAmenitySerializer

class RoomTypeViewSet(HotelFeatureViewSet):
    queryset = RoomType.objects.all()
    serializer_class = AdminRoomTypeSerializer

class RoomViewSet(HotelFeatureViewSet):
    queryset = Room.objects.select_related('room_type').all()
    serializer_class = AdminRoomSerializer
    filterset_fields = ['room_type']
