import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import CustomUser
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil, CategoriaPrestador
from apps.contabilidad.models import ChartOfAccount
from apps.financiero.models import BankAccount

@pytest.mark.django_db
class TestFinancieraAPI(APITestCase):
    """
    Pruebas para el API del Módulo Financiero.
    """

    def setUp(self):
        self.prestador_user = CustomUser.objects.create_user(
            username="financiero_test",
            email="financiero@test.com",
            password="password123",
            role=CustomUser.Role.PRESTADOR
        )
        self.perfil = Perfil.objects.create(
            user=self.prestador_user,
            nombre_comercial="Tesoreria Test",
            nit="55667788-9"
        )
        self.client.force_authenticate(user=self.prestador_user)

        self.cuenta_contable = ChartOfAccount.objects.create(
            perfil=self.perfil,
            codigo="111005",
            nombre="Bancos Nacionales",
            naturaleza="DEBITO"
        )
        self.cuentas_url = reverse('mi_negocio:cuenta-bancaria-list')
        self.cuenta_bancaria_data = {
            "nombre": "Cuenta Principal",
            "numero_cuenta": "123-456-789",
            "nombre_banco": "Banco Ejemplo",
            "cuenta_contable_asociada": self.cuenta_contable.pk
        }

    def test_crear_cuenta_bancaria(self):
        """
        Verifica que un prestador pueda crear una cuenta bancaria.
        """
        response = self.client.post(self.cuentas_url, self.cuenta_bancaria_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BankAccount.objects.count(), 1)
        cuenta_creada = BankAccount.objects.first()
        self.assertEqual(cuenta_creada.perfil, self.perfil)
        self.assertEqual(cuenta_creada.nombre, "Cuenta Principal")

    def test_listar_cuentas_bancarias_propias(self):
        """
        Verifica que un prestador pueda listar sus propias cuentas bancarias.
        """
        data = self.cuenta_bancaria_data.copy()
        data['cuenta_contable_asociada'] = self.cuenta_contable
        BankAccount.objects.create(perfil=self.perfil, **data)
        response = self.client.get(self.cuentas_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['nombre'], "Cuenta Principal")

    def test_no_listar_cuentas_bancarias_ajenas(self):
        """
        Verifica que un prestador no pueda ver las cuentas de otro.
        """
        otro_user = CustomUser.objects.create_user(username="otro_financiero", email="otro_f@test.com", password="password")
        otro_perfil = Perfil.objects.create(user=otro_user, nombre_comercial="Otra Tesoreria", nit="999")
        # Necesita su propia cuenta contable
        otra_cuenta_contable = ChartOfAccount.objects.create(perfil=otro_perfil, codigo="111005", nombre="Bancos Otros", naturaleza="DEBITO")
        BankAccount.objects.create(perfil=otro_perfil, nombre="Cuenta Ajena", numero_cuenta="000", nombre_banco="Otro Banco", cuenta_contable_asociada=otra_cuenta_contable)

        response = self.client.get(self.cuentas_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)
