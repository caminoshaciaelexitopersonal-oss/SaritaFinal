from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions import IsOwner

class ReservaViewSet(viewsets.ViewSet):
    """
    ViewSet para la gestión de Reservas (RAT).
    Funcionalidad futura.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def list(self, request):
        # Lógica futura para listar reservas
        return Response({"message": "Módulo de Reservas en desarrollo."}, status=status.HTTP_200_OK)

    def create(self, request):
        # Lógica futura para crear una reserva
        return Response({"message": "Funcionalidad no implementada."}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, pk=None):
        # Lógica futura para obtener una reserva
        return Response({"message": "Funcionalidad no implementada."}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, pk=None):
        # Lógica futura para actualizar una reserva
        return Response({"message": "Funcionalidad no implementada."}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def destroy(self, request, pk=None):
        # Lógica futura para eliminar una reserva
        return Response({"message": "Funcionalidad no implementada."}, status=status.HTTP_501_NOT_IMPLEMENTED)
