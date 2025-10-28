# backend/apps/compras/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Proveedor, FacturaProveedor, PagoRealizado
from .serializers import ProveedorSerializer, FacturaProveedorSerializer, PagoRealizadoSerializer
from api.permissions import IsOwnerOrReadOnly

class BasePerfilViewSet(viewsets.ModelViewSet):
    """
    ViewSet base que filtra por perfil del usuario y lo asigna en la creación.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        model_class = self.serializer_class.Meta.model
        if hasattr(user, 'perfil_prestador'):
            return model_class.objects.filter(perfil=user.perfil_prestador)
        return model_class.objects.none()

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

# --- ViewSets para el Ciclo de Compras ---

class ProveedorViewSet(BasePerfilViewSet):
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer

class FacturaProveedorViewSet(BasePerfilViewSet):
    queryset = FacturaProveedor.objects.all().order_by('-fecha_emision')
    serializer_class = FacturaProveedorSerializer

    def perform_create(self, serializer):
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            created_by=self.request.user
        )

class PagoRealizadoViewSet(BasePerfilViewSet):
    queryset = PagoRealizado.objects.all().order_by('-fecha_pago')
    serializer_class = PagoRealizadoSerializer
