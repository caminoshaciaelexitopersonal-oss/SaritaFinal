import logging
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import JournalEntry, JournalLine

logger = logging.getLogger(__name__)

class LedgerEngine:
    """
    Central engine for ledger operations and integrity.
    """
    @staticmethod
    def validate_double_entry(entry: JournalEntry):
        """
        Validates that debits equal credits.
        """
        lines = entry.lines.all()
        if not lines:
            raise ValidationError("Journal entry has no lines.")

        total_debit = sum(line.debit for line in lines)
        total_credit = sum(line.credit for line in lines)

        if abs(total_debit - total_credit) > Decimal('0.001'):
             raise ValidationError(
                 f"Unbalanced Journal Entry {entry.id}: "
                 f"Debits({total_debit}) != Credits({total_credit}). "
                 f"Diff: {total_debit - total_credit}"
             )
        return True

    @staticmethod
    @transaction.atomic
    def post_entry(entry_id: str):
        """
        Finalizes a journal entry, making it official in the ledger.
        """
        entry = JournalEntry.objects.select_for_update().get(id=entry_id)
        if entry.is_posted:
            logger.warning(f"Entry {entry_id} is already posted.")
            return entry

        # Business rules
        if entry.period.status != 'open':
            raise ValidationError(f"Fiscal period is {entry.period.status}.")

        LedgerEngine.validate_double_entry(entry)

        entry.is_posted = True
        entry.save()

        logger.info(f"Journal Entry {entry_id} successfully posted to ledger.")
        return entry
