# backend/apps/financiera/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from .models import BankAccount, CashTransaction

User = get_user_model()

class FinancieraAPITests(APITestCase):

    def setUp(self):
        """Configuración limpia, solo usuarios y perfiles base."""
        self.user_prestador_1 = User.objects.create_user(username='prestador1', email='p1@test.com', password='password123', role='prestador')
        self.perfil_1 = Perfil.objects.create(usuario=self.user_prestador_1, nombre_comercial='Negocio 1')

        self.user_prestador_2 = User.objects.create_user(username='prestador2', email='p2@test.com', password='password123', role='prestador')
        self.perfil_2 = Perfil.objects.create(usuario=self.user_prestador_2, nombre_comercial='Negocio 2')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user_prestador_1)

        self.bank_accounts_url = reverse('mi_negocio:bankaccount-list')
        self.cash_transactions_url = reverse('mi_negocio:cashtransaction-list')

    def test_create_bank_account(self):
        """Verifica que un usuario pueda crear una cuenta bancaria para su perfil."""
        initial_count = BankAccount.objects.filter(perfil=self.perfil_1).count()
        data = {
            'bank_name': 'Banco Nuevo',
            'account_number': '456',
            'account_holder': 'Negocio 1 SAS', # Campo obligatorio añadido
            'account_type': 'CHECKING'
        }
        response = self.client.post(self.bank_accounts_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BankAccount.objects.filter(perfil=self.perfil_1).count(), initial_count + 1)

    def test_list_bank_accounts_isolates_data(self):
        """Verifica que un usuario solo vea sus propias cuentas bancarias."""
        # Limpieza explícita para forzar el aislamiento
        BankAccount.objects.all().delete()

        # Se crea 1 cuenta para el usuario autenticado
        BankAccount.objects.create(perfil=self.perfil_1, bank_name='Banco Local', account_number='123', account_holder='Negocio 1', account_type='SAVINGS')
        # Se crea 1 cuenta para otro usuario (no debe aparecer)
        BankAccount.objects.create(perfil=self.perfil_2, bank_name='Banco Ajeno', account_number='999', account_holder='Negocio 2', account_type='SAVINGS')

        response = self.client.get(self.bank_accounts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['account_number'], '123')

    def test_create_cash_transaction(self):
        """Verifica la creación de una transacción de caja para una cuenta propia."""
        bank_account = BankAccount.objects.create(perfil=self.perfil_1, bank_name='Banco Local', account_number='123', account_holder='Negocio 1', account_type='SAVINGS')
        data = {
            'bank_account': bank_account.id,
            'transaction_type': 'DEPOSIT',
            'amount': 1000.00,
            'date': '2024-10-28',
            'description': 'Depósito inicial'
        }
        response = self.client.post(self.cash_transactions_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CashTransaction.objects.count(), 1)
        self.assertEqual(CashTransaction.objects.first().perfil, self.perfil_1)

    def test_cannot_create_transaction_on_others_account(self):
        """Verifica que no se pueda crear una transacción en una cuenta ajena."""
        other_account = BankAccount.objects.create(perfil=self.perfil_2, bank_name='Banco Ajeno', account_number='789', account_holder='Negocio 2', account_type='SAVINGS')
        data = {
            'bank_account': other_account.id,
            'transaction_type': 'DEPOSIT',
            'amount': 500.00,
            'date': '2024-10-28',
            'description': 'Intento de depósito fraudulento'
        }
        response = self.client.post(self.cash_transactions_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CashTransaction.objects.count(), 0)
