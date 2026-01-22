from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch, MagicMock

from apps.sadi_agent.services import sadi_orquestador_service
from apps.admin_plataforma.models import Plan

CustomUser = get_user_model()

class SadiOrquestadorServiceTest(TestCase):

    def setUp(self):
        """Configura usuarios para las pruebas."""
        self.admin_user = CustomUser.objects.create_superuser(
            email="admin@test.com",
            password="password123",
            username="adminuser"
        )
        self.normal_user = CustomUser.objects.create_user(
            email="user@test.com",
            password="password123",
            username="normaluser"
        )

    @patch('apps.sadi_agent.services.GestionPlataformaService')
    def test_process_crear_plan_success(self, MockGestionPlataformaService):
        """Verifica que el comando 'crear plan' se procese correctamente."""
        # Configurar el mock del servicio
        mock_service_instance = MockGestionPlataformaService.return_value
        mock_plan = Plan(id=1, nombre="testplan", precio="50", frecuencia="MENSUAL")
        mock_service_instance.crear_plan.return_value = mock_plan

        comando = "crear plan testplan con precio 50 MENSUAL"

        # Ejecutar el orquestador
        resultado = sadi_orquestador_service.process_voice_command(comando, self.admin_user)

        # Verificar
        self.assertEqual(resultado, "Plan 'testplan' creado con éxito con ID 1.")
        mock_service_instance.crear_plan.assert_called_once_with(
            nombre="testplan", precio="50", frecuencia="MENSUAL"
        )

    @patch('apps.sadi_agent.services.AdminPublicacionViewSet')
    def test_process_aprobar_publicacion_success(self, MockAdminPublicacionViewSet):
        """Verifica que el comando 'aprobar publicación' se procese correctamente."""
        # Configurar el mock del ViewSet
        mock_viewset_instance = MockAdminPublicacionViewSet.return_value

        comando = "aprobar publicación 123"

        # Ejecutar el orquestador
        resultado = sadi_orquestador_service.process_voice_command(comando, self.admin_user)

        # Verificar
        self.assertEqual(resultado, "Publicación 123 aprobada.")
        self.assertTrue(mock_viewset_instance.approve.called)

    def test_process_unknown_intent(self):
        """Verifica que el servicio maneje un comando con intención desconocida."""
        comando = "este es un comando inválido"

        resultado = sadi_orquestador_service.process_voice_command(comando, self.admin_user)

        self.assertIn("Error al procesar el comando", resultado)
        self.assertIn("No se pudo determinar la intención del comando", resultado)

    def test_process_permission_denied_for_normal_user(self):
        """Verifica que un usuario no administrador no pueda ejecutar comandos."""
        comando = "crear plan testplan con precio 50 MENSUAL"

        resultado = sadi_orquestador_service.process_voice_command(comando, self.normal_user)

        self.assertIn("Error al procesar el comando", resultado)
        self.assertIn("El usuario no tiene permisos para ejecutar comandos de SADI", resultado)
