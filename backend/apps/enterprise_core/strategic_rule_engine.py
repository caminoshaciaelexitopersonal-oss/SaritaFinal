from typing import Dict, Any, List
from .models import StrategicRule

class StrategicRuleEngine:
    """
    Manages and retrieves strategic rules for execution.
    """

    def get_rules_for_domain(self, domain: str) -> List[StrategicRule]:
        return StrategicRule.objects.filter(trigger_metric__startswith=domain, is_active=True)

    def register_default_rules(self):
        """
        Bootstrap baseline rules for EOS.
        """
        StrategicRule.objects.get_or_create(
            trigger_metric='CASH_FLOW_CRITICAL',
            condition_expression='metric < 0',
            defaults={
                'risk_weight': 0.8,
                'recommended_action': 'ERP_VIEW_CASH_FLOW', # Placeholder for real action
                'auto_execute': False
            }
        )
