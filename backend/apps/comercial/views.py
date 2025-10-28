# backend/apps/comercial/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, FacturaVenta, PagoRecibido, NotaCredito
from .serializers import ClienteSerializer, FacturaVentaSerializer, PagoRecibidoSerializer, NotaCreditoSerializer
from api.permissions import IsOwnerOrReadOnly

class BasePerfilViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        model_class = self.serializer_class.Meta.model
        if hasattr(self.request.user, 'perfil_prestador'):
            return model_class.objects.filter(perfil=self.request.user.perfil_prestador)
        return model_class.objects.none()
    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class ClienteViewSet(BasePerfilViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FacturaVentaViewSet(BasePerfilViewSet):
    queryset = FacturaVenta.objects.all()
    serializer_class = FacturaVentaSerializer
    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador, created_by=self.request.user)

class PagoRecibidoViewSet(BasePerfilViewSet): # <-- ViewSet añadido
    queryset = PagoRecibido.objects.all()
    serializer_class = PagoRecibidoSerializer

class NotaCreditoViewSet(BasePerfilViewSet):
    queryset = NotaCredito.objects.all()
    serializer_class = NotaCreditoSerializer
