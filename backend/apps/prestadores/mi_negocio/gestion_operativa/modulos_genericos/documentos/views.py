from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions import IsOwner

class DocumentoViewSet(viewsets.ViewSet):
    """
    ViewSet para la gestión de Documentos.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def list(self, request):
        return Response({"message": "Módulo de Documentos en desarrollo."}, status=status.HTTP_200_OK)

    def create(self, request):
        return Response({"message": "Funcionalidad no implementada."}, status=status.HTTP_501_NOT_IMPLEMENTED)
