from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Perfil, CategoriaPrestador, Cliente, ProductoServicio, Inventario, Costo
from .serializers import (
    PerfilSerializer,
    CategoriaPrestadorSerializer,
    ClienteSerializer,
    ProductoServicioSerializer,
    InventarioSerializer,
    CostoSerializer
)

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Perfil.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class CategoriaPrestadorListView(generics.ListAPIView):
    queryset = CategoriaPrestador.objects.all()
    serializer_class = CategoriaPrestadorSerializer
    permission_classes = [IsAuthenticated]

class BasePrestadorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Asegurarse de que el usuario solo vea los objetos relacionados con su perfil de prestador
        try:
            perfil = self.request.user.perfil_prestador
            return self.queryset.filter(perfil=perfil)
        except Perfil.DoesNotExist:
            return self.queryset.none()

    def perform_create(self, serializer):
        perfil = self.request.user.perfil_prestador
        serializer.save(perfil=perfil)

class ClienteViewSet(BasePrestadorViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoServicioViewSet(BasePrestadorViewSet):
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

class InventarioViewSet(BasePrestadorViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class CostoViewSet(BasePrestadorViewSet):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer
