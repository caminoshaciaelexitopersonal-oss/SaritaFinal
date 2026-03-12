from rest_framework import viewsets, permissions
from .models import Room, RoomType, Amenity
from .serializers import RoomSerializer, RoomTypeSerializer, AmenitySerializer

class AmenityViewSet(viewsets.ModelViewSet):
    serializer_class = AmenitySerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Amenity.objects.filter(provider=self.request.user.perfil_prestador)

class RoomTypeViewSet(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return RoomType.objects.filter(provider=self.request.user.perfil_prestador)

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Room.objects.filter(provider=self.request.user.perfil_prestador)
