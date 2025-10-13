from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import CustomUser, SiteConfiguration, MenuItem
from core.auth.jwt_utils import generate_jwt_for_user

class SiteConfigurationAPITests(APITestCase):
    """
    Pruebas para el endpoint de SiteConfiguration.
    Verifica que la lectura sea pública y la escritura restringida a Admins.
    """
    def setUp(self):
        # Crear usuarios con diferentes roles
        self.admin_user = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'password123')
        self.funcionario_user = CustomUser.objects.create_user('funcionario', 'func@example.com', 'password123', role=CustomUser.Role.FUNCIONARIO_DIRECTIVO)
        self.turista_user = CustomUser.objects.create_user('turista', 'turista@example.com', 'password123', role=CustomUser.Role.TURISTA)

        # Generar tokens JWT para autenticación
        self.admin_token = generate_jwt_for_user(self.admin_user)
        self.funcionario_token = generate_jwt_for_user(self.funcionario_user)
        self.turista_token = generate_jwt_for_user(self.turista_user)

        # Cargar la configuración inicial
        self.config = SiteConfiguration.load()
        self.url = reverse('site-configuration')

    def _get_auth_header(self, token_data):
        return {'HTTP_AUTHORIZATION': f'Bearer {token_data["access"]}'}

    def test_get_config_is_public(self):
        """Cualquier usuario, incluso no autenticado, puede ver la configuración."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('direccion', response.data)

    def test_update_config_as_admin(self):
        """Un admin PUEDE actualizar la configuración."""
        data = {'direccion': 'Nueva Calle 123'}
        self.client.credentials(**self._get_auth_header(self.admin_token))
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.config.refresh_from_db()
        self.assertEqual(self.config.direccion, 'Nueva Calle 123')

    def test_update_config_as_funcionario_is_forbidden(self):
        """Un funcionario NO PUEDE actualizar la configuración."""
        data = {'direccion': 'Calle Prohibida'}
        self.client.credentials(**self._get_auth_header(self.funcionario_token))
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_config_as_turista_is_forbidden(self):
        """Un turista NO PUEDE actualizar la configuración."""
        data = {'direccion': 'Calle Prohibida'}
        self.client.credentials(**self._get_auth_header(self.turista_token))
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MenuItemAPITests(APITestCase):
    """
    Pruebas para el ViewSet de MenuItem.
    Verifica que la lectura sea pública y la escritura restringida a Admins.
    """
    def setUp(self):
        self.admin_user = CustomUser.objects.create_superuser('admin', 'admin@example.com', 'password123')
        self.funcionario_user = CustomUser.objects.create_user('funcionario', 'func@example.com', 'password123', role=CustomUser.Role.FUNCIONARIO_DIRECTIVO)

        self.admin_token = generate_jwt_for_user(self.admin_user)
        self.funcionario_token = generate_jwt_for_user(self.funcionario_user)

        # Crear elementos de menú para probar
        self.parent_item = MenuItem.objects.create(nombre='Quienes Somos', url='/quienes-somos', orden=1)
        self.child_item = MenuItem.objects.create(nombre='Historia', url='/historia', parent=self.parent_item, orden=1)

        self.list_url = reverse('admin-menu-items-list')
        self.detail_url = reverse('admin-menu-items-detail', kwargs={'pk': self.parent_item.pk})
        self.reorder_url = reverse('admin-menu-items-reorder')

    def _get_auth_header(self, token_data):
        return {'HTTP_AUTHORIZATION': f'Bearer {token_data["access"]}'}

    def test_list_menu_items_is_public(self):
        """Cualquier usuario puede listar los elementos del menú (solo los padres)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'Quienes Somos')
        self.assertEqual(len(response.data[0]['children']), 1)

    def test_create_menu_item_as_admin(self):
        """Un admin PUEDE crear un elemento de menú."""
        data = {'nombre': 'Contacto', 'url': '/contacto', 'orden': 2}
        self.client.credentials(**self._get_auth_header(self.admin_token))
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 3)

    def test_create_menu_item_as_funcionario_is_forbidden(self):
        """Un funcionario NO PUEDE crear un elemento de menú."""
        data = {'nombre': 'Contacto', 'url': '/contacto', 'orden': 2}
        self.client.credentials(**self._get_auth_header(self.funcionario_token))
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_menu_item_as_admin(self):
        """Un admin PUEDE actualizar un elemento de menú."""
        data = {'nombre': 'Sobre Nosotros'}
        self.client.credentials(**self._get_auth_header(self.admin_token))
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.parent_item.refresh_from_db()
        self.assertEqual(self.parent_item.nombre, 'Sobre Nosotros')

    def test_delete_menu_item_as_admin(self):
        """Un admin PUEDE eliminar un elemento de menú."""
        self.client.credentials(**self._get_auth_header(self.admin_token))
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Al eliminar el padre, también se elimina el hijo (por on_delete=models.CASCADE)
        self.assertEqual(MenuItem.objects.count(), 0)
