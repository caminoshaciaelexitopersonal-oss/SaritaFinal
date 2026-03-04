from typing import Dict, Any, List
from decimal import Decimal

class PostingRules:
    """
    Motor Declarativo de Reglas Contables.
    Define cómo los eventos de negocio impactan el libro mayor.
    """
    VERSION = "1.0"

    @staticmethod
    def get_rule_for_event(event_type: str, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        rules = {
            "RESERVATION_CREATED": PostingRules.rule_reservation_created,
            "RESERVATION_CONFIRMED": PostingRules.rule_reservation_confirmed,
            "RESERVATION_CANCELLED": PostingRules.rule_reservation_cancelled,
            "PAYMENT_RECEIVED": PostingRules.rule_payment_received,
            "PAYROLL_LIQUIDATED": PostingRules.rule_payroll_liquidated,
            "INVENTORY_ADJUSTED": PostingRules.rule_inventory_adjusted,
            "PURCHASE_ORDER_POSTED": PostingRules.rule_purchase_order_posted,
            "ASSET_DEPRECIATED": PostingRules.rule_asset_depreciated,
            "SALE_COMPLETED": PostingRules.rule_sale,
            "LIQUIDATION": PostingRules.rule_liquidation,
        }

        rule_func = rules.get(event_type)
        if not rule_func:
            return []

        return rule_func(payload)

    @staticmethod
    def rule_reservation_confirmed(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Flujo de Reserva Confirmada (Phase B Flow):
        - Accounts Receivable (130505): Debit Total
        - Revenue - Commission (413501): Credit Commission
        - Tax Payable (240801): Credit Tax
        - Payable to Provider (233505): Credit Net to Provider
        """
        total = Decimal(str(payload.get('total_amount', 0)))
        commission = Decimal(str(payload.get('commission', 0)))
        tax = Decimal(str(payload.get('tax', 0)))

        # If not provided, use default rate logic
        if commission == 0 and tax == 0:
            commission_rate = Decimal(str(payload.get('commission_rate', 0.10)))
            commission = total * commission_rate

        provider_net = total - commission - tax

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
                'account': '240801',
                'debit_amount': 0,
                'credit_amount': tax,
                'description': f"IVA por Pagar - {description}"
            },
            {
                'account': '233505',
                'debit_amount': 0,
                'credit_amount': provider_net,
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

    @staticmethod
    def rule_reservation_created(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Registro de Cuenta por Cobrar al Cliente por Reserva Creada.
        """
        total = Decimal(str(payload.get('total_amount', 0)))
        ref = payload.get('reference', 'N/A')
        return [
            {'account': '130505', 'debit_amount': total, 'credit_amount': 0, 'description': f"CxC Cliente - Reserva {ref}"},
            {'account': '280505', 'debit_amount': 0, 'credit_amount': total, 'description': f"Anticipos Clientes - Reserva {ref}"}
        ]

    @staticmethod
    def rule_reservation_cancelled(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Reversión de Reserva por Cancelación.
        """
        total = Decimal(str(payload.get('total_amount', 0)))
        ref = payload.get('reference', 'N/A')
        return [
            {'account': '280505', 'debit_amount': total, 'credit_amount': 0, 'description': f"Rev. Anticipo - Reserva {ref}"},
            {'account': '130505', 'debit_amount': 0, 'credit_amount': total, 'description': f"Rev. CxC - Reserva {ref}"}
        ]

    @staticmethod
    def rule_payroll_liquidated(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Impacto de Gasto de Nómina.
        """
        net_pay = Decimal(str(payload.get('net_pay', 0)))
        ref = payload.get('reference', 'N/A')
        return [
            {'account': '510506', 'debit_amount': net_pay, 'credit_amount': 0, 'description': f"Gasto Salario - {ref}"},
            {'account': '250505', 'debit_amount': 0, 'credit_amount': net_pay, 'description': f"Salarios por Pagar - {ref}"}
        ]

    @staticmethod
    def rule_inventory_adjusted(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Ajuste de Inventario (Físico vs Sistema).
        """
        val = Decimal(str(payload.get('adjustment_value', 0)))
        ref = payload.get('reference', 'N/A')
        if val > 0: # Entrada
             return [
                {'account': '143505', 'debit_amount': val, 'credit_amount': 0, 'description': f"Ajuste (+) Inv - {ref}"},
                {'account': '425050', 'debit_amount': 0, 'credit_amount': val, 'description': f"Ingreso por Ajuste - {ref}"}
             ]
        else: # Salida
             return [
                {'account': '519595', 'debit_amount': abs(val), 'credit_amount': 0, 'description': f"Gasto por Ajuste - {ref}"},
                {'account': '143505', 'debit_amount': 0, 'credit_amount': abs(val), 'description': f"Ajuste (-) Inv - {ref}"}
             ]

    @staticmethod
    def rule_purchase_order_posted(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Registro de Compra de Mercancía.
        """
        total = Decimal(str(payload.get('total_amount', 0)))
        ref = payload.get('reference', 'N/A')
        return [
            {'account': '143501', 'debit_amount': total, 'credit_amount': 0, 'description': f"Compra Mercancía - {ref}"},
            {'account': '220505', 'debit_amount': 0, 'credit_amount': total, 'description': f"CxP Proveedores Nac - {ref}"}
        ]

    @staticmethod
    def rule_asset_depreciated(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Depreciación Mensual de Activos Fijos.
        """
        val = Decimal(str(payload.get('depreciation_amount', 0)))
        ref = payload.get('reference', 'N/A')
        return [
            {'account': '516005', 'debit_amount': val, 'credit_amount': 0, 'description': f"Gasto Depreciación - {ref}"},
            {'account': '159205', 'debit_amount': 0, 'credit_amount': val, 'description': f"Deprec. Acumulada - {ref}"}
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
