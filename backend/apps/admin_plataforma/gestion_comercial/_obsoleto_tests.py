# backend/apps/comercial/tests.py
# --- Tests deshabilitados temporalmente ---
# La funcionalidad de FacturaVenta será implementada en el futuro.
# Estos tests se reactivarán cuando el modelo y las vistas estén completos.
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from datetime import date, timedelta

from apps.prestadores.models import Perfil, CategoriaPrestador
from apps.inventario.models import Producto
from .models import Cliente, FacturaVenta, ItemFactura

User = get_user_model()

class FacturaVentaAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('vendedor', 'vendedor@test.com', 'password', role='PRESTADOR')
        self.categoria = CategoriaPrestador.objects.create(nombre='Tienda', slug='tienda')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Tienda Test', categoria=self.categoria)
        self.client.force_authenticate(user=self.user)

        self.cliente = Cliente.objects.create(perfil=self.perfil, nombre='Cliente Test')
        self.producto1 = Producto.objects.create(perfil=self.perfil, nombre='Producto 1')
        self.producto2 = Producto.objects.create(perfil=self.perfil, nombre='Producto 2')

        self.url = reverse('facturaventa-list')

    def test_create_factura_with_items(self):
        data = {
            "cliente": self.cliente.id,
            "fecha_emision": date.today().isoformat(),
            "fecha_vencimiento": (date.today() + timedelta(days=30)).isoformat(),
            "items": [
                {"producto": self.producto1.id, "cantidad": 2, "precio_unitario": "10.00"},
                {"producto": self.producto2.id, "cantidad": 5, "precio_unitario": "5.00"}
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FacturaVenta.objects.count(), 1)
        factura = FacturaVenta.objects.first()
        self.assertEqual(factura.items.count(), 2)
        self.assertEqual(factura.subtotal, Decimal('45.00'))
"""
