from rest_framework import viewsets, permissions
from .models import Empleado, Contrato, Planilla, ConceptoNomina
from .serializers import EmpleadoSerializer, ContratoSerializer, PlanillaSerializer, ConceptoNominaSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    def get_queryset(self):
        return Empleado.objects.filter(perfil=self.request.user.perfil_prestador)

class ContratoViewSet(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    def get_queryset(self):
        return Contrato.objects.filter(empleado__perfil=self.request.user.perfil_prestador)

class PlanillaViewSet(viewsets.ModelViewSet):
    serializer_class = PlanillaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    def get_queryset(self):
        return Planilla.objects.filter(perfil=self.request.user.perfil_prestador)

class ConceptoNominaViewSet(viewsets.ModelViewSet):
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [permissions.IsAuthenticated]
