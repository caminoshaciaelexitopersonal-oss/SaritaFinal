import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import CustomUser
from apps.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.comercial.models import Producto

@pytest.mark.django_db
class TestComercialAPI(APITestCase):
    """
    Pruebas para el API del Módulo Comercial.
    """

    def setUp(self):
        self.prestador_user = CustomUser.objects.create_user(
            username="comercial_test",
            email="comercial@test.com",
            password="password123",
            role=CustomUser.Role.PRESTADOR
        )
        self.perfil = Perfil.objects.create(
            user=self.prestador_user,
            nombre_comercial="Tienda Test",
            nit="121212-1"
        )
        self.client.force_authenticate(user=self.prestador_user)

        self.productos_url = reverse('mi_negocio:producto-list')
        self.producto_data = {
            "nombre": "Tour Guiado",
            "descripcion": "Un tour por la ciudad.",
            "precio": "50000.00"
        }

    def test_crear_producto(self):
        """
        Verifica que un prestador pueda crear un producto o servicio.
        """
        response = self.client.post(self.productos_url, self.producto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 1)
        producto_creado = Producto.objects.first()
        self.assertEqual(producto_creado.perfil, self.perfil)
        self.assertEqual(producto_creado.nombre, "Tour Guiado")

    def test_listar_productos_propios(self):
        """
        Verifica que un prestador pueda listar sus propios productos.
        """
        Producto.objects.create(perfil=self.perfil, **self.producto_data)
        response = self.client.get(self.productos_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['nombre'], "Tour Guiado")

    def test_no_listar_productos_ajenos(self):
        """
        Verifica que un prestador no pueda ver los productos de otro.
        """
        otro_user = CustomUser.objects.create_user(username="otro_comercial", email="otro_c@test.com", password="password")
        otro_perfil = Perfil.objects.create(user=otro_user, nombre_comercial="Otra Tienda", nit="343434-3")
        Producto.objects.create(perfil=otro_perfil, nombre="Producto Ajeno", precio="100")

        response = self.client.get(self.productos_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)
