from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto, RegistroCliente, Vacante
from .serializers import ProductoSerializer, RegistroClienteSerializer, VacanteSerializer
from api.permissions import IsPrestador, IsPrestadorOwner # Reutilizamos los permisos de la app api

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        # Asegurarse de que el usuario tenga un perfil de prestador
        if hasattr(self.request.user, 'perfil_prestador'):
            return Producto.objects.filter(prestador=self.request.user.perfil_prestador)
        return Producto.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class RegistroClienteViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroClienteSerializer
    permission_classes = [IsAuthenticated, IsPrestador, IsPrestadorOwner]

    def get_queryset(self):
        if hasattr(self.request.user, 'perfil_prestador'):
            return RegistroCliente.objects.filter(prestador=self.request.user.perfil_prestador)
        return RegistroCliente.objects.none()

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user.perfil_prestador)

class VacanteViewSet(viewsets.ModelViewSet):
    queryset = Vacante.objects.all() # El filtrado se hará en get_queryset
    serializer_class = VacanteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo_contrato', 'ubicacion']
    search_fields = ['titulo', 'descripcion', 'empresa__nombre_negocio']
    ordering_fields = ['fecha_publicacion', 'salario']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsPrestador]
        else: # list, retrieve
            # Permitimos que cualquiera vea las vacantes, pero el queryset las filtra
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        # Los prestadores solo ven y gestionan sus propias vacantes.
        if self.request.user.is_authenticated and hasattr(self.request.user, 'perfil_prestador'):
             if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
                return Vacante.objects.filter(empresa=self.request.user.perfil_prestador)

        # Por defecto, solo mostrar vacantes activas a otros usuarios
        return Vacante.objects.filter(activa=True)

    def perform_create(self, serializer):
        # Asigna automáticamente la empresa del prestador autenticado
        if hasattr(self.request.user, 'perfil_prestador'):
            serializer.save(empresa=self.request.user.perfil_prestador)
        else:
            # Esto no debería ocurrir gracias a los permisos, pero es una salvaguarda
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("No tienes un perfil de prestador para crear una vacante.")