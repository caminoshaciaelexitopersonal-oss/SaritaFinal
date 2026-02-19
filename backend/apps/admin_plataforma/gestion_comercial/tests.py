# Tests para el módulo de gestión comercial
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from decimal import Decimal

# Importaciones de modelos necesarios para crear datos de prueba
from django.contrib.auth import get_user_model
from api.models import ProviderProfile, Company
from apps.admin_plataforma.gestion_operativa.modulos_genericos.clientes.models import Cliente
from apps.admin_plataforma.gestion_operativa.modulos_genericos.productos_servicios.models import Product
from apps.admin_plataforma.gestion_comercial.domain.models import FacturaVenta, ItemFactura

User = get_user_model()

class FacturaVentaAPITests(APITestCase):
    """
    Suite de pruebas para el API de FacturaVenta.
    Valida el ciclo de vida CRUD y las reglas de negocio clave.
    """
    def setUp(self):
        """
        Configura los datos iniciales para cada prueba.
        """
        # --- Usuario y Perfil ---
        self.company = Company.objects.create(name="Empresa de Prueba", code="TEST-COMP")
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser@example.com",
            password="testpassword",
            role="PRESTADOR"
        )
        self.profile = ProviderProfile.objects.create(
            usuario=self.user,
            company=self.company,
            nombre_comercial="Negocio de Prueba"
        )
        self.client.force_authenticate(user=self.user)

        # --- Datos Maestros ---
        self.cliente = Cliente.objects.create(
            perfil=self.profile,
            nombre="Cliente de Prueba",
            email="cliente@test.com"
        )
        self.producto = Product.objects.create(
            provider=self.profile,
            nombre="Servicio de Prueba",
            nature="servicio",
            base_price=Decimal("100.00")
        )

        # --- URLs ---
        self.list_create_url = reverse("mi_negocio:facturaventa-list")

    def test_crear_factura_caso_feliz(self):
        """
        Prueba la creación exitosa de una factura (POST).
        Verifica el código de estado, la persistencia y el cálculo de totales.
        """
        data = {
            "cliente_id": self.cliente.id,
            "number": "FV-001",
            "issue_date": "2026-01-10",
            "items": [
                {
                    "producto_id": str(self.producto.id),
                    "descripcion": "Descripción del servicio",
                    "cantidad": 2,
                    "precio_unitario": 100.00
                }
            ]
        }

        response = self.client.post(self.list_create_url, data, format='json')

        # 1. Verificar la respuesta de la API
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['number'], "FV-001")
        self.assertEqual(Decimal(response.data['total']), Decimal("200.00")) # Total calculado
        self.assertEqual(response.data['estado'], "BORRADOR") # Estado inicial

        # 2. Verificar la persistencia en la base de datos
        factura = FacturaVenta.objects.get(id=response.data['id'])
        self.assertEqual(factura.cliente, self.cliente)
        self.assertEqual(factura.total, Decimal("200.00"))
        self.assertEqual(factura.items.count(), 1)

    def test_rechazar_creacion_con_campos_calculados(self):
        """
        Prueba que la API rechaza una factura (POST) que intenta enviar campos
        calculados por el servidor, como 'total'.
        """
        data = {
            "cliente_id": self.cliente.id,
            "number": "FV-002",
            "issue_date": "2026-01-11",
            "total": "9999.99",  # Campo prohibido
            "items": [
                {
                    "producto_id": str(self.producto.id),
                    "cantidad": 1,
                    "precio_unitario": 50.00,
                    "descripcion": "test"
                }
            ]
        }

        response = self.client.post(self.list_create_url, data, format='json')

        # Verificar que la API devuelve un error de validación
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("total", response.data)
        self.assertIn("calculado por el servidor", response.data['total'][0])

    def test_listar_facturas(self):
        """
        Prueba que se puedan listar las facturas (GET) y que solo se muestren
        las que pertenecen al perfil del usuario.
        """
        # Crear una factura para este usuario
        FacturaVenta.objects.create(
            perfil=self.profile,
            cliente=self.cliente,
            number="FV-LIST-01",
            issue_date="2026-01-12",
            creado_por=self.user,
            total=100
        )

        # Crear un segundo usuario y su factura (que no debería aparecer)
        other_user = User.objects.create_user(email="other@test.com", password="pw", role="PRESTADOR")
        other_profile = ProviderProfile.objects.create(usuario=other_user, company=self.company)
        other_cliente = Cliente.objects.create(perfil=other_profile, nombre="Otro Cliente", email="other_c@test.com")
        FacturaVenta.objects.create(
            perfil=other_profile,
            cliente=other_cliente,
            number="FV-OTHER-01",
            issue_date="2026-01-12",
            creado_por=other_user,
            total=50
        )

        response = self.client.get(self.list_create_url)

        # Verificar que la respuesta es correcta y solo contiene 1 factura
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['number'], "FV-LIST-01")
