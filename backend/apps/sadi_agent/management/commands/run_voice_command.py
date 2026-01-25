# backend/apps/sadi_agent/management/commands/run_voice_command.py
import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from apps.sadi_agent.voice_orchestrator import VoiceOrchestrator
import logging

# Configurar un logger simple para la salida del comando
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(BaseCommand):
    help = 'Simula la ejecución de un comando de voz a través del VoiceOrchestrator.'

    def add_arguments(self, parser):
        parser.add_argument('command_text', type=str, help='El texto del comando de voz a simular.')
        parser.add_argument('--user', type=str, default='sadi', help='El nombre de usuario para obtener el token de API.')

    def handle(self, *args, **options):
        command_text = options['command_text']
        username = options['user']

        self.stdout.write(self.style.SUCCESS(f"Iniciando simulación de comando de voz para el usuario '{username}'..."))
        self.stdout.write(f"Comando: '{command_text}'")

        try:
            # 1. Obtener el token de API para el usuario especificado
            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                self.stdout.write(self.style.WARNING(f"Se ha creado un nuevo token de API para el usuario '{username}'."))

            self.stdout.write(f"Token de API obtenido con éxito.")

            # 2. Instanciar el orquestador
            # Usamos variables de entorno o un default para la URL base de la API
            api_base_url = os.environ.get("SADI_API_BASE_URL", "http://127.0.0.1:8000/api/sarita")
            orchestrator = VoiceOrchestrator(api_token=token.key, api_base_url=api_base_url)
            self.stdout.write(f"VoiceOrchestrator instanciado. Apuntando a: {api_base_url}")

            # 3. Ejecutar el comando de voz
            self.stdout.write(self.style.NOTICE("\n--- INICIO DE LA ORQUESTACIÓN ---"))
            spoken_response = orchestrator.handle_voice_command(command_text)
            self.stdout.write(self.style.NOTICE("--- FIN DE LA ORQUESTACIÓN ---\n"))

            # 4. Mostrar la respuesta final
            self.stdout.write(self.style.SUCCESS("Respuesta final generada:"))
            self.stdout.write(spoken_response)

        except User.DoesNotExist:
            raise CommandError(f"El usuario '{username}' no existe. Asegúrese de que el usuario exista en la base de datos.")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ha ocurrido un error durante la ejecución: {e}"))
            # Opcional: imprimir traceback si se necesita más detalle en el debug
            # import traceback
            # traceback.print_exc()
