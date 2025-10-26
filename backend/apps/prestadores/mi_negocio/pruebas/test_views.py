# SaritaUnificado/backend/apps/prestadores/mi_negocio/pruebas/test_views.py
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import CustomUser
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil, CategoriaPrestador

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_prestador_user():
    def _create_user(username, password='password123'):
        user = CustomUser.objects.create_user(username=username, email=f'{username}@test.com', password=password, role='PRESTADOR')
        categoria, _ = CategoriaPrestador.objects.get_or_create(nombre='Hotel Test', defaults={'slug': 'hotel-test'})
        Perfil.objects.create(usuario=user, nombre_comercial=f'Hotel {username}', categoria=categoria)
        return user
    return _create_user

@pytest.mark.django_db
class TestProductoServicioViewSet:
    def test_unauthenticated_user_cannot_access(self, api_client):
        url = reverse('mi_negocio:producto-servicio-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_prestador_can_create_producto(self, api_client, create_prestador_user):
        user = create_prestador_user('prestador1')
        api_client.force_authenticate(user=user)

        url = reverse('mi_negocio:producto-servicio-list')
        data = {
            'nombre': 'Habitación Doble',
            'precio': 150000,
            'tipo': 'SERVICIO'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['nombre'] == 'Habitación Doble'
        assert user.perfil_prestador.productos_servicios.count() == 1

    def test_prestador_can_only_see_own_productos(self, api_client, create_prestador_user):
        # Usuario 1 y su producto
        user1 = create_prestador_user('prestador1')
        api_client.force_authenticate(user=user1)
        url = reverse('mi_negocio:producto-servicio-list')
        api_client.post(url, {'nombre': 'Producto de User1', 'precio': 100, 'tipo': 'PRODUCTO'})

        # Usuario 2 y su producto
        user2 = create_prestador_user('prestador2')
        api_client.force_authenticate(user=user2)
        api_client.post(url, {'nombre': 'Producto de User2', 'precio': 200, 'tipo': 'PRODUCTO'})

        # Verificamos que el Usuario 2 solo ve su producto
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['nombre'] == 'Producto de User2'

        # Verificamos que el Usuario 1 solo ve su producto
        api_client.force_authenticate(user=user1)
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['nombre'] == 'Producto de User1'
