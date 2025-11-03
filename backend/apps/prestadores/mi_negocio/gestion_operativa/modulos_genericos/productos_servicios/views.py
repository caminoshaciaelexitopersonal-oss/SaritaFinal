from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ....permissions import IsPrestadorOwner
from .models import ProductoServicio
from .serializers import ProductoServicioSerializer

class ProductoServicioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los productos y servicios de un prestador.
    """
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer
    permission_classes = [IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        """
        Filtra el queryset para devolver solo los objetos que pertenecen
        al perfil del prestador del usuario autenticado.
        """
        try:
            perfil = self.request.user.perfil_prestador
            return super().get_queryset().filter(perfil=perfil)
        except AttributeError:
            # Si el usuario no tiene un perfil de prestador, no puede ver ningún objeto.
            return self.queryset.model.objects.none()

    def perform_create(self, serializer):
        """
        Asocia automáticamente el perfil del prestador al nuevo objeto
        al momento de la creación.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)
