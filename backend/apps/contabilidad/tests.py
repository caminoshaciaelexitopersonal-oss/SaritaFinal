# backend/apps/contabilidad/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import Decimal
from django.contrib.auth import get_user_model
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.contabilidad.models import ChartOfAccount, JournalEntry, Transaction

# Importamos las factorías si existieran, si no, creamos los objetos manualmente
# from .factories import UserFactory, ChartOfAccountFactory

User = get_user_model()

class JournalEntryAPITests(APITestCase):
    """
    Suite de pruebas para el endpoint de Asientos Contables, adaptada a la arquitectura de Sarita.
    """
    def setUp(self):
        """Se ejecuta antes de cada prueba individual."""
        # Creamos un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword', role='PRESTADOR')

        # Creamos un Perfil de Prestador para este usuario
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio de Prueba')

        # Autenticamos al usuario para las peticiones
        self.client.force_authenticate(user=self.user)

        # Crear cuentas necesarias para las pruebas, ASOCIADAS AL PERFIL
        self.cash_account = ChartOfAccount.objects.create(perfil=self.perfil, code='110505', name='Caja', nature='DEBITO', allows_transactions=True)
        self.sales_account = ChartOfAccount.objects.create(perfil=self.perfil, code='413501', name='Ingresos', nature='CREDITO', allows_transactions=True)
        self.control_account = ChartOfAccount.objects.create(perfil=self.perfil, code='1000', name='Activo Control', nature='DEBITO', allows_transactions=False)

    def test_create_valid_journal_entry(self):
        """
        Prueba el "camino feliz": crear un asiento contable válido y balanceado.
        """
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30",
            "description": "Venta de prueba",
            "entry_type": "Ingreso",
            "transactions": [
                {"account_code": "110505", "debit": "1190.00", "credit": 0},
                {"account_code": "413501", "debit": 0, "credit": "1190.00"}
            ]
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JournalEntry.objects.count(), 1)
        self.assertEqual(Transaction.objects.count(), 2)
        entry = JournalEntry.objects.first()
        self.assertEqual(entry.description, "Venta de prueba")
        self.assertEqual(entry.user, self.user)
        self.assertEqual(entry.perfil, self.perfil) # Verificar la asignación del perfil

    def test_create_unbalanced_journal_entry_fails(self):
        """
        PRUEBA DE ROBUSTEZ: Un asiento desbalanceado debe ser rechazado por la API.
        """
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Intento fallido", "entry_type": "Error",
            "transactions": [
                {"account_code": "110505", "debit": "1000.00"},
                {"account_code": "413501", "credit": "999.99"} # <- Desbalance
            ]
        }
        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("La partida doble no cuadra", str(response.data))
        self.assertEqual(JournalEntry.objects.count(), 0) # Confirmar que NADA se guardó

    def test_create_entry_on_control_account_fails(self):
        """
        PRUEBA DE ROBUSTEZ: Un asiento sobre una cuenta de control (no transaccional) debe fallar.
        """
        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Intento fallido", "entry_type": "Error",
            "transactions": [
                {"account_code": "1000", "debit": "1000.00"}, # <- Cuenta de control
                {"account_code": "413501", "credit": "1000.00"}
            ]
        }
        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("no permite transacciones", str(response.data))

    def test_cannot_access_other_perfil_data(self):
        """
        PRUEBA DE ROBUSTEZ (SEGURIDAD): Un usuario no puede crear asientos con cuentas de otro perfil.
        """
        # Creamos otro usuario y perfil
        other_user = User.objects.create_user(username='otheruser', password='password', role='PRESTADOR')
        other_perfil = Perfil.objects.create(usuario=other_user, nombre_comercial='Otro Negocio')
        other_account = ChartOfAccount.objects.create(perfil=other_perfil, code='9999', name='Cuenta Ajena', nature='DEBITO', allows_transactions=True)

        url = reverse('mi_negocio:contabilidad_api:journalentry-list')
        payload = {
            "entry_date": "2024-05-30", "description": "Intento de fraude", "entry_type": "Error",
            "transactions": [
                {"account_code": "9999", "debit": "100.00"}, # <-- Usando una cuenta de otro perfil
                {"account_code": "413501", "credit": "100.00"}
            ]
        }
        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("no existe para este negocio", str(response.data))
