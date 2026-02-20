import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class ChartOfAccountsManager:
    """
    Gestiona la estructura lógica del Plan de Cuentas (PUC).
    Centraliza la validación de códigos y naturalezas contables.
    """

    # Definición de Naturalezas (Debito/Credito) por Clase de Cuenta
    CLASS_NATURES = {
        '1': 'DEBIT',  # Activo
        '2': 'CREDIT', # Pasivo
        '3': 'CREDIT', # Patrimonio
        '4': 'CREDIT', # Ingresos
        '5': 'DEBIT',  # Gastos
        '6': 'DEBIT',  # Costos de Venta
        '7': 'DEBIT',  # Costos de Producción
    }

    @staticmethod
    def validate_account_code(code):
        if not code or not code.isdigit():
            raise ValidationError(f"Código de cuenta inválido: {code}. Debe ser numérico.")

        first_digit = code[0]
        if first_digit not in ChartOfAccountsManager.CLASS_NATURES:
            raise ValidationError(f"Clase de cuenta no reconocida: {first_digit}")

    @staticmethod
    def get_account_nature(code):
        first_digit = code[0]
        return ChartOfAccountsManager.CLASS_NATURES.get(first_digit, 'DEBIT')

    @staticmethod
    def is_debit_increase(code):
        return ChartOfAccountsManager.get_account_nature(code) == 'DEBIT'
