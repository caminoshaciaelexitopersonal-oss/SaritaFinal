from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from datetime import date, timedelta
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil, CategoriaPrestador
from .models import Empleado, ConceptoNomina, Nomina
from .services import procesar_nomina_service

User = get_user_model()

class NominaBaseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('prestador', 'prestador@test.com', 'password123', role='PRESTADOR')
        self.categoria = CategoriaPrestador.objects.create(nombre='Hotel', slug='hotel')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Hotel Sarita', categoria=self.categoria)
        self.client.force_authenticate(user=self.user)
        self.empleado = Empleado.objects.create(perfil=self.perfil, nombre='Juan', apellido='Perez', tipo_documento='CC', numero_documento='123456', fecha_nacimiento=date(1990,1,1), fecha_contratacion=date(2022,1,1), salario_base=Decimal('2000000.00'), activo=True)
        self.concepto_bono = ConceptoNomina.objects.create(codigo='BONO', tipo='ingreso', es_fijo=True, valor=Decimal('100000.00'))
        self.concepto_salud = ConceptoNomina.objects.create(codigo='SALUD', tipo='deduccion', es_fijo=False, valor=Decimal('0.04'))

class NominaServiceTests(NominaBaseTestCase):
    def test_procesar_nomina_correctamente(self):
        nomina = procesar_nomina_service(self.perfil, date(2023,1,1), date(2023,1,31))
        self.assertIsNotNone(nomina)
        total_ingresos = self.empleado.salario_base + self.concepto_bono.valor
        total_deducciones = self.empleado.salario_base * self.concepto_salud.valor
        self.assertEqual(nomina.total_ingresos, total_ingresos)
        self.assertEqual(nomina.total_deducciones, total_deducciones)

class NominaAPITests(NominaBaseTestCase):
    def test_crear_empleado(self):
        url = reverse('mi_negocio:empleado-list')
        data = {'nombre': 'Maria', 'apellido': 'Gomez', 'tipo_documento': 'CC', 'numero_documento': '654321', 'fecha_nacimiento': '1995-05-10', 'fecha_contratacion': '2023-01-01', 'salario_base': '2500000.00'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Empleado.objects.count(), 2)

    def test_procesar_nomina_api(self):
        url = reverse('mi_negocio:nomina-procesar')
        data = {'fecha_inicio': '2023-02-01', 'fecha_fin': '2023-02-28'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Nomina.objects.count(), 1)
