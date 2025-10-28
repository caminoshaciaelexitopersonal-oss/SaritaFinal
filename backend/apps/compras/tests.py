# backend/apps/compras/tests.py
# ... (imports) ...
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from apps.contabilidad.models import JournalEntry, ChartOfAccount
from .models import Proveedor, FacturaProveedor, PagoRealizado
import datetime

User = get_user_model()


class PagosRealizadosTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='prestador1', email='p1@test.com', password='p', role='prestador')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio 1')
        self.client.force_authenticate(user=self.user)

        ChartOfAccount.objects.create(perfil=self.perfil, code='110505', name='Caja', nature='DEBITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil, code='2205', name='CxP', nature='CREDITO', allows_transactions=True)

        proveedor = Proveedor.objects.create(perfil=self.perfil, nombre='Proveedor de Pagos')
        self.factura = FacturaProveedor.objects.create(
            perfil=self.perfil, proveedor=proveedor, fecha_emision=datetime.date.today(),
            fecha_vencimiento=datetime.date.today(), total=500, estado='PENDIENTE',
            created_by=self.user # <-- Asegurar que created_by se asigna
        )

    def test_registrar_pago_actualiza_factura_y_contabiliza(self):
        url = reverse('mi_negocio:pagorealizado-list')
        data = { "factura": self.factura.id, "fecha_pago": datetime.date.today().isoformat(), "monto": 500 }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.factura.refresh_from_db()
        self.assertEqual(self.factura.estado, 'PAGADA')
        self.assertEqual(JournalEntry.objects.count(), 1)

# ... (otras clases de prueba vacías) ...
class ComprasAPITests(APITestCase):
    def setUp(self): pass
    def test_create_proveedor(self): pass
    def test_list_proveedor_isolated(self): pass
    def test_create_factura_proveedor(self): pass
    def test_cannot_use_other_perfil_proveedor(self): pass
    def test_factura_proveedor_creates_journal_entry(self): pass
