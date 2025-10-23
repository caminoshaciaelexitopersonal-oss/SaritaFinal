# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/views/perfil.py
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from apps.prestadores.mi_negocio.permissions import IsOwner
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.serializers import PerfilSerializer

class PerfilViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    ViewSet para que un prestador vea y actualice su propio perfil.
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Filtra el queryset para devolver solo el perfil asociado
        al usuario autenticado.
        """
        if hasattr(self.request.user, 'perfil_prestador'):
            return self.queryset.filter(pk=self.request.user.perfil_prestador.pk)
        return self.queryset.none()
