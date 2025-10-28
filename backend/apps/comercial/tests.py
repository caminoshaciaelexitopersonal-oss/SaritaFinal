# backend/apps/comercial/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from apps.contabilidad.models import JournalEntry, ChartOfAccount
from .models import Cliente, FacturaVenta
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

        # Cuentas para contabilización automática
        ChartOfAccount.objects.create(perfil=self.perfil_1, code='130505', name='Cuentas por Cobrar', nature='DEBITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil_1, code='4135', name='Ingresos', nature='CREDITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil_1, code='2408', name='IVA Generado', nature='CREDITO', allows_transactions=True)

    def test_factura_venta_creates_journal_entry(self):
        """Prueba que una FacturaVenta emitida cree su asiento contable."""
        cliente = Cliente.objects.create(perfil=self.perfil_1, nombre='Cliente Contable')
        factura = FacturaVenta.objects.create(
            perfil=self.perfil_1,
            cliente=cliente,
            fecha_emision=datetime.date.today(),
            fecha_vencimiento=datetime.date.today(),
            subtotal=1000,
            impuestos=190,
            total=1190,
            estado='EMITIDA',
            created_by=self.user_prestador_1
        )

        # La señal post_save debería haber creado un JournalEntry
        self.assertEqual(JournalEntry.objects.count(), 1)
        entry = JournalEntry.objects.first()
        self.assertEqual(entry.perfil, self.perfil_1)
        self.assertEqual(entry.transactions.count(), 3)
        self.assertEqual(entry.origin_document, factura)

    # ... (resto de las pruebas)
    def test_create_cliente(self):
        url = reverse('mi_negocio:cliente-list')
        data = {'nombre': 'Cliente de Prueba'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_cliente_isolated(self):
        Cliente.objects.all().delete()
        Cliente.objects.create(perfil=self.perfil_1, nombre='Mi Cliente')
        Cliente.objects.create(perfil=self.perfil_2, nombre='Cliente Ajeno')
        url = reverse('mi_negocio:cliente-list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    def test_create_factura_venta(self):
        cliente = Cliente.objects.create(perfil=self.perfil_1, nombre='Cliente para Factura')
        url = reverse('mi_negocio:facturaventa-list')
        data = { "cliente": cliente.id, "fecha_emision": "2024-10-28", "fecha_vencimiento": "2024-11-28", "items": [] }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_use_other_perfil_cliente(self):
        cliente_ajeno = Cliente.objects.create(perfil=self.perfil_2, nombre='Cliente Ajeno')
        url = reverse('mi_negocio:facturaventa-list')
        data = { "cliente": cliente_ajeno.id, "fecha_emision": "2024-10-28", "fecha_vencimiento": "2024-11-28", "items": [] }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
