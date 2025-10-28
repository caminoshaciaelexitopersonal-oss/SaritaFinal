# backend/apps/comercial/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, FacturaVenta, PagoRecibido, NotaCredito
from .serializers import ClienteSerializer, FacturaVentaSerializer, PagoRecibidoSerializer, NotaCreditoSerializer
from api.permissions import IsOwnerOrReadOnly

class BasePerfilViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet base que automáticamente filtra los objetos por el perfil
    del usuario autenticado y lo asigna al crear nuevos objetos.
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

# --- ViewSets para el Ciclo de Ingresos ---

class ClienteViewSet(BasePerfilViewSet):
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = ClienteSerializer

class FacturaVentaViewSet(BasePerfilViewSet):
    queryset = FacturaVenta.objects.all().order_by('-fecha_emision')
    serializer_class = FacturaVentaSerializer

    def perform_create(self, serializer):
        # Asigna también el created_by
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            created_by=self.request.user
        )

class PagoRecibidoViewSet(BasePerfilViewSet):
    queryset = PagoRecibido.objects.all().order_by('-fecha_pago')
    serializer_class = PagoRecibidoSerializer

class NotaCreditoViewSet(BasePerfilViewSet):
    queryset = NotaCredito.objects.all().order_by('-fecha')
    serializer_class = NotaCreditoSerializer
