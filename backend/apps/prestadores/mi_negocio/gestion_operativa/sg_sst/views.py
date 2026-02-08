from rest_framework import viewsets, permissions
from .models import MatrizRiesgo, IncidenteLaboral, SaludOcupacional, CapacitacionSST
from .serializers import MatrizRiesgoSerializer, IncidenteLaboralSerializer, SaludOcupacionalSerializer, CapacitacionSSTSerializer

class IsSSTOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return str(obj.provider_id) == str(request.user.perfil_prestador.id)

class MatrizRiesgoViewSet(viewsets.ModelViewSet):
    serializer_class = MatrizRiesgoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSSTOwner]
    def get_queryset(self):
        return MatrizRiesgo.objects.filter(provider_id=self.request.user.perfil_prestador.id)

class IncidenteLaboralViewSet(viewsets.ModelViewSet):
    serializer_class = IncidenteLaboralSerializer
    permission_classes = [permissions.IsAuthenticated, IsSSTOwner]
    def get_queryset(self):
        return IncidenteLaboral.objects.filter(provider_id=self.request.user.perfil_prestador.id)

class SaludOcupacionalViewSet(viewsets.ModelViewSet):
    serializer_class = SaludOcupacionalSerializer
    permission_classes = [permissions.IsAuthenticated, IsSSTOwner]
    def get_queryset(self):
        return SaludOcupacional.objects.filter(provider_id=self.request.user.perfil_prestador.id)

class CapacitacionSSTViewSet(viewsets.ModelViewSet):
    serializer_class = CapacitacionSSTSerializer
    permission_classes = [permissions.IsAuthenticated, IsSSTOwner]
    def get_queryset(self):
        return CapacitacionSST.objects.filter(provider_id=self.request.user.perfil_prestador.id)
