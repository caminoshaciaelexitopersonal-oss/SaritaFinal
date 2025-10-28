# backend/apps/contabilidad/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import Decimal
from django.contrib.auth import get_user_model
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.contabilidad.models import ChartOfAccount, JournalEntry, Transaction, CostCenter

User = get_user_model()

class CostCenterAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', role='PRESTADOR')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio de Prueba')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('mi_negocio:contabilidad_api:costcenter-list')

    def test_create_and_list_cost_center(self):
        # Probar creación
        data = {'code': 'C01', 'name': 'Administración'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CostCenter.objects.filter(perfil=self.perfil).count(), 1)

        # Crear otro para un perfil diferente
        other_user = User.objects.create_user(username='other', password='pw', role='PRESTADOR')
        other_perfil = Perfil.objects.create(usuario=other_user, nombre_comercial='Otro')
        CostCenter.objects.create(perfil=other_perfil, code='C02', name='Ventas Otro')

        # Probar listado aislado
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Administración')

class JournalEntryAPITests(APITestCase):
    """
    Suite de pruebas para el endpoint de Asientos Contables.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', role='PRESTADOR')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio de Prueba')
        self.client.force_authenticate(user=self.user)

        self.cash_account = ChartOfAccount.objects.create(perfil=self.perfil, code='110505', name='Caja', nature='DEBITO', allows_transactions=True)
        self.sales_account = ChartOfAccount.objects.create(perfil=self.perfil, code='413501', name='Ingresos', nature='CREDITO', allows_transactions=True)
        self.control_account = ChartOfAccount.objects.create(perfil=self.perfil, code='1000', name='Activo Control', nature='DEBITO', allows_transactions=False)
        self.cost_center = CostCenter.objects.create(perfil=self.perfil, code='C01', name='Ventas')

    def test_create_valid_journal_entry_with_cost_center(self):
        """Prueba crear un asiento válido asignando un centro de costo."""
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Venta con CC", "entry_type": "Ingreso",
            "transactions": [
                {"account_code": "110505", "debit": "1190.00", "cost_center_code": "C01"},
                {"account_code": "413501", "credit": "1190.00", "cost_center_code": "C01"}
            ]
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.first().cost_center, self.cost_center)

    # ... (resto de las pruebas de JournalEntryAPITests sin cambios) ...
    def test_create_valid_journal_entry(self):
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Venta de prueba", "entry_type": "Ingreso",
            "transactions": [
                {"account_code": "110505", "debit": "1190.00", "credit": 0},
                {"account_code": "413501", "debit": 0, "credit": "1190.00"}
            ]
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_unbalanced_journal_entry_fails(self):
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Intento fallido", "entry_type": "Error",
            "transactions": [
                {"account_code": "110505", "debit": "1000.00"},
                {"account_code": "413501", "credit": "999.99"}
            ]
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_entry_on_control_account_fails(self):
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Intento fallido", "entry_type": "Error",
            "transactions": [
                {"account_code": "1000", "debit": "1000.00"},
                {"account_code": "413501", "credit": "1000.00"}
            ]
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_access_other_perfil_data(self):
        other_user = User.objects.create_user(username='otheruser', password='password', role='PRESTADOR')
        other_perfil = Perfil.objects.create(usuario=other_user, nombre_comercial='Otro Negocio')
        other_account = ChartOfAccount.objects.create(perfil=other_perfil, code='9999', name='Cuenta Ajena', nature='DEBITO', allows_transactions=True)
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Intento de fraude", "entry_type": "Error",
            "transactions": [
                {"account_code": "9999", "debit": "100.00"},
                {"account_code": "413501", "credit": "100.00"}
            ]
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
