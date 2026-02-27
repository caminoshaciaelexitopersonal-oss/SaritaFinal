import logging
from typing import Dict, Any, List
from .models import StrategicRule, DecisionProposal
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel, AuthorityLevel
from apps.core_erp.event_bus import EventBus
from django.db import transaction

logger = logging.getLogger(__name__)

class EnterpriseDecisionEngine:
    """
    Main EOS Decision Orchestrator.
    Evaluates rules and generates proposals based on systemic metrics.
    """

    @staticmethod
    def process_metric_update(metric_name: str, value: Any, context: Dict[str, Any] = None):
        """
        Entry point when a system metric (KPI) is updated.
        """
        logger.info(f"EOS DECISION ENGINE: Evaluating rules for metric '{metric_name}' = {value}")

        active_rules = StrategicRule.objects.filter(trigger_metric=metric_name, is_active=True)

        for rule in active_rules:
            if EnterpriseDecisionEngine._evaluate_condition(rule.condition_expression, value):
                EnterpriseDecisionEngine._generate_proposal(rule, value, context)

    @staticmethod
    def _evaluate_condition(expression: str, value: Any) -> bool:
        """
        Evaluates a logic expression against a value without using eval().
        Supports simple operators: <, >, <=, >=, ==, !=
        Expected format: 'metric < 100'
        """
        try:
            parts = expression.split()
            if len(parts) != 3 or parts[0] != 'metric':
                logger.error(f"EOS ERROR: Invalid condition format '{expression}'. Expected 'metric <op> <val>'.")
                return False

            operator = parts[1]
            threshold = float(parts[2])
            metric_val = float(value)

            if operator == '<': return metric_val < threshold
            if operator == '>': return metric_val > threshold
            if operator == '<=': return metric_val <= threshold
            if operator == '>=': return metric_val >= threshold
            if operator == '==': return metric_val == threshold
            if operator == '!=': return metric_val != threshold

            return False
        except Exception as e:
            logger.error(f"EOS ERROR: Failed to parse condition '{expression}': {e}")
            return False

    @staticmethod
    def _generate_proposal(rule: StrategicRule, current_value: Any, context: Dict[str, Any] = None):
        """
        Generates a DecisionProposal for human or automated approval.
        """
        with transaction.atomic():
            proposal = DecisionProposal.objects.create(
                origin_metric=rule.trigger_metric,
                metric_value=current_value,
                evaluated_risk=rule.risk_weight, # Risk score component
                suggested_action={
                    "intention": rule.recommended_action,
                    "parameters": context or {}
                },
                governance_status=DecisionProposal.Status.PENDING,
                tenant_id=rule.tenant_id
            )

            logger.warning(f"EOS PROPOSAL GENERATED: {proposal.id} for {rule.recommended_action}")

            # Emit Event for UI update
            EventBus.emit("STRATEGIC_PROPOSAL_GENERATED", {
                "proposal_id": str(proposal.id),
                "risk": proposal.evaluated_risk,
                "action": rule.recommended_action
            })

            # Auto-execute if authorized by rule and Governance Policy
            if rule.auto_execute:
                EnterpriseDecisionEngine.execute_proposal(proposal.id, auto=True)

    @staticmethod
    def execute_proposal(proposal_id: str, user=None, auto=False):
        """
        Validates and executes a proposal via GovernanceKernel.
        """
        proposal = DecisionProposal.objects.get(id=proposal_id)

        if proposal.executed:
            return {"status": "ALREADY_EXECUTED"}

        # Kernel validation is mandatory
        kernel = GovernanceKernel(user=user)

        try:
            action = proposal.suggested_action
            result = kernel.resolve_and_execute(
                intention_name=action["intention"],
                parameters=action["parameters"]
            )

            proposal.governance_status = DecisionProposal.Status.EXECUTED
            proposal.executed = True
            proposal.execution_result = result
            proposal.save()

            return result
        except Exception as e:
            logger.error(f"EOS EXECUTION FAILED: {proposal_id} - {e}")
            proposal.governance_status = DecisionProposal.Status.FAILED
            proposal.save()
            raise e
