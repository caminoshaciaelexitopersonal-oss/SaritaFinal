from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from apps.core_erp.events.erp_events import DomainEvent

@dataclass
class AccountingEvent(DomainEvent):
    """Base class for accounting-related events."""
    organization_id: str = ""

@dataclass
class JournalEntryPosted(AccountingEvent):
    entry_id: str = ""
    total_amount: float = 0.0

@dataclass
class FinancialDiscrepancyDetected(AccountingEvent):
    reason: str = ""
    details: Dict[str, Any] = field(default_factory=dict)
