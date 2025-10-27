from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions import IsOwner

class ValoracionViewSet(viewsets.ViewSet):
    """
    ViewSet para la gestión de Valoraciones.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def list(self, request):
        return Response({"message": "Módulo de Valoraciones en desarrollo."}, status=status.HTTP_200_OK)
