# backend/apps/comercial/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from apps.contabilidad.models import JournalEntry, ChartOfAccount
from .models import Cliente, FacturaVenta, PagoRecibido
import datetime

User = get_user_model()

class PagosRecibidosTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='prestador1', email='p1@test.com', password='p', role='prestador')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio 1')
        self.client.force_authenticate(user=self.user)

        ChartOfAccount.objects.create(perfil=self.perfil, code='110505', name='Caja', nature='DEBITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil, code='130505', name='CxC', nature='DEBITO', allows_transactions=True)

        cliente = Cliente.objects.create(perfil=self.perfil, nombre='Cliente de Pagos')
        self.factura = FacturaVenta.objects.create(
            perfil=self.perfil, cliente=cliente, fecha_emision=datetime.date.today(),
            fecha_vencimiento=datetime.date.today(), total=1000, estado='EMITIDA',
            created_by=self.user
        )

    def test_registrar_pago_actualiza_factura_y_contabiliza(self):
        url = reverse('mi_negocio:pagorecibido-list')
        data = { "factura": self.factura.id, "fecha_pago": datetime.date.today().isoformat(), "monto": 1000 }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.factura.refresh_from_db()
        self.assertEqual(self.factura.pagado, 1000)
        self.assertEqual(self.factura.estado, 'PAGADA')
        self.assertEqual(JournalEntry.objects.count(), 1)
