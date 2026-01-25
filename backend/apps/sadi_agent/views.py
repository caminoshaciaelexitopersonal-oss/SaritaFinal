from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, permissions
from .services import sadi_orquestador_service
from .models import AgentExecution
from .serializers import AgentExecutionSerializer, AgentExecutionCreateSerializer
from .tasks import run_agent_execution


class SadiCommandView(APIView):
    """
    Punto de entrada de la API para recibir y procesar comandos de voz.
    """
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        """
        Recibe un comando de voz en formato de texto y lo procesa.
        """
        command_text = request.data.get('command', None)
        if not command_text:
            return Response({"error": "No se proporcionó ningún comando."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            resultado = sadi_orquestador_service.process_voice_command(
                texto_comando=command_text,
                usuario=request.user
            )
            return Response({"respuesta": resultado}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Ocurrió un error inesperado: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AgentExecutionViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet for Agent Executions.
    - `create`: Starts a new agent execution.
    - `retrieve`: Fetches the status and results of an execution.
    - `list`: Lists all executions for the authenticated user.
    """
    queryset = AgentExecution.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return AgentExecutionCreateSerializer
        return AgentExecutionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the executions
        for the currently authenticated user.
        """
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Initiates a new agent execution by dispatching a Celery task.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the initial execution object with PENDING status
        execution = serializer.save(user=request.user)

        # Dispatch the Celery task to run the agent in the background
        run_agent_execution.delay(execution_id=str(execution.id))

        # Return the initial data with a 202 Accepted status
        response_serializer = AgentExecutionSerializer(execution)
        return Response(response_serializer.data, status=status.HTTP_202_ACCEPTED)
