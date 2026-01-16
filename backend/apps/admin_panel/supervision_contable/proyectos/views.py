from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Proyecto, IngresoProyecto, CostoProyecto
from .serializers import ProyectoSerializer, IngresoProyectoSerializer, CostoProyectoSerializer

        if hasattr(obj, 'proyecto') and hasattr(obj.proyecto, 'perfil'):
             return obj.proyecto.perfil == request.user.perfil_prestador
        return False

class ProyectoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return .objects.all()

class IngresoProyectoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = IngresoProyectoSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return IngresoProyecto.objects.filter(proyecto__perfil=self.request.user.perfil_prestador)

class CostoProyectoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = CostoProyectoSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return CostoProyecto.objects.filter(proyecto__perfil=self.request.user.perfil_prestador)
