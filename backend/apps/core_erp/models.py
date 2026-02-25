import uuid
from django.db import models
from .accounting.models import (
    ChartOfAccounts, Account, FiscalPeriod, JournalEntry, LedgerEntry
)
from .tenancy.models import Tenant
from .consolidation.models import (
    HoldingEntity, HoldingMembership,
    IntercompanyAccountMapping, ConsolidatedReportSnapshot
)
from .taxation.models import (
    Jurisdiction, TaxRule, RegulatoryCalendar, TaxAuditTrail
)
from .intelligence.models import (
    FinancialProjection, StrategicScenario
)
from .base.fx_engine import FXRate
from .base_models import BaseErpModel

class EventAuditLog(BaseErpModel):
    """
    Store for all processed business events.
    Enables total traceability and replayability.
    """
    event_id = models.UUIDField(default=uuid.uuid4, editable=False)
    correlation_id = models.CharField(max_length=100, db_index=True)
    event_type = models.CharField(max_length=100, db_index=True)
    tenant_id = models.CharField(max_length=100, db_index=True, null=True)
    payload = models.JSONField()
    status = models.CharField(max_length=20, default='PROCESSED')
    processed_at = models.DateTimeField(auto_now_add=True)
    error_details = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Event Audit Log"

class AgentActionAudit(BaseErpModel):
    """
    Audit log for all AI Agent actions.
    Ensures AI boundary governance.
    """
    agent_code = models.CharField(max_length=100, db_index=True)
    action = models.CharField(max_length=255)
    service_invoked = models.CharField(max_length=255)
    parameters = models.JSONField()
    result = models.JSONField(null=True)
    correlation_id = models.CharField(max_length=100, db_index=True)
    tenant_id = models.CharField(max_length=100, db_index=True, null=True)

    class Meta:
        app_label = 'core_erp'
        verbose_name = "Agent Action Audit"
