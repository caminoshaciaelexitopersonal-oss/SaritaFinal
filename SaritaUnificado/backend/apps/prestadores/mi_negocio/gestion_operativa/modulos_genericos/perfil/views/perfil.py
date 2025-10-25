# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/views/perfil.py
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.prestadores.mi_negocio.permissions import IsOwner
from ..models import Perfil
from ..serializers import PerfilSerializer

class PerfilViewSet(viewsets.GenericViewSet):
    """
    ViewSet singleton para que un prestador vea y actualice su propio perfil.
    No utiliza un `pk` en la URL.
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        """
        Devuelve el perfil asociado al usuario autenticado.
        """
        try:
            # Asegura que solo el dueño pueda acceder.
            obj = self.request.user.perfil_prestador
            self.check_object_permissions(self.request, obj)
            return obj
        except Perfil.DoesNotExist:
            return None

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        """Endpoint para obtener el perfil del usuario actual."""
        instance = self.get_object()
        if instance is None:
            return Response(status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['put', 'patch'])
    def update_me(self, request, *args, **kwargs):
        """Endpoint para actualizar el perfil del usuario actual."""
        instance = self.get_object()
        if instance is None:
            return Response(status=404)
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
