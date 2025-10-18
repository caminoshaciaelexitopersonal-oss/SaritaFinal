from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto, Vacante, Cliente, Inventario, Costo
from .serializers import ProductoSerializer, VacanteSerializer, ClienteSerializer, InventarioSerializer, CostoSerializer
from api.permissions import IsPrestador, IsPrestadorOwner

# --- Vistas para el Módulo de Clientes (CRM) ---
class ClienteViewSet(viewsets.ModelViewSet):
    """
    Gestiona los clientes de un prestador de servicios.
    """
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'email', 'telefono']
    ordering_fields = ['nombre', 'fecha_creacion']

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Cliente.objects.filter(prestador=self.request.user.perfil_prestador)
        return Cliente.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

# --- Vistas para el Módulo de Productos/Servicios ---
class ProductoViewSet(viewsets.ModelViewSet):
    """
    Gestiona los productos o servicios ofrecidos por un prestador.
    """
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Producto.objects.filter(prestador=self.request.user.perfil_prestador)
        return Producto.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

# --- Vistas para el Módulo de Inventario ---
class InventarioViewSet(viewsets.ModelViewSet):
    """
    Gestiona el inventario de un prestador.
    """
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Inventario.objects.filter(prestador=self.request.user.perfil_prestador)
        return Inventario.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

# --- Vistas para el Módulo de Costos ---
class CostoViewSet(viewsets.ModelViewSet):
    """
    Gestiona los costos operativos de un prestador.
    """
    serializer_class = CostoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return Costo.objects.filter(prestador=self.request.user.perfil_prestador)
        return Costo.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

# --- Vistas para el Módulo de Empleo / Vacantes ---
class VacanteViewSet(viewsets.ModelViewSet):
    """
    Gestiona las vacantes de empleo. Accesible públicamente para lectura.
    """
    queryset = Vacante.objects.all()
    serializer_class = VacanteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo_contrato', 'ubicacion']
    search_fields = ['titulo', 'descripcion', 'empresa__nombre_negocio']
    ordering_fields = ['fecha_publicacion', 'salario']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsPrestador]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'perfil_prestador'):
             if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
                return Vacante.objects.filter(empresa=self.request.user.perfil_prestador)
        return Vacante.objects.filter(activa=True)

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'perfil_prestador'):
            serializer.save(empresa=self.request.user.perfil_prestador)
        else:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("No tienes un perfil de prestador para crear una vacante.")