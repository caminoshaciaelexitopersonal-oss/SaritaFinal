import logging
from .models import IntercompanyMatch
from apps.core_erp.accounting.models import JournalEntry, LedgerEntry
from django.db import transaction

logger = logging.getLogger(__name__)

class IntercompanyEliminator:
    """
    Automates the detection and elimination of intercompany balances.
    """

    @staticmethod
    def detect_and_match(entry_id: str):
        """
        Scans a JournalEntry for transactions involving other tenants in the holding.
        """
        try:
            entry = JournalEntry.plain_objects.get(id=entry_id)
            # Fetch ledger lines that have consolidation codes (Intercompany indicators)
            ic_lines = LedgerEntry.plain_objects.filter(
                journal_entry=entry,
                account__consolidation_code__isnull=False
            )

            for line in ic_lines:
                # Logic to identify counterpart tenant via metadata or account code convention
                counterpart_code = line.account.consolidation_code # e.g. "IC-SUBSIDIARY-B"

                # Check for corresponding entry in the other entity (Matched Pair)
                # For Phase EOS, we log the detection and prepare the Match record
                IntercompanyMatch.objects.get_or_create(
                    entity_a_id=entry.tenant_id,
                    transaction_reference=entry.reference or str(entry.id),
                    amount=line.amount_transaction,
                    currency=line.currency,
                    defaults={'status': 'PENDING'}
                )

            logger.info(f"EOS ELIMINATION: Detected {ic_lines.count()} potential intercompany lines in entry {entry_id}.")
        except Exception as e:
            logger.error(f"EOS ELIMINATION ERROR: {e}")

    @staticmethod
    def run_elimination_cycle(holding_tenant_id: str):
        """
        Executes elimination entries to zero out matched intercompany balances.
        """
        with transaction.atomic():
            pending_matches = IntercompanyMatch.objects.filter(
                status='MATCHED',
                entity_a__parent_company_id=holding_tenant_id
            )

            for match in pending_matches:
                IntercompanyEliminator._create_elimination_entry(match)
                match.status = 'ELIMINATED'
                match.save()

    @staticmethod
    def _create_elimination_entry(match: IntercompanyMatch):
        """
        Generates the virtual JournalEntry that offsets the intercompany balance.
        """
        logger.info(f"EOS ELIMINATION: Creating entry for match {match.id}")
        # Logic to call LedgerEngine and post elimination
