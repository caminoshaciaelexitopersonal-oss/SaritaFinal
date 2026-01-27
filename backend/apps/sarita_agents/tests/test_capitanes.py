from django.test import TestCase
from unittest.mock import patch
from backend.apps.sarita_agents.models import Mision, PlanTáctico
from backend.apps.sarita_agents.agents.general.sarita.coroneles.prestadores.capitanes.onboarding_prestador_capitan import CapitanOnboardingPrestador

class CapitanOnboardingPrestadorIntegrationTests(TestCase):

    def setUp(self):
        self.capitan = CapitanOnboardingPrestador(coronel=None)  # El coronel no es necesario para `plan`

    def test_plan_crea_plan_tactico_correctamente(self):
        """
        Prueba que el método plan() del Capitán crea un PlanTáctico
        con los pasos y parámetros correctos a partir de una Misión.
        """
        # 1. Preparación: Crear una Misión con la directiva esperada
        directiva = {
            "domain": "prestadores",
            "mission": {
                "name": "ONBOARDING_PRESTADOR",
                "datos": {
                    "nombre_comercial": "Hotel de Prueba",
                    "email": "test@hotelprueba.com"
                }
            }
        }
        mision = Mision.objects.create(directiva_original=directiva, dominio="prestadores")

        # 2. Ejecución: Llamar al método `plan` del capitán
        plan_tactico_resultado = self.capitan.plan(mision)

        # 3. Verificación
        self.assertIsInstance(plan_tactico_resultado, PlanTáctico)
        self.assertEqual(plan_tactico_resultado.mision, mision)
        self.assertEqual(plan_tactico_resultado.capitan_responsable, "CapitanOnboardingPrestador")
        self.assertEqual(plan_tactico_resultado.estado, 'PLANIFICADO')

        # Verificar la estructura de los pasos del plan
        pasos = plan_tactico_resultado.pasos_del_plan
        self.assertIn('paso_1_validacion', pasos)
        self.assertIn('paso_2_persistencia', pasos)

        # Verificar los parámetros del paso de validación
        self.assertEqual(pasos['paso_1_validacion']['teniente'], 'validacion')
        self.assertEqual(pasos['paso_1_validacion']['parametros']['nombre_comercial'], "Hotel de Prueba")

        # Verificar los parámetros del paso de persistencia
        self.assertEqual(pasos['paso_2_persistencia']['teniente'], 'persistencia')
        self.assertEqual(pasos['paso_2_persistencia']['parametros']['email'], "test@hotelprueba.com")

        # Contar para asegurar que no hay más pasos de los esperados
        self.assertEqual(len(pasos), 2)
