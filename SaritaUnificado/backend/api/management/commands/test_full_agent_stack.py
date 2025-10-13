import asyncio
from django.core.management.base import BaseCommand
from api.models import CustomUser, AgentTask
from agents.corps.sarita_nacion_general import get_sarita_nacion_graph

class Command(BaseCommand):
    help = 'Ejecuta una prueba de extremo a extremo del sistema de agentes jerárquicos.'

    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='La orden en lenguaje natural para el agente.')
        parser.add_argument('--user_id', type=int, default=1, help='El ID del usuario que ejecuta el comando.')

    def handle(self, *args, **options):
        command_text = options['command']
        user_id = options['user_id']

        self.stdout.write(self.style.SUCCESS(f"Iniciando prueba del stack de agentes para el usuario ID: {user_id}"))
        self.stdout.write(self.style.WARNING(f"Orden: '{command_text}'"))

        try:
            # Simulamos la creación de un usuario y una tarea si no existen
            user, _ = CustomUser.objects.get_or_create(id=user_id, defaults={'username': f'testuser{user_id}'})
            task = AgentTask.objects.create(
                user=user,
                command=command_text,
                status=AgentTask.Status.PENDING
            )

            self.stdout.write(self.style.SUCCESS(f"Tarea de agente creada con ID: {task.id}"))

            # Obtenemos el grafo del agente de más alto nivel
            sarita_nacion_agent = get_sarita_nacion_graph()

            # Preparamos el estado inicial para la invocación
            initial_state = {
                "mandate": command_text,
                "user": user, # Pasamos el objeto de usuario completo
                "task_id": str(task.id),
                "conversation_history": []
            }

            self.stdout.write(self.style.NOTICE("--- INICIANDO INVOCACIÓN DEL AGENTE SARITA NACIÓN ---"))

            # Ejecutamos el grafo de forma síncrona
            final_state = asyncio.run(sarita_nacion_agent.ainvoke(initial_state))

            self.stdout.write(self.style.NOTICE("--- INVOCACIÓN COMPLETADA ---"))

            final_report = final_state.get("final_report", "El agente no generó un informe final.")

            self.stdout.write(self.style.SUCCESS("\n--- INFORME FINAL DEL AGENTE ---"))
            self.stdout.write(final_report)

            # Actualizamos la tarea en la BD
            task.status = AgentTask.Status.COMPLETED
            task.report = final_report
            task.save()

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocurrió un error durante la prueba: {e}"))
            import traceback
            traceback.print_exc()