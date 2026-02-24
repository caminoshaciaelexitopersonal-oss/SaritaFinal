import logging
from decimal import Decimal
from typing import Dict, List, Any
from django.utils import timezone
from apps.core_erp.accounting.ledger_engine import LedgerEngine
from .models import HoldingEntity, HoldingMembership
from .currency_translation import CurrencyTranslation
from .elimination_rules import EliminationRules

logger = logging.getLogger(__name__)

class ConsolidationEngine:
    """
    Motor de Consolidación Financiera del Core ERP.
    Realiza agregación virtual de múltiples tenants bajo una entidad Holding.
    """

    @staticmethod
    def get_consolidated_trial_balance(holding_id: str, cutoff_date: Any = None) -> Dict[str, Any]:
        """
        Genera un Balance de Prueba consolidado.
        """
        if cutoff_date is None:
            cutoff_date = timezone.now().date()

        holding = HoldingEntity.objects.get(id=holding_id)
        memberships = holding.memberships.all()

        # Estructura: account_code -> { account_name, debit, credit, balance, currency, is_eliminated }
        consolidated_results: Dict[str, Any] = {}

        # 1. Agregación de todos los tenants miembros
        for membership in memberships:
            tenant = membership.tenant
            tb = LedgerEngine.get_trial_balance(str(tenant.id), cutoff_date)

            # Obtener tasa de cambio para el periodo
            rate = CurrencyTranslation.get_rate(tenant.currency, holding.base_currency)

            # Multiplicador según método
            multiplier = Decimal('1.0')
            if membership.consolidation_method == HoldingMembership.ConsolidationMethod.PROPORTIONAL:
                multiplier = membership.ownership_percentage / Decimal('100.0')
            elif membership.consolidation_method == HoldingMembership.ConsolidationMethod.EQUITY:
                # El método de participación suele ser una sola línea, no consolidación línea a línea.
                # Para simplificar este engine, tratamos EQUITY como fuera del alcance de la agregación línea a línea por ahora.
                continue

            for line in tb['lines']:
                code = line['account_code']

                # Traducir montos
                translated_debit = CurrencyTranslation.translate(line['debit'] * multiplier, tenant.currency, holding.base_currency, rate)
                translated_credit = CurrencyTranslation.translate(line['credit'] * multiplier, tenant.currency, holding.base_currency, rate)
                translated_balance = CurrencyTranslation.translate(line['balance'] * multiplier, tenant.currency, holding.base_currency, rate)

                if code not in consolidated_results:
                    consolidated_results[code] = {
                        'account_code': code,
                        'account_name': line['account_name'],
                        'debit': Decimal('0'),
                        'credit': Decimal('0'),
                        'balance': Decimal('0'),
                        'currency': holding.base_currency,
                        'is_eliminated': False
                    }

                consolidated_results[code]['debit'] += translated_debit
                consolidated_results[code]['credit'] += translated_credit
                consolidated_results[code]['balance'] += translated_balance

        # 2. Eliminaciones Intercompany
        mappings = holding.intercompany_mappings.all()
        ic_lines_to_eliminate = []

        for membership in memberships:
            tenant_tb = LedgerEngine.get_trial_balance(str(membership.tenant.id), cutoff_date)
            ic_lines = EliminationRules.get_intercompany_lines(tenant_tb['lines'], mappings)

            # Traducir líneas IC antes de eliminar
            rate = CurrencyTranslation.get_rate(membership.tenant.currency, holding.base_currency)
            for ic in ic_lines:
                ic['debit'] = CurrencyTranslation.translate(ic['debit'], membership.tenant.currency, holding.base_currency, rate)
                ic['credit'] = CurrencyTranslation.translate(ic['credit'], membership.tenant.currency, holding.base_currency, rate)
                ic['balance'] = CurrencyTranslation.translate(ic['balance'], membership.tenant.currency, holding.base_currency, rate)

            ic_lines_to_eliminate.extend(ic_lines)

        EliminationRules.eliminate(consolidated_results, ic_lines_to_eliminate)

        return {
            'holding_id': holding_id,
            'holding_name': holding.name,
            'cutoff_date': str(cutoff_date),
            'base_currency': holding.base_currency,
            'lines': list(consolidated_results.values())
        }
