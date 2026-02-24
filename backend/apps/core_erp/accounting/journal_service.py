import logging
from datetime import date
from typing import List, Dict, Any
from django.db import transaction
from .models import JournalEntry, JournalLine, Account, FiscalPeriod

logger = logging.getLogger(__name__)

class JournalService:
    """
    Service layer for Journal Entry lifecycle management.
    """
    @staticmethod
    @transaction.atomic
    def create_entry(
        organization_id: str,
        entry_date: date,
        description: str,
        lines_data: List[Dict[str, Any]],
        reference: str = ""
    ) -> JournalEntry:
        """
        Creates a new journal entry with multiple lines.
        """
        # 1. Resolve Fiscal Period
        period = FiscalPeriod.objects.filter(
            organization_id=organization_id,
            period_start__lte=entry_date,
            period_end__gte=entry_date,
            status='open'
        ).first()

        if not period:
            logger.error(f"No open fiscal period found for {entry_date} (Org: {organization_id})")
            # In some cases we might want to auto-create, but usually it's a configuration error
            raise ValueError(f"No open fiscal period found for date {entry_date}")

        # 2. Create the Header
        entry = JournalEntry.objects.create(
            organization_id=organization_id,
            date=entry_date,
            description=description,
            reference=reference,
            period=period
        )

        # 3. Create Lines
        for line in lines_data:
            account = line['account']
            if isinstance(account, str):
                # Resolve by code if string
                account = Account.objects.get(
                    chart_of_accounts__organization_id=organization_id,
                    code=account
                )

            JournalLine.objects.create(
                journal_entry=entry,
                account=account,
                debit=line.get('debit', 0),
                credit=line.get('credit', 0),
                description=line.get('description', description)
            )

        logger.info(f"Journal Entry created: {entry.id} ({description})")
        return entry
