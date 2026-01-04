
import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.db import transaction
from unittest.mock import patch

from api.models import CustomUser, ProviderProfile
from apps.companies.models import Company
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import FacturaVenta
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Cliente
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import ChartOfAccount, JournalEntry, Transaction
from apps.prestadores.mi_negocio.gestion_contable.services import FacturaVentaAccountingService


@pytest.mark.django_db
class FacturaVentaAccountingServiceTests(TestCase):

    def setUp(self):
        """
        Configura un entorno de multi-tenancy con dos prestadores diferentes
        y sus respectivos planes de cuentas.
        """
        self.accounting_service = FacturaVentaAccountingService

        # --- Prestador A ---
        self.user_a = CustomUser.objects.create_user(email='prestador_a@test.com', username='prestador_a', password='pw', role='PRESTADOR')
        self.company_a = Company.objects.create(name='Empresa A', code='COMPA')
        self.profile_a = ProviderProfile.objects.create(usuario=self.user_a, nombre_comercial='Negocio A', company=self.company_a)
        self.cliente_a = Cliente.objects.create(perfil=self.profile_a, nombre='Cliente A', email='cliente_a@test.com')

        self.cxc_a = ChartOfAccount.objects.create(perfil=self.profile_a, code='1305', name='CXC A', nature='DEBITO')
        self.ingresos_a = ChartOfAccount.objects.create(perfil=self.profile_a, code='4135', name='Ingresos A', nature='CREDITO')
        self.iva_a = ChartOfAccount.objects.create(perfil=self.profile_a, code='2408', name='IVA A', nature='CREDITO')

        # --- Prestador B ---
        self.user_b = CustomUser.objects.create_user(email='prestador_b@test.com', username='prestador_b', password='pw', role='PRESTADOR')
        self.company_b = Company.objects.create(name='Empresa B', code='COMPB')
        self.profile_b = ProviderProfile.objects.create(usuario=self.user_b, nombre_comercial='Negocio B', company=self.company_b)
        self.cliente_b = Cliente.objects.create(perfil=self.profile_b, nombre='Cliente B', email='cliente_b@test.com')

        self.cxc_b = ChartOfAccount.objects.create(perfil=self.profile_b, code='1305', name='CXC B', nature='DEBITO')
        self.ingresos_b = ChartOfAccount.objects.create(perfil=self.profile_b, code='4135', name='Ingresos B', nature='CREDITO')

    def _crear_factura(self, perfil, user, cliente, subtotal, impuestos, total, numero='FV-TEST'):
        return FacturaVenta.objects.create(
            perfil=perfil,
            cliente=cliente,
            fecha_emision='2024-01-01',
            numero_factura=numero,
            creado_por=user,
            subtotal=subtotal,
            impuestos=impuestos,
            total=total
        )

    def test_registrar_factura_simple_crea_asiento_balanceado(self):
        factura = self._crear_factura(self.profile_a, self.user_a, self.cliente_a, Decimal('100.00'), Decimal('0.00'), Decimal('100.00'))
        journal_entry = self.accounting_service.registrar_factura_venta(factura)

        self.assertIsNotNone(journal_entry)
        self.assertEqual(journal_entry.transactions.count(), 2)
        debit_trans = journal_entry.transactions.get(account=self.cxc_a)
        self.assertEqual(debit_trans.debit, Decimal('100.00'))
        credit_trans = journal_entry.transactions.get(account=self.ingresos_a)
        self.assertEqual(credit_trans.credit, Decimal('100.00'))

    def test_registrar_factura_con_impuestos_crea_asiento_balanceado(self):
        factura = self._crear_factura(self.profile_a, self.user_a, self.cliente_a, Decimal('100.00'), Decimal('19.00'), Decimal('119.00'))
        journal_entry = self.accounting_service.registrar_factura_venta(factura)

        self.assertIsNotNone(journal_entry)
        self.assertEqual(journal_entry.transactions.count(), 3)
        debit_trans = journal_entry.transactions.get(account=self.cxc_a)
        self.assertEqual(debit_trans.debit, Decimal('119.00'))
        ingresos_trans = journal_entry.transactions.get(account=self.ingresos_a)
        self.assertEqual(ingresos_trans.credit, Decimal('100.00'))
        iva_trans = journal_entry.transactions.get(account=self.iva_a)
        self.assertEqual(iva_trans.credit, Decimal('19.00'))

    def test_falla_si_falta_cuenta_de_iva(self):
        # El Prestador B no tiene cuenta de IVA configurada
        factura = self._crear_factura(self.profile_b, self.user_b, self.cliente_b, Decimal('100.00'), Decimal('19.00'), Decimal('119.00'))

        with self.assertRaises(ValidationError) as context:
            self.accounting_service.registrar_factura_venta(factura)

        self.assertIn("Configuración contable incompleta", str(context.exception))
        self.assertEqual(JournalEntry.objects.filter(perfil=self.profile_b).count(), 0)

    def test_aislamiento_multi_tenant(self):
        """
        Verifica que el asiento de una factura para el Prestador A
        solo utilice cuentas del Prestador A.
        """
        factura = self._crear_factura(self.profile_a, self.user_a, self.cliente_a, Decimal('50.00'), Decimal('0.00'), Decimal('50.00'))
        journal_entry = self.accounting_service.registrar_factura_venta(factura)

        self.assertEqual(journal_entry.perfil, self.profile_a)
        for trans in journal_entry.transactions.all():
            self.assertEqual(trans.account.perfil, self.profile_a)
            self.assertNotIn(trans.account, [self.cxc_b, self.ingresos_b])

    @patch('apps.prestadores.mi_negocio.gestion_contable.contabilidad.models.JournalEntry.clean')
    def test_rollback_si_partida_doble_falla(self, mock_clean):
        """
        Simula un error en la validación de partida doble y verifica que
        la transacción completa se revierta.
        """
        # Configuramos el mock para que lance una ValidationError
        mock_clean.side_effect = ValidationError("Fallo de partida doble simulado")

        factura = self._crear_factura(self.profile_a, self.user_a, self.cliente_a, Decimal('100.00'), Decimal('0.00'), Decimal('100.00'))

        with self.assertRaises(ValidationError):
            # Usamos transaction.atomic() aquí para simular el comportamiento del ViewSet
            with transaction.atomic():
                self.accounting_service.registrar_factura_venta(factura)

        # Verificamos que no se haya creado NADA en la base de datos
        self.assertEqual(JournalEntry.objects.count(), 0)
        self.assertEqual(Transaction.objects.count(), 0)
