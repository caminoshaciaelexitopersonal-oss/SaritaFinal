# backend/apps/activos/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.management import call_command
from apps.prestadores.models import Perfil
from apps.contabilidad.models import JournalEntry, ChartOfAccount
from .models import ActivoFijo
import datetime

User = get_user_model()

class ActivosFijosTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'p', role='prestador')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio Activos')

        # Cuentas contables para depreciación
        ChartOfAccount.objects.create(perfil=self.perfil, code='5160', name='Gasto Depreciación', nature='DEBITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil, code='1592', name='Depreciación Acumulada', nature='CREDITO', allows_transactions=True)

    def test_comando_depreciar_activos_y_contabiliza(self):
        """
        Prueba el flujo completo: el comando de gestión calcula la depreciación,
        actualiza el activo y la señal de `RegistroDepreciacion` crea el asiento contable.
        """
        activo = ActivoFijo.objects.create(
            perfil=self.perfil,
            nombre='Computador',
            fecha_adquisicion=datetime.date.today() - datetime.timedelta(days=60),
            costo_inicial=1200,
            vida_util_meses=12
        )

        # Verificar estado inicial
        self.assertEqual(activo.valor_en_libros, 1200)
        self.assertEqual(JournalEntry.objects.count(), 0)

        # Ejecutar el comando de gestión
        call_command('depreciar_activos')

        # Verificar estado final
        activo.refresh_from_db()
        self.assertEqual(activo.depreciacion_acumulada, 100) # 1200 / 12 meses
        self.assertEqual(activo.valor_en_libros, 1100)

        # Verificar contabilización
        self.assertEqual(JournalEntry.objects.count(), 1)
        entry = JournalEntry.objects.first()
        self.assertEqual(entry.entry_type, 'DEP')
        self.assertTrue(entry.transactions.filter(account__code='5160', debit=100).exists())
        self.assertTrue(entry.transactions.filter(account__code='1592', credit=100).exists())
