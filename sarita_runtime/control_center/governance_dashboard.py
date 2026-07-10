class GovernanceDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Governance & Compliance",
            "compliance_ratio": state_manager.governance.compliance_ratio,
            "violations": state_manager.governance.violations_detected
        }
