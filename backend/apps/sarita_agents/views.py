 
# backend/apps/sarita_agents/views.py
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from backend.models import Mision
from backend.serializers import MisionSerializer, DirectiveSerializer
from backend.orchestrator import sarita_orchestrator
from backend.tasks import ejecutar_mision_completa

class DirectiveView(APIView):
    """
    Recibe una directiva, crea una Misión y encola su ejecución asíncrona.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = DirectiveSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        idempotency_key = validated_data.get('idempotency_key')

        try:
            # 1. Crear la Misión (esto también verifica la idempotencia)
            mision = sarita_orchestrator.start_mission(
                directive=validated_data,
                idempotency_key=idempotency_key
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_409_CONFLICT)

        # 2. Encolar la ejecución de la misión DESPUÉS de que la transacción se confirme.
        transaction.on_commit(lambda: ejecutar_mision_completa.delay(mision_id=str(mision.id)))

        response_data = {
            "mission_id": mision.id,
            "status": mision.estado
        }
        return Response(response_data, status=status.HTTP_202_ACCEPTED)

class MissionStatusView(APIView):
    """
    Consulta el estado y la trazabilidad completa de una misión.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        try:
            mision = Mision.objects.get(id=id)
            serializer = MisionSerializer(mision)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Mision.DoesNotExist:
            return Response(
                {"error": "Misión no encontrada."},
                status=status.HTTP_404_NOT_FOUND
            )
 
