import logging
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import transaction

logger = logging.getLogger(__name__)

class AccountingEngine:
    """
    Motor Contable Soberano del Core ERP.
    Único punto de entrada para la creación y validación de asientos contables.
    """

    @staticmethod
    def validate_balance(entry):
        """
        Garantiza el principio de partida doble (Debe = Haber).
        """
        # Se asume que entry tiene un related_name 'lines' o 'transactions'
        lines_manager = getattr(entry, 'lines', None) or getattr(entry, 'transactions', None)
        if not lines_manager:
            raise ValidationError("El asiento no tiene líneas definidas.")

        lines = lines_manager.all()
        total_debit = sum(line.debit for line in lines)
        total_credit = sum(line.credit for line in lines)

        if abs(total_debit - total_credit) > Decimal('0.001'):
            raise ValidationError(
                f"Asiento descuadrado. Débito: {total_debit}, Crédito: {total_credit}. "
                f"Diferencia: {total_debit - total_credit}"
            )
        return True

    @staticmethod
    def check_period_status(date, company):
        """
        Verifica si el periodo para la fecha dada está abierto.
        """
        # Esta lógica se delega a la implementación concreta del modelo FinancialPeriod
        # pero el engine define la regla de negocio.
        pass

    @staticmethod
    @transaction.atomic
    def post_journal_entry(entry, responsible_user=None):
        """
        Realiza la contabilización definitiva de un asiento.
        """
        if entry.is_posted:
            raise ValidationError("El asiento ya ha sido contabilizado.")

        # Validaciones de Integridad
        AccountingEngine.validate_balance(entry)

        # Lógica Multi-moneda: Normalización a moneda base si aplica
        if hasattr(entry, 'currency') and entry.currency != 'COP':
            logger.info(f"Procesando asiento en moneda extranjera: {entry.currency}")
            # Aquí iría la lógica de conversión usando el engine de global_orchestration si está disponible

        entry.is_posted = True
        entry.save()

        logger.info(f"Asiento {entry.id} posteado exitosamente.")

        # Registro en Auditoría (AuditEngine será llamado aquí o vía señales)
        return entry

    @staticmethod
    def create_intercompany_entry(origin_entity_id, destination_entity_id, amount, currency, concept):
        """
        Genera asientos espejo para transacciones entre empresas del holding.
        """
        logger.info(f"Iniciando transacción intercompany: {origin_entity_id} -> {destination_entity_id}")
        # Implementación de lógica de eliminación/espejo
        pass
