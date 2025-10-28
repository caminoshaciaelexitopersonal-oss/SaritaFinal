# backend/apps/compras/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from .models import Proveedor, FacturaProveedor
import datetime

User = get_user_model()

class ComprasAPITests(APITestCase):

    def setUp(self):
        self.user_prestador_1 = User.objects.create_user(username='prestador1', email='p1@test.com', password='password123', role='prestador')
        self.perfil_1 = Perfil.objects.create(usuario=self.user_prestador_1, nombre_comercial='Negocio 1')

        self.user_prestador_2 = User.objects.create_user(username='prestador2', email='p2@test.com', password='password123', role='prestador')
        self.perfil_2 = Perfil.objects.create(usuario=self.user_prestador_2, nombre_comercial='Negocio 2')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user_prestador_1)

    def test_create_proveedor(self):
        url = reverse('mi_negocio:proveedor-list')
        data = {'nombre': 'Proveedor de Prueba'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Proveedor.objects.filter(perfil=self.perfil_1).count(), 1)

    def test_list_proveedor_isolated(self):
        Proveedor.objects.all().delete() # Limpieza
        Proveedor.objects.create(perfil=self.perfil_1, nombre='Mi Proveedor')
        Proveedor.objects.create(perfil=self.perfil_2, nombre='Proveedor Ajeno')

        url = reverse('mi_negocio:proveedor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'Mi Proveedor')

    def test_create_factura_proveedor(self):
        proveedor = Proveedor.objects.create(perfil=self.perfil_1, nombre='Proveedor para Factura')
        url = reverse('mi_negocio:facturaproveedor-list')
        data = {
            "proveedor": proveedor.id,
            "fecha_emision": datetime.date.today().isoformat(),
            "fecha_vencimiento": (datetime.date.today() + datetime.timedelta(days=30)).isoformat(),
            "total": "1500.00",
            "items": [
                {"descripcion": "Insumo 1", "cantidad": "10.00", "costo_unitario": "150.00"}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FacturaProveedor.objects.count(), 1)

    def test_cannot_use_other_perfil_proveedor(self):
        proveedor_ajeno = Proveedor.objects.create(perfil=self.perfil_2, nombre='Proveedor Ajeno')
        url = reverse('mi_negocio:facturaproveedor-list')
        data = {
            "proveedor": proveedor_ajeno.id,
            "fecha_emision": "2024-10-28",
            "fecha_vencimiento": "2024-11-28",
            "total": "100.00",
            "items": []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
