from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from datetime import date

from apps.prestadores.models import Perfil, CategoriaPrestador
from .models import Empleado, ConceptoNomina, Nomina
from .services import procesar_nomina_service

User = get_user_model()

class NominaBaseTestCase(TestCase):
    """
    Clase base para configurar los datos de prueba necesarios.
    """
    def setUp(self):
        # Crear usuario y perfil de prestador
        self.user = User.objects.create_user(
            username='prestador',
            email='prestador@test.com',
            password='password123',
            role='prestador'
        )
        self.categoria = CategoriaPrestador.objects.create(nombre='Hotel', slug='hotel')
        self.perfil = Perfil.objects.create(
            usuario=self.user,
            nombre_comercial='Hotel Sarita',
            categoria=self.categoria
        )

        # Crear empleado
        self.empleado = Empleado.objects.create(
            perfil=self.perfil,
            nombre='Juan',
            apellido='Perez',
            tipo_documento='CC',
            numero_documento='123456',
            fecha_nacimiento=date(1990, 1, 1),
            fecha_contratacion=date(2022, 1, 1),
            salario_base=Decimal('2000000.00'),
            activo=True
        )

        # Crear conceptos de nómina
        self.concepto_bono = ConceptoNomina.objects.create(
            codigo='BONO_FIJO',
            descripcion='Bonificación Fija',
            tipo='ingreso',
            es_fijo=True,
            valor=Decimal('100000.00')
        )
        self.concepto_salud = ConceptoNomina.objects.create(
            codigo='APORTE_SALUD',
            descripcion='Aporte a Salud (4%)',
            tipo='deduccion',
            es_fijo=False,
            valor=Decimal('0.04')
        )


class NominaServiceTests(NominaBaseTestCase):
    """
    Pruebas para el servicio de procesamiento de nómina.
    """
    def test_procesar_nomina_correctamente(self):
        """
        Verifica que el servicio procese la nómina y calcule los totales correctamente.
        """
        nomina = procesar_nomina_service(
            perfil=self.perfil,
            fecha_inicio=date(2023, 1, 1),
            fecha_fin=date(2023, 1, 31)
        )

        self.assertIsNotNone(nomina)
        self.assertEqual(nomina.estado, 'procesada')

        # Cálculos esperados
        salario_base = self.empleado.salario_base
        bono = self.concepto_bono.valor
        aporte_salud = salario_base * self.concepto_salud.valor

        total_ingresos_esperado = salario_base + bono
        total_deducciones_esperado = aporte_salud
        neto_a_pagar_esperado = total_ingresos_esperado - total_deducciones_esperado

        self.assertEqual(nomina.total_ingresos, total_ingresos_esperado)
        self.assertEqual(nomina.total_deducciones, total_deducciones_esperado)
        self.assertEqual(nomina.neto_a_pagar, neto_a_pagar_esperado)

        # Verificar que se crearon los detalles
        self.assertEqual(nomina.detalles.count(), 2)

    def test_procesar_nomina_sin_empleados_activos(self):
        """
        Verifica que el servicio lance una excepción si no hay empleados activos.
        """
        self.empleado.activo = False
        self.empleado.save()

        with self.assertRaises(ValueError):
            procesar_nomina_service(
                perfil=self.perfil,
                fecha_inicio=date(2023, 1, 1),
                fecha_fin=date(2023, 1, 31)
            )


class NominaAPITests(APITestCase, NominaBaseTestCase):
    """
    Pruebas para los endpoints de la API de Nómina.
    """
    def setUp(self):
        super().setUp()
        self.client.force_authenticate(user=self.user)

    def test_crear_empleado(self):
        """
        Verifica que se pueda crear un empleado a través de la API.
        """
        url = '/api/v1/mi-negocio/nomina/empleados/'
        data = {
            'nombre': 'Maria',
            'apellido': 'Gomez',
            'tipo_documento': 'CC',
            'numero_documento': '654321',
            'fecha_nacimiento': '1995-05-10',
            'fecha_contratacion': '2023-01-01',
            'salario_base': '2500000.00'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Empleado.objects.count(), 2)

    def test_procesar_nomina_api(self):
        """
        Verifica que el endpoint de procesamiento de nómina funcione.
        """
        url = '/api/v1/mi-negocio/nomina/nominas/procesar/'
        data = {
            'fecha_inicio': '2023-02-01',
            'fecha_fin': '2023-02-28'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Nomina.objects.count(), 1)
        self.assertEqual(response.data['estado'], 'procesada')
