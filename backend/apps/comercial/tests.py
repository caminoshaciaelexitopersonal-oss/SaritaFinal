# backend/apps/comercial/tests.py
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
        # Crear usuario y perfil
        self.user = User.objects.create_user(
            username='prestador_ventas',
            email='ventas@test.com',
            password='password123',
            role='PRESTADOR'
        )
        self.categoria = CategoriaPrestador.objects.create(nombre='Tienda', slug='tienda')
        self.perfil = Perfil.objects.create(
            usuario=self.user,
            nombre_comercial='Tienda de Prueba',
            categoria=self.categoria
        )
        self.client.force_authenticate(user=self.user)

        # Crear datos de prueba
        self.cliente = Cliente.objects.create(perfil=self.perfil, nombre='Cliente de Facturación')
        self.producto1 = Producto.objects.create(
            perfil=self.perfil,
            nombre='Producto A',
            costo_promedio_ponderado=Decimal('70.00'),
            cantidad_en_stock=Decimal('10')
        )
        self.producto2 = Producto.objects.create(
            perfil=self.perfil,
            nombre='Producto B',
            costo_promedio_ponderado=Decimal('35.00'),
            cantidad_en_stock=Decimal('20')
        )

        self.url = reverse('mi_negocio:facturaventa-list')

    def test_create_factura_with_items(self):
        """
        Verifica que se pueda crear una factura de venta con sus ítems anidados
        en una sola petición a la API.
        """
        data = {
            "cliente": self.cliente.id,
            "fecha_emision": date.today().isoformat(),
            "fecha_vencimiento": (date.today() + timedelta(days=30)).isoformat(),
            "estado": "BORRADOR",
            "items": [
                {
                    "producto": self.producto1.id,
                    "cantidad": 2,
                    "precio_unitario": "100.00"
                },
                {
                    "producto": self.producto2.id,
                    "cantidad": 3,
                    "precio_unitario": "50.00"
                }
            ]
        }

        response = self.client.post(self.url, data, format='json')

        # Verificar respuesta
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar creación en la base de datos
        self.assertEqual(FacturaVenta.objects.count(), 1)
        self.assertEqual(ItemFactura.objects.count(), 2)

        factura = FacturaVenta.objects.first()
        self.assertEqual(factura.items.count(), 2)

        # Verificar cálculos
        subtotal_esperado = (2 * Decimal('100.00')) + (3 * Decimal('50.00'))
        self.assertEqual(factura.subtotal, subtotal_esperado)
        self.assertEqual(factura.total, subtotal_esperado) # Asumiendo 0 impuestos por ahora
