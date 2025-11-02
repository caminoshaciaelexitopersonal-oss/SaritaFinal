import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import CustomUser
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil, CategoriaPrestador
from apps.contabilidad.models import ChartOfAccount

@pytest.mark.django_db
class TestContabilidadAPI(APITestCase):
    """
    Pruebas para el API de Contabilidad en el panel "Mi Negocio".
    """

    def setUp(self):
        """
        Configura el entorno de prueba creando un usuario prestador y su perfil.
        """
        self.prestador_user = CustomUser.objects.create_user(
            username="contador_test",
            email="contador@test.com",
            password="password123",
            role=CustomUser.Role.PRESTADOR
        )
        self.categoria = CategoriaPrestador.objects.create(nombre="Servicios Contables")
        self.perfil = Perfil.objects.create(
            user=self.prestador_user,
            nombre_comercial="Contadores Asociados",
            nit="1122334455-6",
            razon_social="Contadores S.A.S",
            categoria=self.categoria
        )
        self.client.force_authenticate(user=self.prestador_user)

        self.puc_list_create_url = reverse('mi_negocio:plan-de-cuentas-list')
        self.cuenta_data = {
            "codigo": "110505",
            "nombre": "Caja General",
            "naturaleza": "DEBITO",
            "permite_transacciones": True
        }

    def test_crear_cuenta_contable(self):
        """
        Verifica que un prestador pueda crear una cuenta en su plan de cuentas.
        """
        response = self.client.post(self.puc_list_create_url, self.cuenta_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChartOfAccount.objects.count(), 1)
        cuenta_creada = ChartOfAccount.objects.first()
        self.assertEqual(cuenta_creada.perfil, self.perfil)
        self.assertEqual(cuenta_creada.nombre, "Caja General")

    def test_listar_cuentas_propias(self):
        """
        Verifica que un prestador pueda listar sus propias cuentas contables.
        """
        ChartOfAccount.objects.create(perfil=self.perfil, **self.cuenta_data)
        response = self.client.get(self.puc_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['nombre'], "Caja General")

    def test_no_listar_cuentas_ajenas(self):
        """
        Verifica que un prestador no pueda ver las cuentas de otro.
        """
        otro_user = CustomUser.objects.create_user(username="otro", email="otro@test.com", password="password")
        otro_perfil = Perfil.objects.create(user=otro_user, nombre_comercial="Otra Empresa", nit="000")
        ChartOfAccount.objects.create(perfil=otro_perfil, codigo="999", nombre="Cuenta Ajena", naturaleza="DEBITO")

        response = self.client.get(self.puc_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)
