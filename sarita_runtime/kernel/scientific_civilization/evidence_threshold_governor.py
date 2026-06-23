class EvidenceThresholdGovernor:
    def get_threshold(self, domain_risk):
        # Higher thresholds for riskier domains
        return 0.7 + (domain_risk * 0.2)
