# backend/apps/comercial/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from .models import Cliente, FacturaVenta, ItemFactura
import datetime

User = get_user_model()

class ComercialAPITests(APITestCase):

    def setUp(self):
        self.user_prestador_1 = User.objects.create_user(username='prestador1', email='p1@test.com', password='password123', role='prestador')
        self.perfil_1 = Perfil.objects.create(usuario=self.user_prestador_1, nombre_comercial='Negocio 1')

        self.user_prestador_2 = User.objects.create_user(username='prestador2', email='p2@test.com', password='password123', role='prestador')
        self.perfil_2 = Perfil.objects.create(usuario=self.user_prestador_2, nombre_comercial='Negocio 2')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user_prestador_1)

    def test_create_cliente(self):
        """Prueba la creación de un cliente."""
        url = reverse('mi_negocio:cliente-list')
        data = {'nombre': 'Cliente de Prueba'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.filter(perfil=self.perfil_1).count(), 1)

    def test_list_cliente_isolated(self):
        """Prueba el listado aislado de clientes."""
        # Limpieza explícita
        Cliente.objects.all().delete()

        # Crear 1 cliente para el perfil 1
        Cliente.objects.create(perfil=self.perfil_1, nombre='Mi Cliente')
        # Crear 1 cliente para el perfil 2 (no debe aparecer)
        Cliente.objects.create(perfil=self.perfil_2, nombre='Cliente Ajeno')

        url = reverse('mi_negocio:cliente-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'Mi Cliente')

    def test_create_factura_venta(self):
        """Prueba la creación de una factura de venta con items."""
        cliente = Cliente.objects.create(perfil=self.perfil_1, nombre='Cliente para Factura')
        url = reverse('mi_negocio:facturaventa-list')
        data = {
            "cliente": cliente.id,
            "fecha_emision": datetime.date.today().isoformat(),
            "fecha_vencimiento": (datetime.date.today() + datetime.timedelta(days=30)).isoformat(),
            "items": [
                {"descripcion": "Producto 1", "cantidad": "2.00", "precio_unitario": "100.00"},
                {"descripcion": "Producto 2", "cantidad": "1.00", "precio_unitario": "50.00"}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FacturaVenta.objects.count(), 1)
        factura = FacturaVenta.objects.first()
        self.assertEqual(factura.items.count(), 2)
        self.assertEqual(factura.total, 297.50) # (200 + 50) * 1.19

    def test_cannot_use_other_perfil_cliente(self):
        """Asegura que no se pueda facturar a un cliente de otro perfil."""
        cliente_ajeno = Cliente.objects.create(perfil=self.perfil_2, nombre='Cliente Ajeno')
        url = reverse('mi_negocio:facturaventa-list')
        data = {
            "cliente": cliente_ajeno.id,
            "fecha_emision": "2024-10-28",
            "fecha_vencimiento": "2024-11-28",
            "items": [{"descripcion": "Item", "cantidad": "1.00", "precio_unitario": "10.00"}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
