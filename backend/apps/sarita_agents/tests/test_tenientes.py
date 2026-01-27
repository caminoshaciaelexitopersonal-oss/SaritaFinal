from django.test import TestCase
from unittest.mock import MagicMock, patch
from backend.apps.sarita_agents.models import TareaDelegada, PlanTáctico, Mision
from backend.apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.validacion_prestador_teniente import TenienteValidacionPrestador
from backend.apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente import TenientePersistenciaPrestador
# Asumimos que existe un modelo Prestador en alguna parte
# from backend.apps.prestadores.models import Prestador

class TenienteValidacionPrestadorTests(TestCase):

    def setUp(self):
        self.teniente = TenienteValidacionPrestador()
        # Creamos los objetos de misión y plan táctico necesarios
        self.mision = Mision.objects.create(directiva_original={"test": "data"}, dominio="prestadores")
        self.plan = PlanTáctico.objects.create(mision=self.mision, capitan_responsable="TestCapitan", pasos_del_plan={})

    def test_validacion_exitosa(self):
        """Prueba que el teniente marca la tarea como COMPLETADA si los datos son válidos."""
        parametros = {"nombre_comercial": "Hotel Paraíso", "email": "contacto@hotelparaiso.com"}
        tarea = TareaDelegada.objects.create(plan_tactico=self.plan, teniente_asignado="validacion", parametros=parametros)

        self.teniente.execute_task(tarea)

        tarea.refresh_from_db()
        self.assertEqual(tarea.estado, 'COMPLETADA')

    def test_validacion_fallida_sin_email(self):
        """Prueba que el teniente marca la tarea como FALLIDA si falta el email."""
        parametros = {"nombre_comercial": "Hotel Olvidado"}
        tarea = TareaDelegada.objects.create(plan_tactico=self.plan, teniente_asignado="validacion", parametros=parametros)

        self.teniente.execute_task(tarea)

        tarea.refresh_from_db()
        self.assertEqual(tarea.estado, 'FALLIDA')

# Mock para el modelo Prestador que aún no existe o no queremos acoplar
class MockPrestador:
    objects = MagicMock()

@patch('backend.apps.sarita_agents.agents.general.sarita.coroneles.prestadores.tenientes.persistencia_prestador_teniente.Prestador', MockPrestador)
class TenientePersistenciaPrestadorTests(TestCase):

    def setUp(self):
        self.teniente = TenientePersistenciaPrestador()
        self.mision = Mision.objects.create(directiva_original={"test": "data"}, dominio="prestadores")
        self.plan = PlanTáctico.objects.create(mision=self.mision, capitan_responsable="TestCapitan", pasos_del_plan={})
        MockPrestador.objects.create.reset_mock()

    def test_persistencia_exitosa(self):
        """Prueba que el teniente llama a Prestador.objects.create con los parámetros correctos."""
        parametros = {"nombre_comercial": "Hotel Central", "email": "ventas@hotelcentral.com"}
        tarea = TareaDelegada.objects.create(plan_tactico=self.plan, teniente_asignado="persistencia", parametros=parametros)

        self.teniente.execute_task(tarea)

        # Verificamos que el método `create` fue llamado una vez con los parámetros correctos
        MockPrestador.objects.create.assert_called_once_with(
            nombre="Hotel Central",
            email="ventas@hotelcentral.com",
            activo=True
        )

        tarea.refresh_from_db()
        self.assertEqual(tarea.estado, 'COMPLETADA')

    def test_persistencia_falla_por_excepcion(self):
        """Prueba que el teniente maneja una excepción de la base de datos y marca la tarea como FALLIDA."""
        parametros = {"nombre_comercial": "Hotel Roto", "email": "error@hotelroto.com"}
        tarea = TareaDelegada.objects.create(plan_tactico=self.plan, teniente_asignado="persistencia", parametros=parametros)

        # Simulamos que la base de datos lanza una excepción
        MockPrestador.objects.create.side_effect = Exception("Error de base de datos")

        self.teniente.execute_task(tarea)

        tarea.refresh_from_db()
        self.assertEqual(tarea.estado, 'FALLIDA')
