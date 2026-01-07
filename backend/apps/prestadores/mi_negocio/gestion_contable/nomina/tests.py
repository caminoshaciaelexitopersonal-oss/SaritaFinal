from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from decimal import Decimal
import datetime

from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.company.models import Company, CompanyEncryptionKey
from .models import Empleado, Contrato, Planilla
from ..contabilidad.models import ChartOfAccount, Account

User = get_user_model()

class NominaServiceIntegrationTest(APITestCase):

    def setUp(self):
        # Crear Compañía y su clave de encriptación
        self.company = Company.objects.create(name="Test Company", code="TC01")
        CompanyEncryptionKey.objects.create(company=self.company)

        # Crear Usuario Prestador
        self.user = User.objects.create_user(
            username='prestador@test.com',
            email='prestador@test.com',
            password='password123',
            role='PRESTADOR'
        )
        self.client.login(email='prestador@test.com', password='password123')

        # Crear Perfil de Prestador
        self.profile = ProviderProfile.objects.create(usuario=self.user, company=self.company, is_active=True)

        # Crear Plan de Cuentas básico
        self.chart_of_accounts = ChartOfAccount.objects.create(profile=self.profile, name='Plan de Cuentas Principal')
        Account.objects.create(chart_of_account=self.chart_of_accounts, code='5105', name='Gastos de Personal', type='EXPENSE')
        Account.objects.create(chart_of_account=self.chart_of_accounts, code='2505', name='Salarios por Pagar', type='LIABILITY')

        # Crear Empleado y Contrato
        self.empleado = Empleado.objects.create(
            perfil=self.profile,
            nombre='Juan',
            apellido='Perez',
            identificacion='123456',
            email='juan@perez.com'
        )
        self.contrato = Contrato.objects.create(
            empleado=self.empleado,
            fecha_inicio=datetime.date(2024, 1, 1),
            salario=Decimal('2000000.00'),
            cargo='Desarrollador',
            activo=True
        )

        # Crear Planilla
        self.planilla = Planilla.objects.create(
            perfil=self.profile,
            periodo_inicio=datetime.date(2024, 1, 1),
            periodo_fin=datetime.date(2024, 1, 30)
        )

    def test_liquidar_planilla_endpoint(self):
        """
        Prueba el endpoint de liquidación de planilla de punta a punta.
        """
        url = reverse('planilla-liquidar-planilla', kwargs={'pk': self.planilla.pk})
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Planilla liquidada y contabilizada correctamente.')

        # Verificar que la planilla cambió de estado
        self.planilla.refresh_from_db()
        self.assertEqual(self.planilla.estado, Planilla.EstadoPlanilla.CONTABILIZADA)

        # Verificar que se creó el detalle de liquidación
        self.assertTrue(self.planilla.detalles_liquidacion.exists())
        detalle = self.planilla.detalles_liquidacion.first()
        self.assertEqual(detalle.empleado, self.empleado)
        self.assertGreater(detalle.valor_cesantias, 0)

        # Verificar que se creó el asiento contable
        from ..contabilidad.models import JournalEntry
        self.assertTrue(JournalEntry.objects.filter(profile=self.profile, description__icontains='Contabilización de nómina').exists())
        journal_entry = JournalEntry.objects.get(profile=self.profile)
        self.assertGreater(journal_entry.total_debits, 0)
        self.assertEqual(journal_entry.total_debits, journal_entry.total_credits)
