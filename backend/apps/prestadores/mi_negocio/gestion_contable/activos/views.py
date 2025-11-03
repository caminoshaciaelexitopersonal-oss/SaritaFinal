from rest_framework import viewsets, permissions
from .models import CategoriaActivo, ActivoFijo, Depreciacion
from .serializers import CategoriaActivoSerializer, ActivoFijoSerializer, DepreciacionSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'activo') and hasattr(obj.activo, 'perfil'):
             return obj.activo.perfil == request.user.perfil_prestador
        return False

class CategoriaActivoViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaActivoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return CategoriaActivo.objects.filter(perfil=self.request.user.perfil_prestador)

class ActivoFijoViewSet(viewsets.ModelViewSet):
    serializer_class = ActivoFijoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return ActivoFijo.objects.filter(perfil=self.request.user.perfil_prestador)

class DepreciacionViewSet(viewsets.ModelViewSet):
    serializer_class = DepreciacionSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return Depreciacion.objects.filter(activo__perfil=self.request.user.perfil_prestador)
