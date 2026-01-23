from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .services import sadi_orquestador_service

class SadiCommandView(APIView):
    """
    Punto de entrada de la API para recibir y procesar comandos de voz.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        """
        Recibe un comando de voz en formato de texto y lo procesa.
        """
        # Extraer el comando de la petición.
        command_text = request.data.get('command', None)

        if not command_text:
            return Response(
                {"error": "No se proporcionó ningún comando."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Obtener el usuario autenticado.
        usuario = request.user

        # Procesar el comando a través del servicio orquestador.
        try:
            resultado = sadi_orquestador_service.process_voice_command(
                texto_comando=command_text,
                usuario=usuario
            )
            return Response({"respuesta": resultado}, status=status.HTTP_200_OK)

        except Exception as e:
            # Captura de errores inesperados a nivel de vista.
            return Response(
                {"error": f"Ocurrió un error inesperado: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
