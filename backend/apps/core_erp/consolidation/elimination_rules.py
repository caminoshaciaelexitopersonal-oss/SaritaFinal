from typing import List, Dict, Any
from decimal import Decimal
from .models import IntercompanyAccountMapping

class EliminationRules:
    """
    Logic for identifying and neutralizing intercompany transactions.
    """

    @staticmethod
    def get_intercompany_lines(trial_balance_lines: List[Dict[str, Any]], mappings: Any) -> List[Dict[str, Any]]:
        """
        Identifies intercompany lines in a trial balance based on provided mappings.
        mappings: QuerySet of IntercompanyAccountMapping
        """
        intercompany_lines = []

        # Pre-process patterns for efficiency
        patterns = [m.account_name_pattern.lower() for m in mappings]
        prefixes = [m.account_code_prefix for m in mappings if m.account_code_prefix]

        for line in trial_balance_lines:
            name = line.get('account_name', '').lower()
            code = str(line.get('account_code', ''))

            is_ic = False
            if any(p in name for p in patterns):
                is_ic = True
            elif any(code.startswith(pre) for pre in prefixes):
                is_ic = True

            if is_ic:
                intercompany_lines.append(line)

        return intercompany_lines

    @staticmethod
    def eliminate(consolidated_results: Dict[str, Any], ic_lines: List[Dict[str, Any]]):
        """
        Subtracts intercompany lines from consolidated results to neutralize them.
        consolidated_results: { 'account_code': { 'debit': X, 'credit': Y, ... }, ... }
        """
        for line in ic_lines:
            code = line['account_code']
            if code in consolidated_results:
                consolidated_results[code]['debit'] -= line.get('debit', Decimal('0'))
                consolidated_results[code]['credit'] -= line.get('credit', Decimal('0'))
                consolidated_results[code]['balance'] -= line.get('balance', Decimal('0'))
                # Mark as eliminated for traceability
                consolidated_results[code]['is_eliminated'] = True
