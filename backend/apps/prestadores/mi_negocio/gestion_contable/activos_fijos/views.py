from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .models import CategoriaActivo, ActivoFijo, CalculoDepreciacion
from .serializers import CategoriaActivoSerializer, ActivoFijoSerializer, CalculoDepreciacionSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # El perfil se encuentra en el objeto principal o a través de una relación
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'activo'):
            return obj.activo.perfil == request.user.perfil_prestador
        return False

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoriaActivoViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaActivoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return CategoriaActivo.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class ActivoFijoViewSet(viewsets.ModelViewSet):
    serializer_class = ActivoFijoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return ActivoFijo.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class CalculoDepreciacionViewSet(viewsets.ModelViewSet):
    serializer_class = CalculoDepreciacionSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get', 'post', 'head', 'options'] # Solo permitir crear y listar

    def get_queryset(self):
        return CalculoDepreciacion.objects.filter(activo__perfil=self.request.user.perfil_prestador)
