# backend/apps/comercial/views.py
from rest_framework import viewsets, permissions
from .models import FacturaVenta
from .serializers import FacturaVentaSerializer
from apps.prestadores.mi_negocio.permissions import IsOwnerAndPrestador

class FacturaVentaViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaVentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerAndPrestador]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return FacturaVenta.objects.filter(perfil=user.perfil_prestador)
        return FacturaVenta.objects.none()

    def perform_create(self, serializer):
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            created_by=self.request.user
        )
