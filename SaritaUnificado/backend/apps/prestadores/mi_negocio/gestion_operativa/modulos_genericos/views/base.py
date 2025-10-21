from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ....permissions import IsOwner

class GenericViewSet(viewsets.ModelViewSet):
    """
    ViewSet genérico para los módulos de 'Mi Negocio'.
    - Aplica permisos de IsAuthenticated y IsOwner.
    - Filtra automáticamente el queryset para devolver solo los objetos
      pertenecientes al perfil del prestador que realiza la solicitud.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Filtra el queryset para devolver solo los objetos asociados
        al perfil del usuario autenticado.
        """
        # Asegurarse de que el usuario tenga un perfil de prestador
        if hasattr(self.request.user, 'perfil_prestador'):
            return self.queryset.filter(perfil=self.request.user.perfil_prestador)
        # Si no tiene perfil, no puede poseer ningún objeto
        return self.queryset.none()

    def perform_create(self, serializer):
        """
        Asigna automáticamente el perfil del prestador al crear un nuevo objeto.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)
