from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.prestadores.mi_negocio.permissions import IsOwnerAndPrestador
from .models import Inventario
from .serializers import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar el inventario de un prestador.
    """
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndPrestador]

    def get_queryset(self):
        """
        Filtra el queryset para devolver solo los objetos que pertenecen
        al perfil del prestador del usuario autenticado.
        """
        try:
            perfil = self.request.user.perfil_prestador
            return super().get_queryset().filter(perfil=perfil)
        except AttributeError:
            return self.queryset.model.objects.none()

    def perform_create(self, serializer):
        """
        Asocia automáticamente el perfil del prestador al nuevo ítem de inventario.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)
