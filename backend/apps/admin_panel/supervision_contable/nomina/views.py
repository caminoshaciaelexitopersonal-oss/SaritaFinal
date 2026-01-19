from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Empleado, Contrato, Planilla, ConceptoNomina
from .serializers import EmpleadoSerializer, ContratoSerializer, PlanillaSerializer, ConceptoNominaSerializer


class EmpleadoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAdminUser]
    def get_queryset(self):
        return .objects.all()

class ContratoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    permission_classes = [permissions.IsAdminUser]
    def get_queryset(self):
        return Contrato.objects.filter(empleado__perfil=self.request.user.perfil_prestador)

class PlanillaAdminViewSet(viewsets.ModelViewSet):
    serializer_class = PlanillaSerializer
    permission_classes = [permissions.IsAdminUser]
    def get_queryset(self):
        return .objects.all()

class ConceptoNominaAdminViewSet(viewsets.ModelViewSet):
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [permissions.IsAuthenticated]
