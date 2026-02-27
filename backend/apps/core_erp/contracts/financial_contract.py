from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
from datetime import date
from typing import List

@dataclass(frozen=True)
class JournalEntryLineDTO:
    account_id: UUID
    debit: Decimal
    credit: Decimal
    description: str

@dataclass(frozen=True)
class JournalEntryDTO:
    id: UUID
    date: date
    description: str
    lines: List[JournalEntryLineDTO]
    reference: str = ""

class FinancialContract:
    """
    Contrato para integración financiera de alto nivel.
    """
    pass
