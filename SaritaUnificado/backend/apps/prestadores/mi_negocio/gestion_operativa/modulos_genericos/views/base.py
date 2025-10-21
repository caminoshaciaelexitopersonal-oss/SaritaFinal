# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/base.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsOwner

class GenericViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet base que asegura que el usuario esté autenticado
    y solo pueda ver/editar los objetos que le pertenecen (asociados a su perfil).
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Filtra el queryset para devolver solo los objetos
        asociados al Perfil del usuario autenticado.
        """
        user = self.request.user
        # Asumiendo que el CustomUser tiene una relación 'perfil_prestador'
        if hasattr(user, 'perfil_prestador') and user.perfil_prestador:
            return self.queryset.filter(perfil=user.perfil_prestador)
        # Si no tiene perfil, no puede ver nada.
        return self.queryset.none()

    def perform_create(self, serializer):
        """
        Asigna automáticamente el Perfil del usuario al objeto
        que se está creando.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)
