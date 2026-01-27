# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
import datetime

from backend.models import PlanDeCuentas, Cuenta, PeriodoContable, AsientoContable
from backend.services import ContabilidadService, ContabilidadValidationError
from backend.apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

User = get_user_model()

class ContabilidadServiceTests(TestCase):

    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.user = User.objects.create_user(username='testuser', password='password', email='test@test.com', role='PRESTADOR')
        self.provider = ProviderProfile.objects.create(usuario=self.user, nombre_comercial='Hotel Paraiso')

        self.plan = PlanDeCuentas.objects.create(provider=self.provider, nombre='Plan Hotelero 2024')

        self.cuenta_caja = Cuenta.objects.create(
            provider=self.provider, plan_de_cuentas=self.plan, nombre='Caja General', codigo='110505', tipo=Cuenta.TipoCuenta.ACTIVO
        )
        self.cuenta_ingresos = Cuenta.objects.create(
            provider=self.provider, plan_de_cuentas=self.plan, nombre='Ingresos por Alojamiento', codigo='413505', tipo=Cuenta.TipoCuenta.INGRESOS
        )
        self.cuenta_gastos = Cuenta.objects.create(
            provider=self.provider, plan_de_cuentas=self.plan, nombre='Gastos de Limpieza', codigo='513510', tipo=Cuenta.TipoCuenta.GASTOS
        )

        self.periodo = PeriodoContable.objects.create(
            provider=self.provider, nombre='Enero 2024', fecha_inicio=datetime.date(2024, 1, 1), fecha_fin=datetime.date(2024, 1, 31)
        )

    def test_crear_asiento_balanceado_exitoso(self):
        """Verifica que un asiento contable balanceado se crea correctamente."""
        transacciones_data = [
            {'cuenta_id': self.cuenta_caja.id, 'debito': '100.00', 'credito': '0.00'},
            {'cuenta_id': self.cuenta_ingresos.id, 'debito': '0.00', 'credito': '100.00'},
        ]

        asiento = ContabilidadService.crear_asiento_completo(
            provider=self.provider,
            fecha=datetime.date(2024, 1, 15),
            descripcion='Venta de habitación 101',
            periodo=self.periodo,
            creado_por=self.user,
            transacciones_data=transacciones_data
        )

        self.assertIsNotNone(asiento)
        self.assertEqual(AsientoContable.objects.count(), 1)
        self.assertEqual(asiento.transacciones.count(), 2)

        total_debito = sum(t.debito for t in asiento.transacciones.all())
        total_credito = sum(t.credito for t in asiento.transacciones.all())

        self.assertEqual(total_debito, Decimal('100.00'))
        self.assertEqual(total_credito, Decimal('100.00'))

    def test_crear_asiento_no_balanceado_falla(self):
        """Verifica que el servicio rechaza un asiento no balanceado."""
        transacciones_data = [
            {'cuenta_id': self.cuenta_caja.id, 'debito': '100.00', 'credito': '0.00'},
            {'cuenta_id': self.cuenta_ingresos.id, 'debito': '0.00', 'credito': '99.00'}, # Desbalance
        ]

        with self.assertRaises(ContabilidadValidationError) as cm:
            ContabilidadService.crear_asiento_completo(
                provider=self.provider,
                fecha=datetime.date(2024, 1, 16),
                descripcion='Intento de venta con desbalance',
                periodo=self.periodo,
                creado_por=self.user,
                transacciones_data=transacciones_data
            )

        self.assertEqual(AsientoContable.objects.count(), 0)
        self.assertIn("El asiento no está balanceado", str(cm.exception))

    def test_crear_asiento_sin_valor_falla(self):
        """Verifica que el servicio rechaza un asiento con valor cero."""
        transacciones_data = [
            {'cuenta_id': self.cuenta_caja.id, 'debito': '0.00', 'credito': '0.00'},
            {'cuenta_id': self.cuenta_ingresos.id, 'debito': '0.00', 'credito': '0.00'},
        ]

        with self.assertRaises(ContabilidadValidationError):
            ContabilidadService.crear_asiento_completo(
                provider=self.provider,
                fecha=datetime.date(2024, 1, 17),
                descripcion='Asiento sin valor',
                periodo=self.periodo,
                creado_por=self.user,
                transacciones_data=transacciones_data
            )

        self.assertEqual(AsientoContable.objects.count(), 0)

    def test_crear_asiento_con_cuenta_ajena_falla(self):
        """Verifica que no se puede crear un asiento con cuentas de otro inquilino."""
        otro_user = User.objects.create_user(username='otro', password='password', email='otro@test.com', role='PRESTADOR')
        otro_provider = ProviderProfile.objects.create(usuario=otro_user, nombre_comercial='Pensión La Esquina')
        otro_plan = PlanDeCuentas.objects.create(provider=otro_provider, nombre='Plan Pensión 2024')
        cuenta_ajena = Cuenta.objects.create(
            provider=otro_provider, plan_de_cuentas=otro_plan, nombre='Caja Ajena', codigo='110505', tipo=Cuenta.TipoCuenta.ACTIVO
        )

        transacciones_data = [
            {'cuenta_id': self.cuenta_caja.id, 'debito': '50.00', 'credito': '0.00'},
            {'cuenta_id': cuenta_ajena.id, 'debito': '0.00', 'credito': '50.00'}, # Cuenta de otro provider
        ]

        with self.assertRaises(ContabilidadValidationError) as cm:
            ContabilidadService.crear_asiento_completo(
                provider=self.provider,
                fecha=datetime.date(2024, 1, 18),
                descripcion='Intento de asiento con cuenta ajena',
                periodo=self.periodo,
                creado_por=self.user,
                transacciones_data=transacciones_data
            )

        self.assertEqual(AsientoContable.objects.count(), 0)
        self.assertIn("Una de las cuentas especificadas no existe o no pertenece a tu negocio", str(cm.exception))
