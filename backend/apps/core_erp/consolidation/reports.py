from typing import Dict, Any, List
from decimal import Decimal
from .consolidation_engine import ConsolidationEngine
from .models import HoldingEntity, ConsolidatedReportSnapshot
from .currency_translation import CurrencyTranslation

class ConsolidationReports:
    """
    Generates high-level financial statements from consolidated data.
    """

    @staticmethod
    def get_consolidated_balance_sheet(holding_id: str, cutoff_date: Any = None) -> Dict[str, Any]:
        """
        Consolidated Balance Sheet.
        """
        tb = ConsolidationEngine.get_consolidated_trial_balance(holding_id, cutoff_date)

        report = {
            'report_type': 'Consolidated Balance Sheet',
            'holding_name': tb['holding_name'],
            'cutoff_date': tb['cutoff_date'],
            'base_currency': tb['base_currency'],
            'assets': Decimal('0'),
            'liabilities': Decimal('0'),
            'equity': Decimal('0'),
            'details': []
        }

        for line in tb['lines']:
            code = line['account_code']
            if code.startswith('1'):
                report['assets'] += line['balance']
                report['details'].append(line)
            elif code.startswith('2'):
                report['liabilities'] += line['balance']
                report['details'].append(line)
            elif code.startswith('3'):
                report['equity'] += line['balance']
                report['details'].append(line)

        report['check'] = report['assets'] - (report['liabilities'] + report['equity'])

        # Save Snapshot for audit
        ConsolidationReports.save_snapshot(holding_id, 'BALANCE_SHEET', tb['cutoff_date'], report)

        return report

    @staticmethod
    def get_consolidated_income_statement(holding_id: str, cutoff_date: Any = None) -> Dict[str, Any]:
        """
        Consolidated Income Statement (P&L).
        """
        tb = ConsolidationEngine.get_consolidated_trial_balance(holding_id, cutoff_date)

        report = {
            'report_type': 'Consolidated Income Statement',
            'holding_name': tb['holding_name'],
            'cutoff_date': tb['cutoff_date'],
            'base_currency': tb['base_currency'],
            'income': Decimal('0'),
            'expenses': Decimal('0'),
            'details': []
        }

        for line in tb['lines']:
            code = line['account_code']
            if code.startswith('4'):
                report['income'] += line['balance'] # Assuming Credit balance is positive for income here
                report['details'].append(line)
            elif code.startswith('5'):
                report['expenses'] += line['balance'] # Assuming Debit balance is positive for expense here
                report['details'].append(line)

        report['net_income'] = report['income'] - report['expenses']

        # Save Snapshot
        ConsolidationReports.save_snapshot(holding_id, 'INCOME_STATEMENT', tb['cutoff_date'], report)

        return report

    @staticmethod
    def save_snapshot(holding_id: str, report_type: str, period: str, data: Dict[str, Any]):
        """
        Guarda una captura inmutable del reporte para auditoría.
        """
        holding = HoldingEntity.objects.get(id=holding_id)

        # Capturar tasas de cambio usadas (simplificado para este engine)
        fx_rates = {}
        for membership in holding.memberships.all():
            fx_rates[membership.tenant.currency] = str(CurrencyTranslation.get_rate(membership.tenant.currency, holding.base_currency))

        # Convertir Decimales a String para JSON
        import json
        from decimal import Decimal

        class DecimalEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, Decimal):
                    return str(obj)
                return super(DecimalEncoder, self).default(obj)

        json_data = json.loads(json.dumps(data, cls=DecimalEncoder))

        ConsolidatedReportSnapshot.objects.create(
            holding=holding,
            report_type=report_type,
            period=period,
            fx_rates_used=fx_rates,
            tenants_included=[str(m.tenant.id) for m in holding.memberships.all()],
            data=json_data,
            method_applied="VARIES_BY_MEMBERSHIP"
        )
