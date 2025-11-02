import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import CustomUser
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil, CategoriaPrestador
from apps.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente

@pytest.mark.django_db
class TestClienteAPI(APITestCase):
    """
    Pruebas para el API de Clientes en el panel "Mi Negocio".
    """

    def setUp(self):
        """
        Configura el entorno de prueba creando un usuario prestador,
        su perfil y un cliente asociado.
        """
        # 1. Crear usuario PRESTADOR
        self.prestador_user = CustomUser.objects.create_user(
            username="prestador_test",
            email="prestador@test.com",
            password="password123",
            role=CustomUser.Role.PRESTADOR
        )

        # 2. Crear una categoría para el perfil
        self.categoria = CategoriaPrestador.objects.create(nombre="Alojamiento Rural")

        # 3. Crear el perfil del prestador
        self.perfil = Perfil.objects.create(
            user=self.prestador_user,
            nombre_comercial="Finca El Descanso",
            nit="123456789-1",
            razon_social="Finca El Descanso S.A.S",
            categoria=self.categoria
        )

        # 4. Autenticar al cliente de pruebas
        self.client.force_authenticate(user=self.prestador_user)

        # 5. Datos para un nuevo cliente
        self.cliente_data = {
            "nombre": "Juan Pérez",
            "email": "juan.perez@email.com",
            "telefono": "3101234567"
        }

        # URLs de la API
        self.list_create_url = reverse('mi_negocio:cliente-list')

    def test_crear_cliente(self):
        """
        Verifica que un prestador autenticado pueda crear un nuevo cliente.
        """
        response = self.client.post(self.list_create_url, self.cliente_data, format='json')

        # Verificar que la respuesta sea 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar que el cliente se creó en la base de datos
        self.assertEqual(Cliente.objects.count(), 1)

        # Verificar que el cliente está asociado al perfil correcto
        cliente_creado = Cliente.objects.first()
        self.assertEqual(cliente_creado.perfil, self.perfil)
        self.assertEqual(cliente_creado.nombre, "Juan Pérez")

    def test_listar_clientes(self):
        """
        Verifica que un prestador pueda listar sus propios clientes.
        """
        # Crear un cliente de prueba para el prestador
        Cliente.objects.create(perfil=self.perfil, nombre="Cliente de Prueba")

        response = self.client.get(self.list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # La respuesta debe contener 1 cliente
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['nombre'], "Cliente de Prueba")

    def test_no_listar_clientes_de_otros_prestadores(self):
        """
        Verifica que un prestador no pueda ver los clientes de otro.
        """
        # Crear un segundo prestador y un cliente para él
        otro_prestador_user = CustomUser.objects.create_user(username="otro_test", email="otro@test.com", password="password")
        otro_perfil = Perfil.objects.create(user=otro_prestador_user, nombre_comercial="Otro Negocio", nit="987654321-0")
        Cliente.objects.create(perfil=otro_perfil, nombre="Cliente Ajeno")

        response = self.client.get(self.list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # La lista debe estar vacía, ya que el prestador autenticado no tiene clientes
        self.assertEqual(len(response.data['results']), 0)

    def test_ver_detalle_cliente(self):
        """
        Verifica que un prestador pueda ver el detalle de uno de sus clientes.
        """
        cliente = Cliente.objects.create(perfil=self.perfil, **self.cliente_data)
        detail_url = reverse('mi_negocio:cliente-detail', kwargs={'pk': cliente.pk})

        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.cliente_data['nombre'])

    def test_actualizar_cliente(self):
        """
        Verifica que un prestador pueda actualizar los datos de su cliente.
        """
        cliente = Cliente.objects.create(perfil=self.perfil, **self.cliente_data)
        detail_url = reverse('mi_negocio:cliente-detail', kwargs={'pk': cliente.pk})

        payload_actualizacion = {"nombre": "Juan Pérez Actualizado"}
        response = self.client.patch(detail_url, payload_actualizacion, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refrescar el objeto desde la BD y verificar el cambio
        cliente.refresh_from_db()
        self.assertEqual(cliente.nombre, "Juan Pérez Actualizado")

    def test_eliminar_cliente(self):
        """
        Verifica que un prestador pueda eliminar a uno de sus clientes.
        """
        cliente = Cliente.objects.create(perfil=self.perfil, **self.cliente_data)
        self.assertEqual(Cliente.objects.count(), 1)

        detail_url = reverse('mi_negocio:cliente-detail', kwargs={'pk': cliente.pk})
        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)

    def test_no_se_puede_acceder_a_cliente_ajeno(self):
        """
        Verifica que un prestador reciba un error 404 si intenta acceder
        al detalle de un cliente que no le pertenece.
        """
        # Crear un cliente ajeno
        otro_prestador_user = CustomUser.objects.create_user(username="otro_test_2", email="otro2@test.com", password="password")
        otro_perfil = Perfil.objects.create(user=otro_prestador_user, nombre_comercial="Otro Negocio 2", nit="987654321-1")
        cliente_ajeno = Cliente.objects.create(perfil=otro_perfil, nombre="Cliente Ajeno")

        detail_url_ajeno = reverse('mi_negocio:cliente-detail', kwargs={'pk': cliente_ajeno.pk})

        # Intentar GET, PATCH, DELETE
        response_get = self.client.get(detail_url_ajeno)
        response_patch = self.client.patch(detail_url_ajeno, {"nombre": "Intento de hack"})
        response_delete = self.client.delete(detail_url_ajeno)

        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response_patch.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response_delete.status_code, status.HTTP_404_NOT_FOUND)
