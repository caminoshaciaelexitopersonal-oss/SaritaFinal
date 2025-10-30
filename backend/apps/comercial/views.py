# backend/apps/comercial/views.py
from rest_framework import viewsets, permissions
from .models import Cliente, FacturaVenta
from .serializers import ClienteSerializer, FacturaVentaSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Cliente.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class FacturaVentaViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaVentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return FacturaVenta.objects.filter(perfil=self.request.user.perfil_prestador).select_related('cliente')

    def perform_create(self, serializer):
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            created_by=self.request.user
        )
