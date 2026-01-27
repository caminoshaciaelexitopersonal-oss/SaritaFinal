# Este archivo contendrá la lógica de negocio para el cálculo de nómina y la integración contable.
from decimal import Decimal
from .models import Contrato, Planilla

class CalculoNominaService:
    """
    Servicio para calcular las prestaciones sociales y parafiscales de un empleado.
    """

    def __init__(self, contrato: Contrato, fecha_inicio: str, fecha_fin: str):
        self.contrato = contrato
        self.salario_base = contrato.salario
        # TODO: Considerar auxilio de transporte para la base si aplica
        self.dias_trabajados = (fecha_fin - fecha_inicio).days + 1
        # Simplificación: se asume un año de 360 días para cálculos.
        self.dias_ano = 360

    def calcular_prima(self) -> Decimal:
        """
        Fórmula: (Salario mensual * Días trabajados en el semestre) / 360
        """
        # Simplificación: se asume que la planilla es semestral.
        dias_semestre = self.dias_trabajados
        prima = (self.salario_base * Decimal(dias_semestre)) / self.dias_ano
        return prima.quantize(Decimal('0.01'))

    def calcular_cesantias(self) -> Decimal:
        """
        Fórmula: (Salario mensual * Días trabajados) / 360
        """
        cesantias = (self.salario_base * Decimal(self.dias_trabajados)) / self.dias_ano
        return cesantias.quantize(Decimal('0.01'))

    def calcular_intereses_cesantias(self, valor_cesantias: Decimal) -> Decimal:
        """
        Fórmula: (Cesantías * Días trabajados * 0.12) / 360
        """
        intereses = (valor_cesantias * Decimal(self.dias_trabajados) * Decimal('0.12')) / self.dias_ano
        return intereses.quantize(Decimal('0.01'))

    def calcular_vacaciones(self) -> Decimal:
        """
        Fórmula: (Salario mensual básico * Días trabajados) / 720
        """
        vacaciones = (self.salario_base * Decimal(self.dias_trabajados)) / (self.dias_ano * 2)
        return vacaciones.quantize(Decimal('0.01'))

    def calcular_parafiscales(self) -> dict:
        """
        Cálculo de aportes parafiscales (CCF, ICBF, SENA)
        Base: Salario base (simplificado, debería ser el IBC)
        - CCF: 4%
        - ICBF: 3%
        - SENA: 2%
        """
        # TODO: Implementar el cálculo del Ingreso Base de Cotización (IBC) correctamente.
        # Por ahora, se usa el salario base como simplificación.
        base_cotizacion = self.salario_base

        aporte_ccf = base_cotizacion * Decimal('0.04')
        aporte_icbf = base_cotizacion * Decimal('0.03')
        aporte_sena = base_cotizacion * Decimal('0.02')

        return {
            "aporte_ccf": aporte_ccf.quantize(Decimal('0.01')),
            "aporte_icbf": aporte_icbf.quantize(Decimal('0.01')),
            "aporte_sena": aporte_sena.quantize(Decimal('0.01')),
        }

from ..contabilidad.models import JournalEntry, Transaction
from ..contabilidad.services import ChartOfAccountService
from .models import DetalleLiquidacion
from django.utils import timezone

class ContabilidadNominaService:
    """
    Servicio para contabilizar la liquidación de la nómina.
    """
    def __init__(self, planilla: Planilla):
        self.planilla = planilla
        self.perfil = planilla.perfil
        self.chart_of_accounts = ChartOfAccountService(self.perfil)

    def contabilizar_liquidacion(self):
        """
        Crea el asiento contable para la liquidación de la planilla.
        - Debita las cuentas de gasto (salarios, prestaciones, parafiscales).
        - Acredita las cuentas de pasivo (salarios por pagar, provisiones).
        """
        description = f"Contabilización de nómina para el período {self.planilla.periodo_inicio} a {self.planilla.periodo_fin}"

        journal_entry = JournalEntry.objects.create(
            profile=self.perfil,
            date=timezone.now().date(),
            description=description,
            is_automatic=True
        )

        total_gastos = Decimal('0.00')
        total_pasivos = Decimal('0.00')

        detalles = DetalleLiquidacion.objects.filter(planilla=self.planilla)

        for detalle in detalles:
            # Gastos (Débito)
            gasto_prima = detalle.valor_prima
            gasto_cesantias = detalle.valor_cesantias
            gasto_intereses = detalle.valor_intereses_cesantias
            gasto_vacaciones = detalle.valor_vacaciones
            gasto_parafiscales = detalle.valor_aporte_ccf + detalle.valor_aporte_icbf + detalle.valor_aporte_sena

            total_gastos += gasto_prima + gasto_cesantias + gasto_intereses + gasto_vacaciones + gasto_parafiscales

            # Pasivos (Crédito)
            # Aquí se asumen cuentas genéricas. Una implementación real requeriría un mapeo de cuentas.
            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_expense_account(), debit=gasto_prima, description=f"Gasto Prima {detalle.empleado}")
            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_liability_account(), credit=gasto_prima, description=f"Provisión Prima {detalle.empleado}")

            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_expense_account(), debit=gasto_cesantias, description=f"Gasto Cesantías {detalle.empleado}")
            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_liability_account(), credit=gasto_cesantias, description=f"Provisión Cesantías {detalle.empleado}")

            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_expense_account(), debit=gasto_intereses, description=f"Gasto Intereses Cesantías {detalle.empleado}")
            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_liability_account(), credit=gasto_intereses, description=f"Provisión Intereses Cesantías {detalle.empleado}")

            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_expense_account(), debit=gasto_vacaciones, description=f"Gasto Vacaciones {detalle.empleado}")
            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_liability_account(), credit=gasto_vacaciones, description=f"Provisión Vacaciones {detalle.empleado}")

            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_expense_account(), debit=gasto_parafiscales, description=f"Gasto Parafiscales {detalle.empleado}")
            Transaction.objects.create(journal_entry=journal_entry, account=self.chart_of_accounts.get_liability_account(), credit=gasto_parafiscales, description=f"Parafiscales por Pagar {detalle.empleado}")

        journal_entry.validate_debits_and_credits()
        return journal_entry
