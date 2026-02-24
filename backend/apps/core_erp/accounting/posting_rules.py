from typing import Dict, Any, List
from decimal import Decimal

class PostingRules:
    """
    Defines the logic of how business events translate into accounting entries.
    Acts as a mapping layer between Event Payloads and Journal Lines.
    """

    @staticmethod
    def get_lines_for_sale(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        amount = Decimal(str(payload.get('amount', 0)))
        return [
            {
                'account': '130505', # Accounts Receivable (Clientes)
                'debit': amount,
                'credit': 0,
                'description': f"Venta: {payload.get('description', '')}"
            },
            {
                'account': '413501', # Revenue (Comercio al por mayor y menor)
                'debit': 0,
                'credit': amount,
                'description': f"Venta: {payload.get('description', '')}"
            }
        ]

    @staticmethod
    def get_lines_for_liquidation(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        amount = Decimal(str(payload.get('amount', 0)))
        return [
            {
                'account': '111005', # Bank (Bancos)
                'debit': amount,
                'credit': 0,
                'description': f"Liquidación recibida: {payload.get('description', '')}"
            },
            {
                'account': '112505', # Intercompany/Wallet Bridge
                'debit': 0,
                'credit': amount,
                'description': f"Liquidación recibida: {payload.get('description', '')}"
            }
        ]

    @staticmethod
    def get_lines_for_expense(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        amount = Decimal(str(payload.get('amount', 0)))
        return [
            {
                'account': '510506', # Salaries (Sueldos) - Generic example
                'debit': amount,
                'credit': 0,
                'description': f"Gasto: {payload.get('description', '')}"
            },
            {
                'account': '111005', # Bank
                'debit': 0,
                'credit': amount,
                'description': f"Gasto: {payload.get('description', '')}"
            }
        ]
