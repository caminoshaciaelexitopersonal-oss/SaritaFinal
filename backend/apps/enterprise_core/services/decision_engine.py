import logging
from typing import Dict, Any
from ..models.decision_proposal import DecisionProposal
from .strategic_engine import StrategicEngine
from ..integration.governance_adapter import GovernanceAdapter
from apps.core_erp.event_bus import EventBus
from django.db import transaction

logger = logging.getLogger(__name__)

class DecisionEngine:
    """
    Main Orchestrator for Enterprise EOS decisions.
    Integrates all layers from intake to execution.
    """

    @staticmethod
    def process_metric_update(metric_name: str, value: Any, context: Dict[str, Any] = None):
        rules = StrategicEngine.get_matching_rules(metric_name, value)

        for rule in rules:
            DecisionEngine._generate_proposal(rule, value, context)

    @staticmethod
    def _generate_proposal(rule, current_value, context):
        with transaction.atomic():
            proposal = DecisionProposal.objects.create(
                origin_metric=rule.trigger_metric,
                metric_value=current_value,
                evaluated_risk=rule.risk_weight,
                suggested_action={
                    "intention": rule.recommended_action,
                    "parameters": context or {}
                },
                tenant_id=rule.tenant_id
            )

            # Notify System
            EventBus.emit("STRATEGIC_PROPOSAL_GENERATED", {
                "proposal_id": str(proposal.id),
                "action": rule.recommended_action
            })

            if rule.auto_execute:
                DecisionEngine.execute_proposal(proposal.id, auto=True)

    @staticmethod
    def execute_proposal(proposal_id, user=None, auto=False):
        proposal = DecisionProposal.objects.get(id=proposal_id)
        if proposal.executed:
            return {"status": "ALREADY_EXECUTED"}

        # Validate via Governance Validation Layer
        result = GovernanceAdapter.validate_and_execute(
            proposal.suggested_action["intention"],
            proposal.suggested_action["parameters"],
            user=user
        )

        proposal.executed = True
        proposal.governance_status = DecisionProposal.Status.EXECUTED
        proposal.execution_result = result
        proposal.save()

        return result
