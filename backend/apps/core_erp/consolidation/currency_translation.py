from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

class CurrencyTranslation:
    """
    Handles FX conversion for financial consolidation.
    """

    @staticmethod
    def get_rate(from_currency: str, to_currency: str, period: str = None) -> Decimal:
        """
        Retrieves the exchange rate for a given period.
        In a real scenario, this would query an ExchangeRate model.
        """
        if from_currency == to_currency:
            return Decimal('1.0')

        # This is a placeholder for real FX lookup logic
        # For development/test purposes, we might want to allow setting these via settings or a simple dict
        rates = {
            ('USD', 'COP'): Decimal('4000.0'),
            ('EUR', 'COP'): Decimal('4300.0'),
            ('COP', 'USD'): Decimal('0.00025'),
        }

        return rates.get((from_currency, to_currency), Decimal('1.0'))

    @staticmethod
    def translate(amount: Decimal, from_currency: str, to_currency: str, rate: Decimal = None) -> Decimal:
        """
        Translates an amount from one currency to another.
        """
        if from_currency == to_currency:
            return amount

        if rate is None:
            rate = CurrencyTranslation.get_rate(from_currency, to_currency)

        return amount * rate
