from typing import Dict, Any, List
from decimal import Decimal

class PostingRules:
    """
    Motor Declarativo de Reglas Contables.
    Define cómo los eventos de negocio impactan el libro mayor.
    """

    @staticmethod
    def get_rule_for_event(event_type: str, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        rules = {
            "ReservationConfirmed": PostingRules.rule_reservation_confirmed,
            "PaymentReceived": PostingRules.rule_payment_received,
            "ProviderPaid": PostingRules.rule_provider_paid,
            # Compatibility with old types
            "SALE": PostingRules.rule_sale,
            "LIQUIDATION": PostingRules.rule_liquidation,
            "MANUAL_ENTRY": PostingRules.rule_manual_entry,
        }

        rule_func = rules.get(event_type)
        if not rule_func:
            return []

        return rule_func(payload)

    @staticmethod
    def rule_reservation_confirmed(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Flujo de Reserva Confirmada:
        - Accounts Receivable (130505): Debit $1,000 (Cliente debe)
        - Revenue - Commission (413501): Credit $100 (Ganancia Plataforma)
        - Payable to Provider (233505): Credit $900 (Deuda con el prestador)
        """
        total = Decimal(str(payload.get('total_amount', 0)))
        commission_rate = Decimal(str(payload.get('commission_rate', 0.10)))

        commission = total * commission_rate
        provider_payable = total - commission

        description = f"Reserva {payload.get('reference', 'N/A')}"

        return [
            {
                'account': '130505',
                'debit_amount': total,
                'credit_amount': 0,
                'description': f"AR - {description}"
            },
            {
                'account': '413501',
                'debit_amount': 0,
                'credit_amount': commission,
                'description': f"Ingreso Comisión - {description}"
            },
            {
                'account': '233505',
                'debit_amount': 0,
                'credit_amount': provider_payable,
                'description': f"CxP Proveedor - {description}"
            }
        ]

    @staticmethod
    def rule_payment_received(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Flujo de Pago Recibido:
        - Cash / Bank (111005): Debit $1,000
        - Accounts Receivable (130505): Credit $1,000
        """
        amount = Decimal(str(payload.get('amount', 0)))
        description = f"Pago Reserva {payload.get('reference', 'N/A')}"

        return [
            {
                'account': '111005',
                'debit_amount': amount,
                'credit_amount': 0,
                'description': description
            },
            {
                'account': '130505',
                'debit_amount': 0,
                'credit_amount': amount,
                'description': f"Cruce Factura - {description}"
            }
        ]

    @staticmethod
    def rule_provider_paid(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Flujo de Pago al Proveedor:
        - Payable to Provider (233505): Debit $900
        - Cash (111005): Credit $900
        """
        amount = Decimal(str(payload.get('amount', 0)))
        description = f"Liquidación a Proveedor - Ref: {payload.get('reference', 'N/A')}"

        return [
            {
                'account': '233505',
                'debit_amount': amount,
                'credit_amount': 0,
                'description': description
            },
            {
                'account': '111005',
                'debit_amount': 0,
                'credit_amount': amount,
                'description': description
            }
        ]

    # --- Compatibility Rules ---
    @staticmethod
    def rule_sale(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        amount = Decimal(str(payload.get('amount', 0)))
        return [
            {'account': '130505', 'debit_amount': amount, 'credit_amount': 0, 'description': payload.get('description', '')},
            {'account': '413501', 'debit_amount': 0, 'credit_amount': amount, 'description': payload.get('description', '')}
        ]

    @staticmethod
    def rule_liquidation(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        amount = Decimal(str(payload.get('amount', 0)))
        return [
            {'account': '111005', 'debit_amount': amount, 'credit_amount': 0, 'description': payload.get('description', '')},
            {'account': '112505', 'debit_amount': 0, 'credit_amount': amount, 'description': payload.get('description', '')}
        ]

    @staticmethod
    def rule_manual_entry(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Allows posting manual entries via LedgerEngine for testing.
        payload['lines'] = [ {'account': '...', 'debit': 100, 'credit': 0}, ... ]
        """
        lines = []
        for line in payload.get('lines', []):
            lines.append({
                'account': line['account'],
                'debit_amount': Decimal(str(line.get('debit', 0))),
                'credit_amount': Decimal(str(line.get('credit', 0))),
                'description': line.get('description', payload.get('reference', 'Manual Entry'))
            })
        return lines
