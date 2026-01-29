from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_contable.proyectos.models import Proyecto, IngresoProyecto, CostoProyecto
from .serializers import ProyectoSerializer, IngresoProyectoSerializer, CostoProyectoSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'proyecto') and hasattr(obj.proyecto, 'perfil'):
             return obj.proyecto.perfil == request.user.perfil_prestador
        return False

class ProyectoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return Proyecto.objects.filter(perfil=self.request.user.perfil_prestador)

class IngresoProyectoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = IngresoProyectoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return IngresoProyecto.objects.filter(proyecto__perfil=self.request.user.perfil_prestador)

class CostoProyectoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CostoProyectoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return CostoProyecto.objects.filter(proyecto__perfil=self.request.user.perfil_prestador)
